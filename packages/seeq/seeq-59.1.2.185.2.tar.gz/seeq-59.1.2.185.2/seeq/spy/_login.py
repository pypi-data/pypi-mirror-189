from __future__ import annotations

import datetime
import json
import logging
import os
import re
import warnings
from typing import Optional, Union
from urllib.parse import urlparse, quote

import pandas as pd
import pkg_resources
import pytz
import requests
import urllib3
from dateutil import parser
from dateutil.tz import tz
from seeq import spy, sdk
from seeq.base import system, util
from seeq.sdk import *
from seeq.spy import _common, _datalab
from seeq.spy._config import Setting
from seeq.spy._datalab import is_datalab_functions_project
from seeq.spy._errors import *
from seeq.spy._session import Session
from seeq.spy._status import Status
from urllib3.connectionpool import MaxRetryError, SSLError

AUTOMATIC_PROXY_DETECTION = '__auto__'


def login(username=None, password=None, *, access_key=None, url=None, directory='Seeq',
          ignore_ssl_errors=False, proxy=AUTOMATIC_PROXY_DETECTION, credentials_file=None, force=True,
          quiet=None, status=None, session: Session = None, private_url=None, auth_token=None, csrf_token=None,
          request_origin_label=None, request_origin_url=None):
    """
    Establishes a connection with Seeq Server and logs in with a set of
    credentials. At least one set of credentials must be provided.
    Applicable credential sets are:

        - username + password (where username is in "Seeq" user directory)
        - username + password + directory
        - access_key + password
        - credentials_file (where username is in "Seeq" user directory)
        - credentials_file + directory

    Parameters
    ----------
    username : str, optional
        Username for login purposes. See credentials_file argument for
        alternative.

    password : str, optional
        Password for login purposes. See credentials_file argument for
        alternative.

    access_key: str, optional
        Access Key for login purposes. Access Keys are created by individual
        users via the Seeq user interface in the upper-right user profile
        menu. An Access Key has an associated password that is presented
        to the user (once!) upon creation of the Access Key, and it must be
        supplied via the "password" argument. The "directory" argument must
        NOT be supplied.

    url : str, default 'http://localhost:34216'
        Seeq Server url. You can copy this from your browser and cut off
        everything to the right of the port (if present).
        E.g. https://myseeqserver:34216

    directory : str, default 'Seeq'
        The authentication directory to use. You must be able to supply a
        username/password, so some passwordless Windows Authentication
        (NTLM) scenarios will not work. OpenID Connect is also not
        supported. If you need to use such authentication schemes, set up
        a Seeq Data Lab server.

    ignore_ssl_errors : bool, default False
        If True, SSL certificate validation errors are ignored. Use this
        if you're in a trusted network environment but Seeq Server's SSL
        certificate is not from a common root authority.

    proxy : str, default '__auto__'
        Specifies the proxy server to use for all requests. The default
        value is "__auto__", which examines the standard HTTP_PROXY and
        HTTPS_PROXY environment variables. If you specify None for this
        parameter, no proxy server will be used.

    credentials_file : str, optional
        Reads username and password from the specified file. If specified, the
        file should be plane text and contain two lines, the first line being
        the username, the second being the user's password.

    force : str, default True
        If True, re-logs in even if already already logged in. If False, skips
        login if already logged in. You should include a spy.login(force=False)
        cell if you are creating example notebooks that may be used in Jupyter
        environments like Anaconda, AWS SageMaker or Azure Notebooks.)

    quiet : bool, default False
        If True, suppresses progress output. Note that when status is
        provided, the quiet setting of the Status object that is passed
        in takes precedent.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    session : spy.Session, optional
        If supplied, the Session object (and its Options) will be used to
        store the login session state. This is useful to log in to different
        Seeq servers at the same time or with different credentials.

    private_url : str
        If supplied, this will be the URL used for communication with the Seeq
        Server API over private networks.  Generally for internal use only.

    auth_token : str
        Private argument for Data Lab use only.

    csrf_token : str
        Private argument for Data Lab use only.

    request_origin_label : str
        Used for tracking Data Consumption. If supplied, this label will be added as a header to all requests from
        the logged in user. Not necessary in Data Lab because the header will already be filled in.

    request_origin_url : str
        Used for tracking Data Consumption. If supplied, this label will be added as a header to all requests from
        the logged in user. Not necessary in Data Lab because the header will already be filled in. If NOT in Data
        Lab, supply a full URL that leads to the tool/plugin that is consuming data, if applicable.

    Examples
    --------
    Log in to two different servers at the same time:

    >>> session1 = Session()
    >>> session2 = Session()
    >>> spy.login(url='https://server1.seeq.site', username='mark', password='markpassword', session=session1)
    >>> spy.login(url='https://server2.seeq.site', username='alex', password='alexpassword', session=session2)

    """
    _common.validate_argument_types([
        (username, 'username', str),
        (password, 'password', str),
        (access_key, 'access_key', str),
        (url, 'url', str),
        (private_url, 'private_url', str),
        (directory, 'directory', str),
        (ignore_ssl_errors, 'ignore_ssl_errors', bool),
        (proxy, 'proxy', str),
        (credentials_file, 'credentials_file', str),
        # Note: Although auth_token is no longer a supported authentication method for non-Seeq Data Lab scenarios,
        # it is still used by Seeq Data Lab code to log the user in.
        (auth_token, 'auth_token', str),
        (csrf_token, 'csrf_token', str),
        (force, 'force', bool),
        (quiet, 'quiet', bool),
        (status, 'status', Status),
        (session, 'session', Session)
    ])

    status = Status.validate(status, quiet)
    session = Session.validate(session)

    if private_url is not None and url is None:
        raise SPyValueError('private_url argument cannot be specified without also specifying url argument')

    try:
        _login(username, password, access_key, url, directory, ignore_ssl_errors, proxy,
               credentials_file, auth_token, private_url, force, status, csrf_token, session, request_origin_url,
               request_origin_label)
    except SPyException as e:
        status.update(str(e), Status.FAILURE)
        raise

    user_string = session.user.username
    user_profile = ''
    if session.user.first_name:
        user_profile = session.user.first_name
    if session.user.last_name:
        user_profile += ' ' + session.user.last_name
    if session.user.is_admin:
        user_profile += ' [Admin]'
    if len(user_profile) > 0:
        user_string += ' (%s)' % user_profile.strip()

    message = f'Logged in to <strong>{session.public_url}</strong> successfully as <strong>{user_string}</strong>.\n'

    message += (f'Seeq Server Version: <strong>{spy.server_version}</strong>\n'
                f'Seeq SDK Module Version: <strong>{sdk.__version__}</strong> @ {os.path.dirname(sdk.__file__)}\n'
                f'Seeq SPy Module Version: <strong>{spy.__version__}</strong> @ {os.path.dirname(spy.__file__)}')

    status.update(message, Status.SUCCESS)


