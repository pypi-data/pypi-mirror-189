from __future__ import annotations

import json
import os
import re
from typing import Optional, TYPE_CHECKING

import jupyter_client
import psutil
from IPython import get_ipython
from nbformat import NotebookNode

from seeq.sdk import *
from seeq.spy._config import Setting

if TYPE_CHECKING:
    from seeq.spy._session import Session


def is_ipython():
    # noinspection PyBroadException
    try:
        return get_ipython() is not None
    except BaseException:
        return False


def is_ipython_interactive():
    return get_ipython().__class__.__name__ == 'ZMQInteractiveShell'


def is_jupyter():
    # noinspection PyBroadException
    try:
        return is_ipython_interactive() or is_rkernel()
    except BaseException:
        return False


def is_rkernel():
    return get_kernel_language() == 'R'


def get_kernel_language():
    return psutil.Process(os.getpid()).name()


def is_datalab():
    return os.environ.get('SEEQ_SDL_CONTAINER_IS_DATALAB') == 'true'


def is_datalab_api():
    return os.environ.get('SEEQ_DATALAB_API') == 'true'


def is_executor():
    return os.environ.get('SEEQ_SDL_CONTAINER_IS_EXECUTOR') == 'true'


def get_label_from_executor():
    return os.environ.get('SEEQ_SDL_LABEL') or ''


def get_data_lab_project_name(session: Session, project_id=None) -> str:
    projects_api = ProjectsApi(session.client)
    if project_id is None:
        project_id = get_data_lab_project_id()
    return projects_api.get_project(id=project_id).name


def get_notebook_url(session: Session, use_private_url=True):
    project_url = get_data_lab_project_url(use_private_url)
    notebook = f"/notebooks/{get_notebook_path(session)}"

    return project_url + notebook


def get_notebook_path(session: Session):
    if is_datalab_api():
        raise RuntimeError('Cannot determine notebook path within Datalab API')

    kernel_id = os.getenv('KERNEL_ID', re.search('kernel-(.*).json', jupyter_client.find_connection_file()).group(1))
    # Always make the request call using the private url
    response = session.requests.get(f'{get_data_lab_project_url(use_private_url=True)}/api/sessions')
    for nn in json.loads(response.text):
        if nn['kernel']['id'] == kernel_id:
            return nn['notebook']['path']

    # We may be in Add On Mode where voila has its own kernel manager and api/sessions won't find the kernel
    # In that case, check the SCRIPT_NAME env variable which voila sets to '/data-lab/<projectId>/addon/<notebook_path>
    re_groups = re.search(f"/data-lab/{get_data_lab_project_id()}/(addon|apps)/(.*)", os.getenv('SCRIPT_NAME', ''))
    if re_groups is not None and len(re_groups.groups()) > 1:
        return re_groups.group(2)


def get_execution_notebook(lang: str) -> str:
    path = "/seeq/scheduling"
    if lang == "python":
        file = os.path.join(path, "ExecutionNotebook.ipynb")
    elif lang == "R":
        file = os.path.join(path, "ExecutionNotebookR.ipynb")
    else:
        raise FileNotFoundError(f"Could not find an execution notebook for language {lang}")

    return file


def get_notebook_language(nb_notebook: NotebookNode) -> Optional[str]:
    try:
        return nb_notebook['metadata']['kernelspec']['language']
    except KeyError:
        return None


def get_data_lab_orchestrator_url(use_private_url=True):
    return f'{Setting.get_private_url()}/data-lab' if use_private_url else f'{Setting.get_seeq_url()}/data-lab'


def get_data_lab_project_id():
    """
    Get Seeq ID assigned to this Data Lab Project

    Returns
    -------
    {str, None}
        The Seeq ID as a string, or None if no ID assigned
    """
    return Setting.SEEQ_PROJECT_UUID.get()


def get_data_lab_project_url(use_private_url=True):
    """
    Get Data Lab Project URL in form of ``{Seeq_Server_URL}/data-lab/{Data Lab Project ID}``

    Parameters
    ----------
    use_private_url : bool, default True
        If False, use the publicly accessible Seeq url for the Seeq_Server_URL

    Returns
    -------
    {str}
        The Data Lab Project URL as a string
    """
    return f'{get_data_lab_orchestrator_url(use_private_url)}/{get_data_lab_project_id()}'