def _login(username, password, access_key, url, directory, ignore_ssl_errors, proxy, credentials_file, auth_token,
           private_url, force, status, csrf_token, session: Session, request_origin_url=None,
           request_origin_label=None):
    if access_key and username:
        raise SPyValueError('"username" argument must be omitted when supplying "access_key" argument')

    if access_key and directory != 'Seeq':
        raise SPyValueError('"directory" argument must be omitted when supplying "access_key" argument')

    try:
        if force or not session.client:
            # Clear out any global state before attempting to log in
            _clear_login_state(quiet=True, status=None, session=session)

            if url:
                session.public_url = url
                session.private_url = url
            else:
                session.public_url = Setting.SEEQ_URL.get() if Setting.SEEQ_URL.get() else 'http://localhost:34216'
                session.private_url = Setting.PRIVATE_URL.get() if Setting.PRIVATE_URL.get() else session.public_url

            if private_url:
                # User is overriding the private_url that was "calculated" in logic above
                session.private_url = private_url

            _client_login(auth_token, credentials_file, directory, ignore_ssl_errors, password, proxy, status,
                          session.get_api_url(), username, access_key, csrf_token, request_origin_url,
                          request_origin_label, session)

        system_api = SystemApi(session.client)
        server_status = system_api.get_server_status()  # type: ServerStatusOutputV1
        session.server_version = server_status.version
        validate_seeq_server_version(
            session,
            status,
            # We allow a version mismatch here because in the case of Data Lab, this login call happens when the
            # kernel is initialized, and if an exception is thrown, it is not seen by the user. Then subsequent calls to
            # other functions like spy.search() fail with a "not logged in" error instead of failing with a version
            # mismatch error. That's confusing. So instead, we just warn during login (but succeed) and then fail later
            # when other functions are called.
            allow_version_mismatch=True)

        validate_data_lab_license(session)

        users_api = UsersApi(session.client)
        session.user = users_api.get_me()

        folders_api = FoldersApi(session.client)

        # noinspection PyBroadException
        try:
            session.corporate_folder = folders_api.get_folder(folder_id='corporate')
        except BaseException:
            # This can happen in cases where the user does not have access rights to the Corporate folder
            session.corporate_folder = None

    except BaseException:
        logout(quiet=True, session=session)
        raise


def _client_login(auth_token, credentials_file, directory, ignore_ssl_errors, password, proxy, status, api_client_url,
                  username, access_key, csrf_token, request_origin_url, request_origin_label, session: Session):
    # Annoying warnings are printed to stderr if connections fail
    logging.getLogger("requests").setLevel(logging.FATAL)
    logging.getLogger("urllib3").setLevel(logging.FATAL)
    urllib3.disable_warnings()

    cert_file = Setting.get_seeq_cert_path()
    if cert_file and os.path.exists(cert_file):
        session.client_configuration.set_certificate_path(cert_file)

    key_file = Setting.get_seeq_key_path()
    if key_file and os.path.exists(key_file):
        session.client_configuration.key_file = key_file

    session.client_configuration.verify_ssl = not ignore_ssl_errors

    if proxy == AUTOMATIC_PROXY_DETECTION:
        if api_client_url.startswith('https') and 'HTTPS_PROXY' in os.environ:
            session.client_configuration.proxy = os.environ['HTTPS_PROXY']
        elif 'HTTP_PROXY' in os.environ:
            session.client_configuration.proxy = os.environ['HTTP_PROXY']
    elif proxy is not None:
        session.client_configuration.proxy = proxy

    _client = ApiClient(api_client_url, configuration=session.client_configuration)
    if _datalab.is_datalab_api():
        _client.set_default_header('x-sq-origin', 'Add-on')
    else:
        _client.set_default_header('x-sq-origin', 'Data Lab')

    auth_api = AuthApi(_client)
    directories = dict()
    try:
        auth_providers_output = auth_api.get_auth_providers()  # type: AuthProvidersOutputV1
    except MaxRetryError as e:
        if isinstance(e.reason, SSLError):
            raise SPyRuntimeError(f'SSL certificate error. If you trust your network, you can add '
                                  f'the spy.login(ignore_ssl_errors=True) argument.\n\nMore info:\n{e.reason}')

        raise SPyRuntimeError(
            '"%s" could not be reached. Is the server or network down?\n%s' % (api_client_url, e))

    session.auth_providers = auth_providers_output.auth_providers
    for datasource_output in session.auth_providers:  # type: DatasourceOutputV1
        directories[datasource_output.name] = datasource_output

    if auth_token:
        if username or password or credentials_file:
            raise SPyValueError('username, password and/or credentials_file cannot be provided along with auth_token')

        _client.auth_token = auth_token
        _client.csrf_token = csrf_token
    else:
        auth_input = AuthInputV1()

        if access_key:
            username = access_key

        if credentials_file:
            if username is not None or password is not None or access_key is not None:
                raise SPyValueError('If credentials_file is specified, username, '
                                    'access_key and password must be omitted')

            if not os.path.exists(credentials_file):
                repo_root_dir = system.get_test_with_root_dir()
                if repo_root_dir:
                    agent_key_file = os.path.join(repo_root_dir, 'sq-run-data-dir', 'keys', 'agent.key')
                    if os.path.exists(agent_key_file):
                        # This is a hack to make it easier to run the Documentation notebooks without having to create a
                        # credentials file. It was too easy to forget to delete the credentials file when you created
                        # it, and it would wind up in the distribution.
                        credentials_file = agent_key_file

            if not os.path.exists(credentials_file):
                raise SPyValueError(f'credentials_file "{credentials_file}" not found')

            try:
                with open(credentials_file) as f:
                    lines = f.readlines()
            except Exception as e:
                raise SPyRuntimeError('Could not read credentials_file "%s": %s' % (credentials_file, e))

            if len(lines) < 2:
                raise SPyRuntimeError('credentials_file "%s" must have two lines: username then password')

            username = lines[0].strip()
            password = lines[1].strip()

        if not username or not password:
            if access_key:
                raise SPyValueError('Both access_key and password must be supplied')
            else:
                raise SPyValueError('Both username and password must be supplied')

        auth_input.username = username
        auth_input.password = password

        status.update('Logging in to <strong>%s</strong> as <strong>%s</strong>' % (
            api_client_url, username), Status.RUNNING)

        if not access_key:
            if directory not in directories:
                raise SPyRuntimeError('directory "%s" not recognized. Possible directory(s) for this server: %s' %
                                      (directory, ', '.join(directories.keys())))

            datasource_output = directories[directory]
            auth_input.auth_provider_class = datasource_output.datasource_class
            auth_input.auth_provider_id = datasource_output.datasource_id

        try:
            auth_api.login(body=auth_input)
        except ApiException as e:
            if e.status == 401:
                if access_key:
                    raise SPyRuntimeError(
                        f'Access Key "{access_key}" is not valid. Log in to the Seeq user interface to reset its '
                        'validity. If you are still seeing this error after doing so, make sure the "access_key" '
                        'and "password" arguments are correct and match an Access Key that you have created in '
                        'the Seeq user interface.'
                    )
                else:
                    raise SPyRuntimeError(
                        f'"{auth_input.username}" could not be logged in with supplied credentials, check username and '
                        'password.')
            else:
                raise
        except MaxRetryError as e:
            raise SPyRuntimeError(
                f'"{api_client_url}" could not be reached. Is the server or network down?\n{e}')
        except Exception as e:
            raise SPyRuntimeError(
                f'Could not connect to Seeq\'s API at {api_client_url} with login "{auth_input.username}".\n{e}')

    # Now that we have succeeded, set all the session variables
    session.client = _client
    session.https_verify_ssl = not ignore_ssl_errors
    session.https_key_file = key_file
    session.https_cert_file = cert_file

    # Now that we are logged in, retrieve path and url for data consumption
    if ((_datalab.is_datalab() or _datalab.is_executor())
            and not _datalab.is_datalab_api()
            and request_origin_url is None
            and request_origin_label is None):
        # noinspection PyBroadException
        try:
            if _datalab.is_executor():
                project_name = os.environ.get('SEEQ_PROJECT_NAME', '')
                file_path = os.environ.get('SEEQ_SDL_FILE_PATH', '')
                project_url = _datalab.get_data_lab_project_url(use_private_url=False)
                notebook_url = f"{project_url}/notebooks/{file_path}"
                request_origin_label = f"[Scheduled] {project_name} - {file_path}"
                request_origin_url = quote(urlparse(notebook_url).path)
            else:
                notebook_url = _datalab.get_notebook_url(session)
                request_origin_url = quote(urlparse(notebook_url).path)

                project_name = _datalab.get_data_lab_project_name(session)
                file_path = notebook_url.split('notebooks/', 1)[1]
                request_origin_label = project_name + " - " + file_path
        except BaseException:
            pass

    if request_origin_label is not None:
        if is_datalab_functions_project() and not request_origin_label.startswith("[Data Lab Functions]"):
            request_origin_label = f"[Data Lab Functions] {request_origin_label}"
        _client.set_default_header('x-sq-origin-label', request_origin_label)
    if request_origin_url is not None:
        _client.set_default_header('x-sq-origin-url', request_origin_url)


def logout(quiet=None, status=None, session: Session = None):
    """
    Logs you out of your current session.

    Parameters
    ----------

    quiet : bool, default False
        If True, suppresses progress output. Note that when status is
        provided, the quiet setting of the Status object that is passed
        in takes precedent.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    session : spy.Session, optional
        The login session to use for this call. See spy.login() documentation
        for info on how to use a Session object.
    """
    _common.validate_argument_types([
        (quiet, 'quiet', bool),
        (status, 'status', Status),
        (session, 'session', Session)
    ])

    session = Session.validate(session)
    _clear_login_state(quiet, status, session, call_logout=True)


def _clear_login_state(quiet, status, session: Session, call_logout=False):
    """
    Clear out any global state and optionally logs you out of your current session.

    Parameters
    ----------

    quiet : bool
        If True, suppresses progress output. Note that when status is
        provided, the quiet setting of the Status object that is passed
        in takes precedent.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    session : spy.Session, optional
        The login session to use for this call. See spy.login() documentation
        for info on how to use a Session object.

    call_logout : bool
        If True, auth_api.logout is called -- otherwise just the session state
        is cleared
    """

    status = Status.validate(status, quiet, errors='raise')

    if session.client is None:
        status.update('No action taken because you are not currently logged in.', Status.FAILURE)
    else:
        if call_logout:
            auth_api = AuthApi(session.client)
            auth_api.logout()

        session.client.logout()

    session.clear()

    status.update('Logged out.', Status.SUCCESS)


def find_user(session: Session, query: str, exact_match: bool = False) -> UserOutputV1:
    """
    Finds a user by using Seeq's user/group search function. Queries by ID, then username, then email.
    :param session: The login session (necessary to execute this call)
    :param query: A user/group fragment to use for the search
    :param exact_match: If True, it will look for the exact match of the user
    :return: The identity of the matching user.
    :rtype: UserOutputV1
    """
    users_api = UsersApi(session.client)
    if _common.is_guid(query):
        return users_api.get_user(id=query)

    def find_user_by_property(prop: str) -> UserOutputV1:
        search_kwargs = {
            f'{prop}_search': query,
            'limit': 100
        }
        get_users_output = users_api.get_users(**search_kwargs)
        if exact_match:
            search_results = [u for u in get_users_output.users if getattr(u, prop) == query]
            for offset in range(100, get_users_output.total_results, 100):
                search_kwargs['offset'] = offset
                search_results.extend(u for u in users_api.get_users(**search_kwargs).users
                                      if getattr(u, prop) == query)
        else:
            search_results = get_users_output.users
        search_results = [user for user in search_results if user.username != 'agent_api_key']
        if len(search_results) == 0:
            raise SPyRuntimeError('User "%s" not found' % query)
        if len(search_results) > 1:
            raise SPyRuntimeError('Multiple users found that match "%s":\n%s' % (
                query, '\n'.join([('%s (%s)' % (getattr(u, prop), u.id)) for u in search_results])))

        return search_results[0]

    try:
        return find_user_by_property('username')
    except SPyRuntimeError as e:
        try:
            return find_user_by_property('email')
        except SPyRuntimeError:
            raise e


def find_group(session: Session, query, exact_match=False):
    """
    Finds a group by using Seeq's user/group autocomplete functionality. Must result in exactly one match or a
    RuntimeError is raised.
    :param session: The login session (necessary to execute this call)
    :param query: A user/group fragment to use for the search
    :param exact_match: If True, it will look for the exact match of the user
    :return: The identity of the matching group.
    :rtype: UserGroupOutputV1
    """
    users_api = UsersApi(session.client)
    user_groups_api = UserGroupsApi(session.client)

    if _common.is_guid(query):
        group_id = query
    else:
        identity_preview_list = users_api.autocomplete_users_and_groups(query=query).items
        if len(identity_preview_list) == 0:
            raise SPyRuntimeError('Group "%s" not found' % query)
        if len(identity_preview_list) > 1:
            if exact_match:
                identity_preview_list = [x for x in identity_preview_list if x.name == query]
                if len(identity_preview_list) == 0:
                    raise SPyRuntimeError('Exact match for group "%s" not found' % query)
            else:
                raise SPyRuntimeError('Multiple groups found that match "%s":\n%s' % (
                    query, '\n'.join([('%s (%s)' % (g.name, g.id)) for g in identity_preview_list])))

        if exact_match and identity_preview_list[0].name != query:
            raise SPyRuntimeError('Exact match for user "%s" not found' % query)
        group_id = identity_preview_list[0].id

    return user_groups_api.get_user_group(user_group_id=group_id)


def get_user_timezone(session: Session, default_tz='UTC'):
    """
    Returns the preferred timezone of the user currently logged in, or default_tz if there is no user currently
    logged in.

    :param: session: The login session (necessary to fulfill this call).
    :param: default_tz: The default timezone to return if no user is logged in.
    :return: The user's preferred timezone, in IANA Time Zone Database format (e.g., 'America/New York')
    :rtype: str
    """
    _common.validate_timezone_arg(default_tz)
    try:
        workbench_dict = json.loads(session.user.workbench)
        return workbench_dict['state']['stores']['sqWorkbenchStore']['userTimeZone']
    except (AttributeError, KeyError, TypeError):
        # This can happen if the user has never logged in interactively (e.g., agent_api_key)
        return default_tz


def get_sdk_module_version_tuple():
    match = re.match(r'^(\d+)\.(\d+)\.(\d+).*', sdk.__version__ if hasattr(sdk, '__version__') else spy.__version__)
    seeq_module_major = int(match.group(1))
    seeq_module_minor = int(match.group(2))
    seeq_module_patch = int(match.group(3))
    return seeq_module_major, seeq_module_minor, seeq_module_patch


def get_spy_module_version_tuple():
    match = re.match(r'^(\d+)\.(\d+)$', spy.__version__)
    if match is None:
        # Old versioning scheme when spy was part of main seeq module
        match = re.match(r'^.*\.(\d+)\.(\d+)$', spy.__version__)

    spy_module_major = int(match.group(1))
    spy_module_minor = int(match.group(2))
    return spy_module_major, spy_module_minor


def get_server_version_tuple(session: Session):
    match = re.match(r'^R?(?:\d+\.)?(\d+)\.(\d+)\.(\d+)(-v\w+)?(-[-\w]+)?', session.server_version)
    seeq_server_major = int(match.group(1))
    seeq_server_minor = int(match.group(2))
    seeq_server_patch = int(match.group(3))
    return seeq_server_major, seeq_server_minor, seeq_server_patch


SEEQ_SERVER_VERSION_WHERE_SPY_IS_IN_ITS_OWN_PACKAGE = 60


def validate_seeq_server_version(session: Session, status: Status, allow_version_mismatch=False):
    sdk_module_major, sdk_module_minor, _ = get_sdk_module_version_tuple()
    seeq_server_major, seeq_server_minor, seeq_server_patch = get_server_version_tuple(session)

    # The old versioning scheme is like 0.49.3 whereas the new scheme is like 50.1.8
    # See https://seeq.atlassian.net/wiki/spaces/SQ/pages/947225963/Seeq+Versioning+Simplification
    using_old_server_versioning_scheme = (seeq_server_major == 0)

    message = None

    if using_old_server_versioning_scheme:
        if sdk_module_major != seeq_server_major or \
                sdk_module_minor != seeq_server_minor:
            message = (f'The major/minor version of the seeq module ({sdk_module_major}.{sdk_module_minor}) '
                       f'does not match the major/minor version of the Seeq Server you are connected to '
                       f'({seeq_server_major}.{seeq_server_minor}) and is incompatible.')
    else:
        if sdk_module_major != seeq_server_major:
            message = (f'The major version of the seeq module ({sdk_module_major}) '
                       f'does not match the major version of the Seeq Server you are connected to '
                       f'({seeq_server_major}) and is incompatible.')

    if message is not None:
        compatible_module_folder = find_compatible_module(session)
        if not compatible_module_folder:
            message += (f'\n\nIt is recommended that you run spy.upgrade() or issue the following PIP command to '
                        f'install a compatible version of the seeq module:\n')
            if using_old_server_versioning_scheme:
                message += generate_seeq_module_pip_upgrade(
                    f'{seeq_server_major}.{seeq_server_minor}.{seeq_server_patch}')
            else:
                message += generate_seeq_module_pip_upgrade(f'{seeq_server_major}.{seeq_server_minor}')
        else:
            message += (f'\n\nA compatible module was found here: {compatible_module_folder}\n'
                        f'Consider uninstalling your project-specific seeq module by issuing the following PIP '
                        f'command:\n'
                        f'pip uninstall -y seeq')

        if allow_version_mismatch or session.options.allow_version_mismatch:
            status.warn(message)
        else:
            raise SPyRuntimeError(message)

    return seeq_server_major, seeq_server_minor, seeq_server_patch


def generate_seeq_module_pip_upgrade(version, exact_match_version=False):
    matcher = '==' if exact_match_version else '~='
    return f'pip install -U seeq{matcher}{version}'


def find_compatible_module(session: Session):
    """
    Uses pkg_resources tools to look for a seeq module that is compatible with the version of Seeq Server we're
    connected to. This function is useful in Seeq Data Lab scenarios where the user has installed a "private" version of
    the seeq module (presumably to get a bugfix for SPy) but Seeq Server and Seeq Data Lab have been upgraded in the
    meantime and the user's best course of action is to remove the private version and resume using the "built-in"
    version, which will update with Seeq Data Lab as it is upgraded.
    :return: Path to a compatible module, None if a compatible module is not found.
    """
    seeq_module_major, seeq_module_minor, _ = get_sdk_module_version_tuple()
    seeq_server_major, seeq_server_minor, seeq_server_patch = get_server_version_tuple(session)

    pkg_env = pkg_resources.Environment()
    seeq_modules = pkg_env['seeq']
    for seeq_module in seeq_modules:  # type: pkg_resources.Distribution
        if seeq_server_major >= 50 and seeq_module.version.startswith(f'{seeq_server_major}.'):
            return seeq_module.location
        elif seeq_server_major < 50 and seeq_module.version.startswith(f'{seeq_server_major}.{seeq_server_minor}.'):
            return seeq_module.location

    return None


def validate_data_lab_license(session: Session):
    system_api = SystemApi(session.client)
    license_status_output = system_api.get_license()  # type: LicenseStatusOutputV1
    for additional_feature in license_status_output.additional_features:  # type: LicensedFeatureStatusOutputV1
        if additional_feature.name == 'Data_Lab':
            if additional_feature.validity == 'Valid':
                return

            raise SPyRuntimeError(f'Seeq Data Lab license is "{additional_feature.validity}", could not log in. '
                                  f'Contact your administrator or speak with Seeq Support at support@seeq.com.')

    raise SPyRuntimeError('Seeq Data Lab is not licensed for this server, could not log in. Contact your administrator '
                          'or speak with Seeq Support at support@seeq.com.')


def validate_login(session: Session, status: Status):
    if session.client is None:
        raise SPyRuntimeError('Not logged in. Execute spy.login() before calling this function.')

    validate_seeq_server_version(session, status)


def parse_content_datetime_with_timezone(session: Session, dt: object, timestamp_units: str = 'ms',
                                         timezone: Optional[object] = None) -> pd.Timestamp:
    if timezone is None:
        timezone = get_user_timezone(session)

    if isinstance(dt, pd.Timestamp):
        if not pd.isna(dt) and dt.tz is None:
            dt = dt.tz_localize(timezone)
        return dt

    if isinstance(dt, (float, int)):
        # Assume it's in milliseconds because it came from the front-end
        return pd.Timestamp(dt, unit=timestamp_units, tz='UTC')

    if not isinstance(dt, str):
        raise SPyValueError(f'Date/time object {dt} of type "{type(dt)}" not recognized')

    match = re.fullmatch(r'^([^\[\]]+)(\[(.+)])?$', dt)
    if not match or not match.group(3):
        # noinspection PyTypeChecker
        return pd.Timestamp(dt, tz=timezone)

    datetime_part = match.group(1)
    tz_part = match.group(3)
    return pd.Timestamp(datetime_part, tz=tz_part)


def get_fallback_timezone(session: Session):
    """
    Gets the timezone to interpret a datetime as if none is specified. This is the
    spy.options.default_timezone timezone if it exists, else the user's preferred timezone.
    :param session: The login session (necessary to fulfill this call).
    :return: timezone
    """
    return session.options.default_timezone if session.options.default_timezone else get_user_timezone(session)


def parse_input_datetime(session: Session,
                         input_datetime: Union[pd.Timestamp,
                                               datetime.date,
                                               str,
                                               int,
                                               float],
                         timezone: Optional[Union[str,
                                                  pytz.BaseTzInfo,
                                                  tz.tzoffset]] = None) -> pd.Timestamp:
    """
    Takes a datetime and optionally a timezone, and returns a pd.Timestamp that is
    timezone-aware, by localizing naive datetimes to specified timezone if provided, else
    to the fallback timezone.
    :param session: The login session (necessary to fulfill this call).
    :param input_datetime: The datetime to be parsed
    :param timezone: The timezone to interpret a naive datetime as. If none, the fallback
    timezone will be used.
    :return: pd.Timestamp
    """
    if pd.isna(input_datetime) or pd.isnull(input_datetime):
        return input_datetime

    if timezone is None:
        timezone = get_fallback_timezone(session)

    if isinstance(input_datetime, int) or isinstance(input_datetime, float):
        # Unix epoch is definitionally UTC, and timestamp will convert correctly if a
        # timezone is specified, but if no timezone is specified will become a naive
        # datetime, which ignores that it's definitionally UTC
        # Units are assumed to be 'ms'
        input_datetime = pd.Timestamp(input_datetime, unit='ms', tz=timezone)

    warnings.filterwarnings("error", category=parser.UnknownTimezoneWarning)
    if not isinstance(input_datetime, pd.Timestamp):
        try:
            input_datetime = pd.Timestamp(input_datetime)
        except (parser.UnknownTimezoneWarning, ValueError, pd.errors.OutOfBoundsDatetime) as e:
            raise SPyValueError(f'Could not parse input datetime "{input_datetime}" for reason: {str(e)}')

    if input_datetime.tz is None:
        input_datetime = input_datetime.tz_localize(timezone)

    return input_datetime


def validate_start_and_end(session: Session,
                           start: Union[pd.Timestamp, datetime.date, str, int, float],
                           end: Union[pd.Timestamp, datetime.date, str, int, float]):
    """
    Takes a pair of start and end times, either of which could be None, and uses some default logic
    to produce a "cleaned up" start and end. For example, if start is after end, then end is reset to
    one hour after start.
    :param session: The login session (necessary to fulfill this call).
    :param start: The start value, or None if you want a default to be calculated.
    :param end: The end value, or None if you want a default to be calculated.
    :return: The calculated (start, end) tuple after having run through the default logic.
    :rtype: tuple
    """

    pd_start = parse_input_datetime(session, start)
    pd_end = parse_input_datetime(session, end)

    if pd.isnull(pd_end):
        utc_now = pd.Timestamp.utcnow()
        if not pd.isnull(pd_start):
            # noinspection PyTypeChecker
            pd_end = utc_now.tz_convert(pd_start.tz)
            if pd_start > pd_end:
                # noinspection PyTypeChecker
                pd_end = pd_start + pd.Timedelta(hours=1)
        else:
            # noinspection PyTypeChecker
            pd_end = utc_now.tz_convert(get_fallback_timezone(session))

    if pd.isnull(pd_start):
        pd_start = pd_end - pd.Timedelta(hours=1)

    return pd_start, pd_end


# The list of units that come back from system_api.get_supported_units() is a curated set of compound units that are
# meant to be human-friendly in Formula tool help. But it's the only thing available in the API to figure out what
# base units are supported, so we have to split the compound unit string into its components. I.e., S/cm³ gets split
# into S and cm so that we can add those two "base" units to the set we use to determine validity.
UNITS_SPLIT_REGEX = r'[/*²³·]'


def is_valid_unit(session: Session, unit):
    """
    Returns True if the supplied unit will be recognized by the Seeq calculation engine. This can be an important
    function to use if you are attempting to supply a "Value Unit Of Measure" property on a Signal or a "Unit Of
    Measure" property on a Scalar.

    :param: session: The login session (necessary to execute this call)
    :param: unit: The unit of measure for which to assess validity
    :return: True if unit is valid, False if not
    """
    if not session.supported_units:
        system_api = SystemApi(session.client)
        support_units_output = system_api.get_supported_units()  # type: SupportedUnitsOutputV1

        session.supported_units = set()
        for supported_unit_family in support_units_output.units.values():
            for supported_unit in supported_unit_family:
                unit_parts = re.split(UNITS_SPLIT_REGEX, supported_unit)
                session.supported_units.update([u for u in unit_parts if len(u) > 0])

    unit_parts = re.split(UNITS_SPLIT_REGEX, unit)
    for unit_part in [u for u in unit_parts if len(u) > 0]:
        if unit_part not in session.supported_units:
            return False

    return True


def pull_image(session: Session, url):
    return requests.get(url, headers={
        "Accept": "application/vnd.seeq.v1+json",
        "x-sq-auth": session.client.auth_token
    }, verify=session.https_verify_ssl).content


def get_api(session: Session, api_class):
    validate_login(session, Status(quiet=True))
    return api_class(session.client)


def __getattr__(name):
    if name == 'client':
        # Before ~ March 2020, users commonly accessed spy._login.client when they wanted to leverage the SPy login
        # in their use of SDK functions.
        util.deprecation_warning("Use of spy._login.client deprecated, use spy.client instead")
        return spy.client
    else:
        # fallback to default module attribute access
        raise AttributeError
