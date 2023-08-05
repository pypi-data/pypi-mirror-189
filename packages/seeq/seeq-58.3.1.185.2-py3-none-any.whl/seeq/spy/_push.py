from __future__ import annotations

import datetime
import functools
import re
import types
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import pandas as pd

from seeq import spy
from seeq.base.seeq_names import SeeqNames
from seeq.sdk import *
from seeq.spy import _common
from seeq.spy import _login
from seeq.spy import _metadata
from seeq.spy._common import EMPTY_GUID
from seeq.spy._errors import *
from seeq.spy._redaction import safely
from seeq.spy._session import Session
from seeq.spy._status import Status
from seeq.spy.workbooks import _folder, _workbook

# This constant is set to be slightly below numArchivedItemsPerCommit in DatasourceQueriesV1.java
DATASOURCE_CLEANUP_ITEM_COUNT_THRESHOLD = 19_000


def push(data=None, *, metadata=None, replace=None, workbook=_common.DEFAULT_WORKBOOK_PATH,
         worksheet=_common.DEFAULT_WORKSHEET_NAME, datasource=None, archive=False, type_mismatches='raise',
         metadata_state_file: Optional[str] = None, errors=None, quiet=None, status=None,
         session: Optional[Session] = None):
    """
    Imports metadata and/or data into Seeq Server, possibly scoped to a
    workbook and/or datasource.

    The 'data' and 'metadata' arguments work together. Signal and condition
    data cannot be mixed together in a single call to spy.push().

    Successive calls to 'push()' with the same 'metadata' but different 'data'
    will update the items (rather than overwrite them); however, pushing a new
    sample with the same timestamp as a previous one will overwrite the old
    one.

    Metadata can be pushed without accompanying data. This is common after
    having invoked the spy.assets.build() function. In such a case, the
    'metadata' DataFrame can contain signals, conditions, scalars, metrics,
    and assets.

    Parameters
    ----------
    data : pandas.DataFrame, optional
        A DataFrame that contains the signal or condition data to be pushed.
        If 'metadata' is also supplied, it will have specific formatting
        requirements depending on the type of data being pushed.

        For signals, 'data' must have a pandas.Timestamp-based index with a
        column for each signal. To push to an existing signal, set the column
        name to the Seeq ID of the item to be pushed. An exception will be
        raised if the item does not exist.

        For conditions, 'data' must have an integer index and two
        pandas.Timestamp columns named 'Capsule Start' and 'Capsule End'.

    metadata : pandas.DataFrame, optional
        A DataFrame that contains the metadata for signals, conditions,
        scalars, metrics, or assets. If 'metadata' is supplied, in conjunction
        with a 'data' DataFrame, it has specific requirements depending on the
        kind of data supplied.

        For signals, the 'metadata' index (i.e., each row's index value) must
        match the column names of the 'data' DataFrame. For example, if you
        would like to push data where the name of each column is the Name of
        the item, then you might do set_index('Name', inplace=True, drop=False)
        on your metadata DataFrame to make the index match the data DataFrame's
        column names.

        For conditions and metrics, the 'metadata' DataFrame must have only
        one row with metadata.

        Metadata for each object type includes:

        Type Key:   Si = Signal, Sc = Scalar, C = Condition,
                    A = Asset, M = Metric

        ===================== ==================================== ============
        Metadata Term         Definition                           Types
        ===================== ==================================== ============
        Name                  Name of the signal                   Si,Sc,C,A,M
        Description           Description of the signal            Si,Sc,C,A
        Maximum Interpolation Maximum interpolation between        Si
                              samples
        Value Unit Of Measure Unit of measure for the signal       Si
        Formula               Formula for a calculated item        Si,Sc,C
        Formula Parameters    Parameters for a formula             Si,Sc,C
        Interpolation Method  Interpolation method between points  Si
                              Options are Linear, Step, PILinear
        Maximum Duration      Maximum expected duration for a      C
                              capsule
        Number Format         Formatting string ECMA-376           Si,Sc,M
        Path                  Asset tree path where the item's     Si,Sc,C,A
                              parent asset resides
        Measured Item         The ID of the signal or condition    M
        Statistic             Aggregate formula function to        M
                              compute on the measured item
        Duration              Duration to calculate a moving       M
                              aggregation for a continuous process
        Period                Period to sample for a               M
                              continuous process
        Thresholds            List of priority thresholds mapped
                              to a scalar formula/value or an ID   M
                              of a signal, condition or scalar
        Bounding Condition    The ID of a condition to aggregate   M
                              for a batch process
        Bounding Condition    Duration for aggregation for a       M
        Maximum Duration      bounding condition without a maximum
                              duration
        Asset                 Parent asset name. Parent asset      Si,Sc,C,A,M
                              must be in the tree at the
                              specified path, or listed in
                              'metadata' for creation.
        Capsule Property      A dictionary of capsule property     C
        Units                 names with their associated units
                              of measure
        Push Directives       A semi-colon-delimited list of
                              directives for the row that can
                              include:
                              'CreateOnly' - do not overwrite
                              existing item
                              'UpdateOnly' - only overwrite, do
                              not create
        ===================== ==================================== ============

    replace : dict, default None
        A dict with the keys 'Start' and 'End'.
        If provided, the capsules with the start date in the provided time
        period will be replaced. The condition whose capsules are going to be
        replaced must be specified in metadata. Start of the time period is
        inclusive and the end of the time period is exclusive. If replace is
        provided but data is not specified, all capsules within the provided
        time period will be removed.

    workbook : {str, None, AnalysisTemplate}, default 'Data Lab >> Data Lab Analysis'
        The path to a workbook (in the form of 'Folder >> Path >> Workbook
        Name') or an ID that all pushed items will be 'scoped to'. Items scoped
        to a certain workbook will not be visible/searchable using the data
        panel in other workbooks. If None, items can also be 'globally scoped',
        meaning that they will be visible/searchable in all workbooks. Global
        scoping should be used judiciously to prevent search results becoming
        cluttered in all workbooks. The ID for a workbook is visible in the URL
        of Seeq Workbench, directly after the "workbook/" part. You can also
        push to the Corporate folder by using the following pattern:
        f'{spy.workbooks.CORPORATE} >> MySubfolder >> MyWorkbook'

        You can also supply an AnalysisTemplate object (or a list of them) so
        that you push a custom workbook with specific worksheets and associated
        visualizations. Check out the "Workbook Templates.ipynb" tutorial
        notebook for more information.

    worksheet : {str, None, AnalysisWorksheetTemplate}, default 'From Data Lab'
        The name of a worksheet within the workbook to create/update that will
        render the data that has been pushed so that you can see it in Seeq
        easily. If None, no worksheet will be added or changed. This argument
        is ignored if an AnalysisTemplate object is supplied as the workbook
        argument.

        You can also supply an AnalysisWorksheetTemplate object so that you
        push a custom worksheet with associated visualizations. Check out the
        "Workbook Templates.ipynb" tutorial notebook for more information.

    datasource : str, optional
        The name of the datasource within which to contain all the
        pushed items. By default, all pushed items will be contained in a "Seeq
        Data Lab" datasource. Do not create new datasources unless you really
        want to and you have permission from your administrator.

    archive : bool, default False
        If True, and all metadata describes items from a common asset tree,
        then items in the tree not updated by this push call are archived.

    type_mismatches : {'raise', 'drop', 'invalid'}, default 'raise'
        If 'raise' (default), any mismatches between the type of the data and
        its metadata will cause an exception. For example, if string data is
        found in a numeric time series, an error will be raised. If 'drop' is
        specified, such data will be ignored while pushing. If 'invalid' is
        specified, such data will be replaced with an INVALID sample, which
        will interrupt interpolation in calculations and displays.

    metadata_state_file : str, optional
        The file name (with full path, if desired) to a "metadata state file"
        to use for "incremental" pushing, which can dramatically speed up
        pushing of a large metadata DataFrame. If supplied, the metadata push
        operation uses the state file to determine what changed since the
        last time the metadata was pushed and it will only act on those
        changes.

    errors : {'raise', 'catalog'}, default 'raise'
        If 'raise', any errors encountered will cause an exception. If
        'catalog', errors will be added to a 'Result' column in the status.df
        DataFrame.

    quiet : bool, default False
        If True, suppresses progress output. Note that when status is
        provided, the quiet setting of the Status object that is passed
        in takes precedent.

    status : spy.Status, optional
        If specified, the supplied Status object will be updated as the command
        progresses. It gets filled in with the same information you would see
        in Jupyter in the blue/green/red table below your code while the
        command is executed. The table itself is accessible as a DataFrame via
        the status.df property.

    session : spy.Session, optional
        If supplied, the Session object (and its Options) will be used to
        store the login session state. This is useful to log in to different
        Seeq servers at the same time or with different credentials.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the metadata for the items pushed, along with any
        errors and statistics about the operation.

        Additionally, the following properties are stored on the "spy"
        attribute of the output DataFrame:

        =================== ===================================================
        Property            Description
        =================== ===================================================
        func                A str value of 'spy.push'
        kwargs              A dict with the values of the input parameters
                            passed to spy.push to get the output DataFrame
        workbook_id         If pushed to a specific workbook, the ID of that
                            workbook.
        worksheet_id        If pushed to a specific worksheet, the ID of that
                            worksheet.
        workbook_url        If pushed to a specific workbook, the URL of that
                            workbook and the curated worksheet that this
                            command created.
        status              A spy.Status object with the status of the
                            spy.push call
        =================== ===================================================
    """
    input_args = _common.validate_argument_types([
        (data, 'data', pd.DataFrame),
        (metadata, 'metadata', pd.DataFrame),
        (replace, 'replace', dict),
        (workbook, 'workbook', (str, spy.workbooks.AnalysisTemplate, list, spy.workbooks.WorkbookList)),
        (worksheet, 'worksheet', (str, spy.workbooks.AnalysisWorksheetTemplate)),
        (datasource, 'datasource', str),
        (archive, 'archive', bool),
        (type_mismatches, 'type_mismatches', str),
        (metadata_state_file, 'metadata_state_file', str),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', Status),
        (session, 'session', Session)
    ])

    status = Status.validate(status, quiet, errors)
    session = Session.validate(session)
    _login.validate_login(session, status)

    if type_mismatches not in ['drop', 'raise', 'invalid']:
        raise SPyValueError("'type_mismatches' must be either 'drop', 'raise' or 'invalid'")

    if replace is not None:
        if replace.keys() != {'Start', 'End'}:  # strict comparison, allowing only these two keys
            raise SPyValueError(f"Parameter 'replace'' must have 'Start' and 'End' keys. Given keys: "
                                f"{replace.keys()}")

    tree_root = None
    if archive:
        if metadata is None or metadata.empty:
            raise SPyValueError("Asset tree metadata must be provided when parameter 'archive' is True.")
        tree_root = get_common_root(metadata)
        if tree_root is None:
            raise SPyValueError("Items in metadata must all belong to the same asset tree when parameter "
                                "'archive' is True.")

    item_type = 'Signal'
    if data is not None:
        if 'Capsule Start' in data.columns or 'Capsule End' in data.columns:
            item_type = 'Condition'
    elif metadata is not None:
        if 'Type' in metadata.columns and not metadata.empty and metadata.iloc[0]['Type'] == 'Condition':
            item_type = 'Condition'

    datasource_output = _metadata.create_datasource(session, datasource)

    workbook_context: Optional[WorkbookContext] = \
        _determine_workbook_context(session, status, workbook, worksheet, datasource)

    workbook_context.determine_folder_id()

    push_result_df = pd.DataFrame()
    sync_token = datetime.datetime.utcnow().isoformat()
    capsule_property_metadata = None
    push_metadata_status = status.create_inner('Push Metadata')

    if metadata is not None and not metadata.empty:
        if item_type == "Condition" and 'Capsule Property Units' in metadata:
            if data is None:
                capsule_property_metadata = metadata.at[0, 'Capsule Property Units']
            else:
                capsule_property_metadata = {k.lower(): v for k, v in metadata.pop('Capsule Property Units')[0].items()}

        def _metadata_push_first_pass_filter(_row: pd.Series):
            return _row['Type'] != 'Workbook' and not (_row['Type'] == 'Display' and _common.present(_row, 'Object'))

        push_result_df = _metadata.push(session, metadata, workbook_context, datasource_output, sync_token,
                                        _metadata_push_first_pass_filter, push_metadata_status, cleanse_df_first=True,
                                        state_file=metadata_state_file, planning_to_archive=archive)

    sample_stats = types.SimpleNamespace(earliest_sample_in_ms=None, latest_sample_in_ms=None)

    def _on_success(_row_index, _job_result):
        _earliest_sample_in_ms, _latest_sample_in_ms, _item_id, _signal_metadata = _job_result
        if None not in [sample_stats.earliest_sample_in_ms, _earliest_sample_in_ms]:
            sample_stats.earliest_sample_in_ms = min(_earliest_sample_in_ms, sample_stats.earliest_sample_in_ms)
        elif sample_stats.earliest_sample_in_ms is None and _earliest_sample_in_ms is not None:
            sample_stats.earliest_sample_in_ms = _earliest_sample_in_ms

        if None not in [sample_stats.latest_sample_in_ms, _latest_sample_in_ms]:
            sample_stats.latest_sample_in_ms = max(_latest_sample_in_ms, sample_stats.latest_sample_in_ms)
        elif sample_stats.latest_sample_in_ms is None and _latest_sample_in_ms is not None:
            sample_stats.latest_sample_in_ms = _latest_sample_in_ms

        if _item_id is None:
            # This can happen if the column has only nan values. In that case, we don't know whether
            # it's a string or numeric signal and we couldn't create the signal item.
            # Check to see if it was created by push_metadata.
            if 'ID' in _signal_metadata:
                _item_id = _signal_metadata['ID']

            # CRAB-19586: Cannot convert string to float error
            # Since the ID column has only nan values, ensure ID column is dtype object
            push_result_df['ID'] = push_result_df['ID'].astype(object)

        push_result_df.at[_row_index, 'ID'] = _item_id
        push_result_df.at[_row_index, 'Type'] = \
            'StoredSignal' if item_type == 'Signal' else 'StoredCondition'

    if data is not None or replace is not None:
        def _put_item_defaults(d):
            if not _common.present(d, 'Datasource Class'):
                d['Datasource Class'] = datasource_output.datasource_class

            if not _common.present(d, 'Datasource ID'):
                d['Datasource ID'] = datasource_output.datasource_id

            if not _common.present(d, 'Type'):
                d['Type'] = item_type

            if not _common.present(d, 'Data ID'):
                d['Data ID'] = _metadata.get_scoped_data_id(d, workbook_context.workbook_id)

            if not _common.present(d, 'Scoped To') and workbook_context.workbook_id is not None:
                d['Scoped To'] = workbook_context.workbook_id

        status_columns = list()
        if 'ID' in push_result_df:
            status_columns.append('ID')
        if 'Path' in push_result_df:
            status_columns.append('Path')
        if 'Asset' in push_result_df:
            status_columns.append('Asset')
        if 'Name' in push_result_df:
            status_columns.append('Name')

        status.df = push_result_df[status_columns].copy()
        status.df['Count'] = 0
        status.df['Pages'] = 0
        status.df['Time'] = 0
        status.df['Result'] = 'Pushing'
        status_columns.extend(['Count', 'Pages', 'Time', 'Result'])

        push_result_df['Push Count'] = np.int64(0)
        push_result_df['Push Time'] = 0
        push_result_df['Push Result'] = ''

        status.update(
            f'Pushing data to datasource <strong>{datasource_output.name} ['
            f'{datasource_output.datasource_id}]</strong> scoped to workbook ID '
            f'<strong>{workbook_context.workbook_id}</strong>',
            Status.RUNNING)

        if data is not None and item_type == 'Signal':
            for column in data:
                try:
                    status_index = column

                    # For performance reasons, this variable will be supplied to _push_signal() if we had to
                    # retrieve the signal as part of this function
                    signal_output: Optional[SignalOutputV1] = None

                    if status_index in push_result_df.index:
                        # push_result_df will be filled in by _metadata.push() if a metadata DataFrame was
                        # supplied, so grab the metadata out of there for the signal
                        signal_metadata = push_result_df.loc[status_index].to_dict()

                    elif _common.is_guid(status_index):
                        # If an ID is supplied as the column name, then we are pushing to an existing signal and
                        # we need to query that signal for a few pieces of metadata.
                        signals_api = SignalsApi(session.client)
                        signal_output: SignalOutputV1 = signals_api.get_signal(id=status_index)
                        signal_metadata = {
                            # This is the metadata needed to process the samples appropriately in _push_signal()
                            'Name': signal_output.name,
                            'Type': signal_output.type,
                            'Value Unit Of Measure': signal_output.value_unit_of_measure
                        }

                    else:
                        # Metadata has not been supplied and the column name is not an ID, so just create a
                        # "blank" row in the status DataFrame.
                        ad_hoc_status_df = pd.DataFrame({'Count': 0, 'Pages': 0, 'Time': 0, 'Result': 'Pushing'},
                                                        index=[status_index])
                        status.df = status.df.append(ad_hoc_status_df, sort=True)
                        status.update()
                        signal_metadata = dict()

                    if not _common.present(signal_metadata, 'Name'):
                        if '>>' in column:
                            raise SPyRuntimeError(
                                'Paths in column name not currently supported. Supply a metadata argument if you '
                                'would like to put signal(s) directly in an asset tree.')

                        signal_metadata['Name'] = column

                    if not signal_output:
                        # Plant the "default" metadata so that the item will be placed in the specified
                        # datasource and its Data ID will be managed by SPy
                        _put_item_defaults(signal_metadata)

                    push_result_df.at[status_index, 'Name'] = signal_metadata['Name']

                    status.add_job(status_index,
                                   (_push_signal, session, column, signal_metadata, replace, data, signal_output,
                                    type_mismatches, status_index, status),
                                   _on_success)

                except BaseException as e:
                    _common.raise_or_catalog(status=status, df=push_result_df, index=column,
                                             column='Push Result', e=e)

        elif data is not None and item_type == 'Condition':
            try:
                if metadata is None or len(metadata) != 1:
                    raise SPyRuntimeError('Condition requires "metadata" input of DataFrame with single row')

                condition_metadata = metadata.iloc[0].to_dict()

                if 'Name' not in condition_metadata or 'Maximum Duration' not in condition_metadata:
                    raise SPyRuntimeError('Condition metadata requires "Name" and "Maximum Duration" columns')

                if 'Capsule Start' not in data or 'Capsule End' not in data:
                    raise SPyRuntimeError('Condition data requires "Capsule Start" and "Capsule End" columns')

                _put_item_defaults(condition_metadata)

                push_result_df.at[0, 'Name'] = condition_metadata['Name']

                status.add_job(0,
                               (_push_condition, session, condition_metadata, replace, data, 0, status,
                                capsule_property_metadata),
                               _on_success)

            except BaseException as e:
                _common.raise_or_catalog(status=status, df=push_result_df, index=0,
                                         column='Push Result', e=e)

        else:
            for status_index, row in push_result_df.iterrows():
                try:
                    if 'StoredSignal' in _common.get(row, 'Type'):
                        signal_metadata = row.to_dict()
                        _put_item_defaults(signal_metadata)
                        status.add_job(status_index,
                                       (_push_signal, session, None, signal_metadata, replace, None, None,
                                        type_mismatches, status_index, status),
                                       _on_success)

                    elif 'StoredCondition' in _common.get(row, 'Type'):
                        condition_metadata = row.to_dict()
                        _put_item_defaults(condition_metadata)
                        status.add_job(status_index,
                                       (_push_condition, session, condition_metadata, replace, data, status_index,
                                        status, capsule_property_metadata))
                except BaseException as e:
                    _common.raise_or_catalog(status=status, df=push_result_df, index=status_index,
                                             column='Push Result', e=e)

        status.execute_jobs(session)

        for status_index, status_row in status.df.iterrows():
            push_result_df.at[
                status_index, 'Push Result'] = status.df.at[status_index, 'Result']
            push_result_df.at[status_index, 'Push Count'] = status.df.at[status_index, 'Count']
            push_result_df.at[status_index, 'Push Time'] = status.df.at[status_index, 'Time']

    if metadata is not None and 'Asset Object' in metadata.columns:
        for _, _row in metadata.iterrows():
            asset_object = _row['Asset Object']
            if not pd.isna(asset_object):
                asset_object.context.push_df = push_result_df

    # Look for Workbook objects in the 'Object' column of the metadata DataFrame.
    if metadata is not None and 'Type' in metadata.columns:
        _handle_workbooks_in_metadata_dataframe(metadata, workbook_context, worksheet)

    _auto_populate_worksheet_if_necessary(workbook_context, worksheet, sample_stats, replace, push_result_df)

    push_workbooks_status = status.create_inner('Push Workbooks')
    if len(workbook_context.to_push) > 0:
        push_workbooks_df: Optional[pd.DataFrame] = _push_workbooks(
            session, push_result_df, workbook_context, datasource, push_workbooks_status)

        workbook_context.item_map = push_workbooks_df.spy.item_map

    if metadata is not None and not metadata.empty:
        def _metadata_push_second_pass_filter(_row: pd.Series):
            return _row['Type'] != 'Workbook' and (_row['Type'] == 'Display' and _common.present(_row, 'Object'))

        push_result_df = _metadata.push(session, push_result_df, workbook_context, datasource_output, sync_token,
                                        _metadata_push_second_pass_filter, push_metadata_status,
                                        cleanse_df_first=False, state_file=metadata_state_file,
                                        planning_to_archive=archive)

    if archive:
        status.update(f'Archiving obsolete items in Asset Tree <strong>{tree_root}</strong> scoped to '
                      f'workbook ID <strong>{workbook_context.workbook_id}</strong>.', Status.RUNNING)
        _archive_tree_items(session, datasource_output, workbook_context.workbook_id, tree_root, sync_token, status)

    if workbook_context.workbook_object is not None and workbook_context.worksheet_object is None:
        workbook_context.worksheet_object = _determine_primary_worksheet(session, status, workbook_context.workbook_id)

    workbook_url = None
    if workbook_context.workbook_object:
        workbook_push_status = 'Success'
        if not push_workbooks_status.df.empty:
            rows = list()
            if 'ID' in push_workbooks_status.df.columns:
                rows = push_workbooks_status.df[
                    push_workbooks_status.df['ID'] == workbook_context.workbook_object.id]
            if len(rows) == 0 and 'Pushed Workbook ID' in push_workbooks_status.df.columns:
                rows = push_workbooks_status.df[
                    push_workbooks_status.df['Pushed Workbook ID'] == workbook_context.workbook_object.id]
            if len(rows) != 1:
                raise SPyRuntimeError('Unexpected error: "Push Workbooks" inner status does not contain row for '
                                      'primary workbook')
            if 'Result' not in rows.columns:
                raise SPyRuntimeError(
                    'Unexpected error: "Push Workbooks" inner status does not contain "Result" column')

            workbook_push_status = rows.iloc[0]['Result']

        if workbook_push_status != 'Success':
            scope_string = '.'
            status.warn(f'An error was encountered pushing workbook/worksheet:\n'
                        f'<strong>{workbook_push_status}</strong>\n'
                        'As a result, no URL link is available.')
        else:
            workbook_url = workbook_context.get_workbook_url(session)

            scope_string = ' and scoped to workbook ID <strong>%s</strong><br>Click the following link to see what ' \
                           'you pushed in Seeq:<br><a href="%s" target="_new">%s</a>' % (workbook_context.workbook_id,
                                                                                         workbook_url,
                                                                                         workbook_url)
    else:
        scope_string = ' and globally scoped.'

    status.update(
        f'Pushed successfully to datasource <strong>{datasource_output.name} [Datasource ID: '
        f'{datasource_output.datasource_id}]</strong>{scope_string}', Status.SUCCESS)

    push_df_properties = types.SimpleNamespace(
        func='spy.push',
        kwargs=input_args,
        workbook_id=workbook_context.workbook_id,
        worksheet_id=workbook_context.worksheet_id,
        workbook_url=workbook_url,
        status=status)

    _common.put_properties_on_df(push_result_df, push_df_properties)

    return push_result_df


@dataclass
class WorkbookContext:
    workbook_object: Optional[spy.workbooks.Analysis] = None
    worksheet_object: Optional[spy.workbooks.AnalysisWorksheet] = None
    folder_id: Optional[str] = None
    to_push: list = field(default_factory=list)
    item_map: spy.workbooks.ItemMap = None

    def _lookup(self, _id):
        if self.item_map is not None and _id in self.item_map:
            return self.item_map[_id]
        else:
            return _id

    @property
    def workbook_id(self):
        if self.workbook_object is None:
            return None

        return self._lookup(self.workbook_object.id)

    @property
    def worksheet_id(self):
        if self.worksheet_object is None:
            return None

        return self._lookup(self.worksheet_object.id)

    def determine_folder_id(self):
        # This is called deliberately at the top of the push function so that it's calculated once and then used
        # consistently throughout, even if the workbook_object changes.

        if self.workbook_object is None:
            return None

        self.folder_id = None
        if not isinstance(self.workbook_object, spy.workbooks.AnalysisTemplate):
            if (_common.present(self.workbook_object, 'Ancestors') and
                    len(self.workbook_object['Ancestors']) > 0):
                self.folder_id = self.workbook_object['Ancestors'][-1]

        # Here we cover the case where an admin is pushing data to a single workbook that they don't own. In R51,
        # there's a proper user folder in the path that can be used as the folder_id. In R50 there is no such user
        # folder, so the folder_id will end up being __All__ or __Shared__, which is not viable to use as a parent
        # folder. But in the case where we're pushing to only the primary workbook, then we don't need to supply the
        # folder_id because the workbook is not being moved and we're not adding other sibling workbooks (and therefore
        # we don't need to know the actual folder that the workbook is in).
        if (self.folder_id in spy.workbooks.SYNTHETIC_FOLDERS and len(self.to_push) == 1 and
                self.to_push[0] == self.workbook_object):
            self.folder_id = None

    def get_workbook_url(self, session: Session):
        if self.workbook_object is None:
            return None

        return '%s/%sworkbook/%s/worksheet/%s' % (
            session.public_url,
            (self.folder_id + '/') if self.folder_id is not None else '',
            self.workbook_id,
            self.worksheet_id
        )


def _determine_workbook_context_from_id(session: Session, status: Status, workbook_arg, worksheet_arg) -> \
        WorkbookContext:
    primary_workbooks = spy.workbooks.pull(pd.DataFrame([{
        'ID': _common.sanitize_guid(workbook_arg),
        'Type': 'Workbook',
        'Workbook Type': 'Analysis'
    }]),
        include_inventory=False,
        # Pulling worksheets can be expensive. If we just want to push items without changing the UI, skip that.
        specific_worksheet_ids=list() if worksheet_arg is None else None,
        status=status.create_inner('Pull Workbook', quiet=True),
        session=session)

    if len(primary_workbooks) == 0 or not isinstance(primary_workbooks[0], _workbook.Workbook):
        raise SPyRuntimeError(f'Workbook with ID "{_common.sanitize_guid(workbook_arg)}" not found')

    # noinspection PyTypeChecker
    primary_workbook: spy.workbooks.Analysis = primary_workbooks[0]
    if isinstance(worksheet_arg, str):
        primary_worksheet = primary_workbook.worksheet(worksheet_arg)
    elif isinstance(workbook_arg, spy.workbooks.AnalysisWorksheetTemplate):
        primary_worksheet = workbook_arg
    else:
        primary_worksheet = None

    return WorkbookContext(workbook_object=primary_workbook, worksheet_object=primary_worksheet)


def _determine_workbook_context_from_list(session: Session, status: Status, workbook_arg, datasource_arg):
    analysis_workbooks = [w for w in workbook_arg if w['Workbook Type'] == 'Analysis']
    if len(analysis_workbooks) == 0:
        raise SPyValueError(
            f'workbook argument is a WorkbookList that contains no Analysis workbooks. You must supply at '
            f'least one (and ideally only one, otherwise things can get confusing) Analysis workbook in the '
            f'list')

    primary_workbook = analysis_workbooks[0]

    if len(analysis_workbooks) > 1:
        status.warn(f'workbook argument is a WorkbookList that contains more than one Analysis workbook. As a '
                    f'result, the first workbook "{primary_workbook}" is the one to which '
                    f'signals/conditions/scalars (etc) will be pushed')

    push_workbooks_df = spy.workbooks.push(workbook_arg, datasource=datasource_arg, specific_worksheet_ids=list(),
                                           status=status.create_inner('Create Workbook', quiet=True), session=session)

    return WorkbookContext(workbook_object=primary_workbook, to_push=workbook_arg,
                           item_map=push_workbooks_df.spy.item_map)


def _determine_workbook_context_from_analysis_template(session: Session, status: Status, workbook_arg, datasource_arg):
    push_workbooks_df = spy.workbooks.push(workbook_arg, datasource=datasource_arg, specific_worksheet_ids=list(),
                                           status=status.create_inner('Create Workbook', quiet=True),
                                           session=session)

    # noinspection PyTypeChecker
    primary_workbook: spy.workbooks.Analysis = push_workbooks_df.spy.output[0]

    return WorkbookContext(workbook_object=primary_workbook, to_push=[workbook_arg])


def _determine_workbook_context_from_string(session: Session, status: Status, workbook_arg, worksheet_arg,
                                            datasource_arg):
    search_query, workbook_name = create_analysis_search_query(workbook_arg)
    search_df = spy.workbooks.search(search_query, quiet=True, session=session)
    workbooks_to_push = list()
    worksheet_object = None
    if len(search_df) == 0:
        workbook_object = spy.workbooks.Analysis({'Name': workbook_name})
        path = _common.get(search_query, 'Path')
        inner_status = status.create_inner('Create Workbook', quiet=True)
        if isinstance(worksheet_arg, spy.workbooks.AnalysisWorksheetTemplate):
            workbooks_to_push = [workbook_object]
            workbook_object.worksheets.append(worksheet_arg)

            # Don't push any worksheets, since we can't resolve template parameters yet
            specific_worksheet_ids = list()

            spy.workbooks.push(
                workbook_object, path=path, include_inventory=False, datasource=datasource_arg,
                specific_worksheet_ids=specific_worksheet_ids, status=inner_status, session=session)
        else:
            worksheet_name = worksheet_arg if isinstance(worksheet_arg, str) else _common.DEFAULT_WORKSHEET_NAME
            worksheet_object = workbook_object.worksheet(worksheet_name)

            spy.workbooks.push(workbook_object, path=path, include_inventory=False, datasource=datasource_arg,
                               status=inner_status, session=session)
    else:
        # noinspection PyTypeChecker
        workbook_object: spy.workbooks.Analysis = spy.workbooks.pull(
            search_df,
            include_inventory=False,
            # Pulling worksheets can be expensive. If we just want to push items without changing the UI, skip that.
            specific_worksheet_ids=list() if worksheet_arg is None else None,
            status=status.create_inner('Pull Workbook', quiet=True),
            session=session)[0]

        if isinstance(worksheet_arg, spy.workbooks.AnalysisWorksheetTemplate):
            workbooks_to_push = [workbook_object]
            worksheet_object = worksheet_arg
            if worksheet_object.name in workbook_object.worksheets:
                existing_worksheet = workbook_object.worksheets[worksheet_object.name]
                worksheet_object['ID'] = existing_worksheet['ID']
                workbook_object.worksheets[worksheet_object['ID']] = worksheet_object
            else:
                workbook_object.worksheets.append(worksheet_object)

        elif worksheet_arg is not None:
            worksheet_name = worksheet_arg if isinstance(worksheet_arg, str) else _common.DEFAULT_WORKSHEET_NAME
            worksheet_object = workbook_object.worksheet(worksheet_name)

    return WorkbookContext(workbook_object=workbook_object, worksheet_object=worksheet_object,
                           to_push=workbooks_to_push)


def _determine_workbook_context(session: Session, status: Status, workbook_arg, worksheet_arg, datasource_arg):
    if _common.is_guid(workbook_arg):
        return _determine_workbook_context_from_id(session, status, workbook_arg, worksheet_arg)
    elif isinstance(workbook_arg, list):
        return _determine_workbook_context_from_list(session, status, workbook_arg, datasource_arg)
    elif isinstance(workbook_arg, spy.workbooks.AnalysisTemplate):
        return _determine_workbook_context_from_analysis_template(session, status, workbook_arg, datasource_arg)
    elif workbook_arg is not None:
        return _determine_workbook_context_from_string(session, status, workbook_arg, worksheet_arg, datasource_arg)
    else:
        return WorkbookContext()


def _determine_primary_worksheet(session: Session, status: Status, workbook_id: str) -> Optional[WorksheetOutputV1]:
    # Get the primary worksheet so we can build up a correct link url
    workbooks_api = WorkbooksApi(session.client)
    worksheet_output_list = safely(
        lambda: workbooks_api.get_worksheets(workbook_id=workbook_id,
                                             is_archived=False, offset=0, limit=1),
        action_description=f'get first worksheet for workbook {workbook_id}',
        status=status)
    if (worksheet_output_list and len(worksheet_output_list.worksheets) > 0 and
            worksheet_output_list.worksheets[0] is not None):
        return worksheet_output_list.worksheets[0]
    # This can return None if a template worksheet failed to push properly. The caller will detect this case and
    # present the inner error to the user.


def _handle_workbooks_in_metadata_dataframe(metadata, workbook_context: WorkbookContext, worksheet_arg):
    workbook_rows = metadata[metadata['Type'] == 'Workbook']
    for _, workbook_row in workbook_rows.iterrows():
        workbook_object = workbook_row['Object']  # type: spy.workbooks.Workbook
        primary_name = (workbook_context.workbook_object.name if workbook_context.workbook_object else
                        _common.DEFAULT_WORKBOOK_NAME)

        if isinstance(workbook_object, spy.workbooks.WorkbookTemplate):
            if not workbook_object.is_overridden('Name'):
                # If the user didn't override the name deliberately, then we assume they would like to control
                # the name of the workbook via the spy.push(workbook) parameter.
                workbook_object.name = None

        if workbook_object.name is None:
            # The user wants the name of the workbook object to take on the name passed in to spy.push()
            workbook_object.name = primary_name

        if isinstance(workbook_object, spy.workbooks.Analysis) and workbook_object.name == primary_name:
            if isinstance(workbook_object, spy.workbooks.AnalysisTemplate):
                # If this is a template, we want to override the ID so we push to the right workbook that contains
                # the asset tree (or any other metadata we've pushed), and get rid of the label (but only on the
                # workbook, not the worksheets/worksteps).
                workbook_id_to_keep = workbook_context.workbook_id
                workbook_context.workbook_object = workbook_object
                workbook_context.workbook_object['ID'] = workbook_id_to_keep
                workbook_context.workbook_object.label = None
            else:
                workbook_context.workbook_object = workbook_object

        for worksheet_object in workbook_object.worksheets:
            if worksheet_object.name is None:
                # The user wants the name of the worksheet to take on the name passed in to spy.push()
                worksheet_object.name = worksheet_arg if worksheet_arg else _common.DEFAULT_WORKSHEET_NAME

        workbook_context.to_push.append(workbook_object)


def _auto_populate_worksheet_if_necessary(workbook_context: WorkbookContext, worksheet_arg, sample_stats,
                                          replace, push_result_df):
    if workbook_context.worksheet_object is None:
        return

    # Only auto-populate a worksheet if the user specified a string as the worksheet arg
    if not isinstance(worksheet_arg, str):
        return

    _auto_populate_worksheet(sample_stats.earliest_sample_in_ms, sample_stats.latest_sample_in_ms,
                             replace, push_result_df, workbook_context.worksheet_object)

    if workbook_context.workbook_object not in workbook_context.to_push:
        workbook_context.to_push.append(workbook_context.workbook_object)


def _auto_populate_worksheet(earliest_sample_in_ms, latest_sample_in_ms, replace, push_result_df, worksheet_object):
    display_items = pd.DataFrame()

    if 'Type' in push_result_df:
        display_items = push_result_df[push_result_df['Type'].isin(['StoredSignal', 'CalculatedSignal',
                                                                    'StoredCondition', 'CalculatedCondition',
                                                                    'CalculatedScalar', 'Chart',
                                                                    'ThresholdMetric'])]

    worksheet_object.display_items = display_items.head(10)
    if earliest_sample_in_ms is not None and latest_sample_in_ms is not None:
        _range = {
            'Start': pd.Timestamp(int(earliest_sample_in_ms), unit='ms', tz='UTC'),
            'End': pd.Timestamp(int(latest_sample_in_ms), unit='ms', tz='UTC')
        }
        worksheet_object.display_range = _range
        worksheet_object.investigate_range = _range
    elif replace is not None:
        _range = replace
        worksheet_object.display_range = _range
        worksheet_object.investigate_range = _range


def create_analysis_search_query(workbook) -> tuple[dict[str, str], str]:
    workbook_spec_parts = _common.path_string_to_list(workbook)
    search_query = dict()
    if len(workbook_spec_parts) > 1:
        search_query['Path'] = _common.path_list_to_string(workbook_spec_parts[0:-1])
        workbook_name = workbook_spec_parts[-1]
    else:
        workbook_name = workbook_spec_parts[0]
    search_query['Name'] = f'/^{re.escape(workbook_name)}$/'
    search_query['Workbook Type'] = 'Analysis'
    return search_query, workbook_name


def _push_signal(session: Session, column, signal_metadata, replace, data, signal_output, type_mismatches, status_index,
                 status: Status) -> tuple[float, float, str, dict]:
    signals_api = SignalsApi(session.client)
    signal_input = SignalInputV1()
    _metadata.dict_to_signal_input(signal_metadata, signal_input)
    if replace is not None:
        add_samples_input = SamplesOverwriteInputV1()
    else:
        add_samples_input = SamplesInputV1()
    add_samples_input.samples = list()
    count = 0
    page_count = 0
    is_string = None
    # noinspection PyTypeChecker
    timer = _common.timer_start()
    earliest_sample_in_ms = None
    latest_sample_in_ms = None

    def _put_signal(_signal_metadata, _signal_input) -> SignalOutputV1:
        return signals_api.put_signal_by_data_id(datasource_class=_signal_metadata['Datasource Class'],
                                                 datasource_id=_signal_metadata['Datasource ID'],
                                                 data_id=_signal_metadata['Data ID'],
                                                 body=_signal_input)

    if replace is not None:
        pd_start, pd_end = _login.validate_start_and_end(session, replace['Start'], replace['End'])
        interval_input = IntervalV1()
        interval_input.start = pd_start
        interval_input.end = pd_end
        add_samples_input.interval = interval_input

    if data is not None:
        # Performance notes: It was found that pulling out the column as a pd.Series and then using series.iteritems()
        #                    instead of doing data.iterrows() was 5x-6x faster
        series: pd.Series = data[column]
        for index, sample_value in series.iteritems():
            if pd.isna(sample_value) and sample_value is not None:
                continue

            if not isinstance(index, pd.Timestamp):
                raise SPyRuntimeError('data index must only be pd.Timestamp objects, but %s found instead' %
                                      type(index))

            # Add a timezone (from options.default_timezone) if necessary
            sample_timestamp = _login.parse_input_datetime(session, index)

            if is_string is None:
                if _common.present(signal_metadata, 'Value Unit Of Measure'):
                    is_string = (signal_metadata['Value Unit Of Measure'].lower() == 'string')
                else:
                    is_string = isinstance(sample_value, str)

                if is_string:
                    signal_input.value_unit_of_measure = 'string'

            if is_string != isinstance(sample_value, str):
                # noinspection PyBroadException
                try:
                    if is_string:
                        if sample_value is not None:
                            sample_value = str(sample_value)
                    else:
                        if data[column].dtype.name == 'int64':
                            sample_value = int(sample_value)
                        else:
                            sample_value = float(sample_value)
                except BaseException:
                    # Couldn't convert it, fall through to the next conditional
                    pass

            if is_string != isinstance(sample_value, str):
                if type_mismatches == 'drop':
                    continue
                elif type_mismatches == 'raise':
                    raise SPyRuntimeError('Column "%s" was detected as %s, but %s value at (%s, %s) found. Supply '
                                          'type_mismatches parameter as "drop" to ignore the sample entirely or '
                                          '"invalid" to insert an INVALID sample in its place.' %
                                          (column, 'string-valued' if is_string else 'numeric-valued',
                                           'numeric' if is_string else 'string',
                                           index, sample_value))
                else:
                    sample_value = None

            if isinstance(sample_value, np.number):
                sample_value = sample_value.item()

            if not signal_output:
                signal_output = _put_signal(signal_metadata, signal_input)

            sample_input = SampleInputV1()
            key_in_ms = sample_timestamp.value / 1000000
            earliest_sample_in_ms = min(key_in_ms,
                                        earliest_sample_in_ms) if earliest_sample_in_ms is not None else key_in_ms
            latest_sample_in_ms = max(key_in_ms, latest_sample_in_ms) if latest_sample_in_ms is not None else key_in_ms

            sample_input.key = sample_timestamp.value
            sample_input.value = sample_value
            add_samples_input.samples.append(sample_input)

            if len(add_samples_input.samples) >= session.options.push_page_size:
                if replace is not None:
                    signals_api.put_samples(id=signal_output.id,
                                            body=add_samples_input)
                else:
                    signals_api.add_samples(id=signal_output.id,
                                            body=add_samples_input)
                count += len(add_samples_input.samples)
                page_count += 1
                status.send_update(status_index, {
                    'Result': f'Pushed to {sample_timestamp}',
                    'Count': count,
                    'Pages': page_count,
                    'Time': _common.timer_elapsed(timer)
                })

                add_samples_input.samples = list()

    if not signal_output:
        if signal_input.value_unit_of_measure is None and not _common.present(signal_metadata, 'ID'):
            raise SPyRuntimeError(f'Column "{column}" contains no data, does not correspond to a pre-existing signal, '
                                  f'and has no Value Unit of Measure provided. Drop the column from the data '
                                  f'dataframe, or provide an ID or Value Unit of Measure for "{column}" using the '
                                  f'metadata parameter.')
        signal_output = _put_signal(signal_metadata, signal_input)

    if len(add_samples_input.samples) > 0 or replace is not None:
        if replace is not None:
            signals_api.put_samples(id=signal_output.id,
                                    body=add_samples_input)
        else:
            signals_api.add_samples(id=signal_output.id,
                                    body=add_samples_input)
        count += len(add_samples_input.samples)
        page_count += 1

    status.send_update(status_index, {
        'Result': 'Success',
        'Count': count,
        'Pages': page_count,
        'Time': _common.timer_elapsed(timer)
    })

    return (earliest_sample_in_ms, latest_sample_in_ms,
            signal_output.id if signal_output is not None else None, signal_metadata)


def _push_condition(session: Session, condition_metadata, replace, data, status_index, status: Status,
                    capsule_property_metadata) -> tuple[float, float, str, dict]:
    conditions_api = ConditionsApi(session.client)
    condition_batch_input = ConditionBatchInputV1()
    condition_update_input = ConditionUpdateInputV1()
    _metadata.dict_to_condition_update_input(condition_metadata, condition_update_input)

    condition_batch_input.conditions = [condition_update_input]
    condition_update_input.datasource_class = condition_metadata['Datasource Class']
    condition_update_input.datasource_id = condition_metadata['Datasource ID']
    items_batch_output: ItemBatchOutputV1 = conditions_api.put_conditions(body=condition_batch_input)
    item_update_output: ItemUpdateOutputV1 = items_batch_output.item_updates[0]
    if replace is not None:
        capsules_input = CapsulesOverwriteInputV1()
    else:
        capsules_input = CapsulesInputV1()
    capsules_input.capsules = list()
    capsules_input.key_unit_of_measure = 'ns'
    count = 0
    page_count = 0
    timer = _common.timer_start()
    earliest_sample_in_ms = None
    latest_sample_in_ms = None

    if replace is not None:
        pd_start, pd_end = _login.validate_start_and_end(session, replace['Start'], replace['End'])
        interval_input = IntervalV1()
        interval_input.start = pd_start
        interval_input.end = pd_end
        capsules_input.interval = interval_input

    if data is not None:
        for index, row in data.iterrows():
            capsule = CapsuleV1()
            _dict_to_capsule(row.to_dict(), capsule, capsule_property_units=capsule_property_metadata)
            pd_start, pd_end = _login.validate_start_and_end(session, row['Capsule Start'], row['Capsule End'])
            capsule.start = pd_start.value
            capsule.end = pd_end.value
            capsules_input.capsules.append(capsule)
            # noinspection PyTypeChecker
            key_in_ms = capsule.start / 1000000
            earliest_sample_in_ms = min(key_in_ms,
                                        earliest_sample_in_ms) if earliest_sample_in_ms is not None else key_in_ms
            # noinspection PyTypeChecker
            key_in_ms = capsule.end / 1000000
            latest_sample_in_ms = max(key_in_ms, latest_sample_in_ms) if latest_sample_in_ms is not None else key_in_ms

            if len(capsules_input.capsules) > session.options.push_page_size:
                if replace is not None:
                    conditions_api.put_capsules(id=item_update_output.item.id, body=capsules_input)
                else:
                    conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)

                count += len(capsules_input.capsules)
                page_count += 1
                status.send_update(status_index, {
                    'Result': f'Pushed to {index}',
                    'Count': count,
                    'Pages': page_count,
                    'Time': _common.timer_elapsed(timer)
                })
                capsules_input.capsules = list()

    if len(capsules_input.capsules) > 0 or replace is not None:
        if replace is not None:
            conditions_api.put_capsules(id=item_update_output.item.id, body=capsules_input)
        else:
            conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)
        count += len(capsules_input.capsules)
        page_count += 1

    status.send_update(status_index, {
        'Result': 'Success',
        'Count': count,
        'Pages': page_count,
        'Time': _common.timer_elapsed(timer)
    })

    return earliest_sample_in_ms, latest_sample_in_ms, item_update_output.item.id, condition_metadata


def _dict_to_capsule(d, capsule, capsule_property_units=None):
    _metadata.dict_to_input(d, capsule, 'properties', {
        'Capsule Start': None,
        'Capsule End': None
    }, capsule_property_units)


def _push_workbooks(session: Session, push_result_df, workbook_context: WorkbookContext, datasource,
                    status: Status) -> pd.DataFrame:
    for workbook in workbook_context.to_push:  # type: spy.workbooks.Analysis
        if not isinstance(workbook, spy.workbooks.Analysis):
            continue

        for worksheet in workbook.worksheets:  # type: spy.workbooks.AnalysisWorksheet
            if isinstance(worksheet, spy.workbooks.AnalysisWorksheetTemplate):
                # This is a template, in which case we don't need to fix up display_items
                continue

            for workstep in worksheet.worksteps.values():  # type: spy.workbooks.AnalysisWorkstep
                display_items = workstep.display_items

                # CRAB-19586: Cannot convert string to float error
                # 'ID' field is sometimes assigned float dtype in display_items dataframe but cannot duplicate this
                # This should be resolved in a fix done in workbooks/_workstep.py that cast the display_items df
                # as object type but since cannot duplicate the issue, let's patch here too
                display_items['ID'] = display_items['ID'].astype(object)

                for index, display_item in display_items.iterrows():
                    if not _common.present(display_item, 'ID') or _common.get(display_item, 'Reference', False):
                        pushed_item = _common.look_up_in_df(display_item, push_result_df)
                        display_items.at[index, 'ID'] = pushed_item['ID']

                workstep.display_items = display_items

    folder = workbook_context.folder_id if (_common.is_guid(workbook_context.folder_id) or workbook_context.folder_id
                                            in [_folder.MY_FOLDER, _folder.CORPORATE]) else None

    # We have to include the inventory when we're pushing templates because it allows us to fall back on the
    # placeholder items when the user hasn't mapped every template parameter to a new item. And then it's important
    # that refresh=False so that we're not downloading potentially hundreds of thousands of workbook-scoped items.
    return spy.workbooks.push(workbook_context.to_push, path=folder, refresh=False,
                              datasource=datasource, lookup_df=push_result_df, include_inventory=True,
                              status=status, session=session)


def _tree_root_to_data_id_regex(workbook_id, tree_root) -> str:
    path_regex = re.escape(tree_root) + r'(\s*>>.*)?'
    return r'\[' + re.escape(workbook_id if workbook_id else EMPTY_GUID) + r'\] \{.+?\} (' + path_regex + r')'


def get_common_root(data) -> Optional[str]:
    if isinstance(data, pd.DataFrame) and 'Type' in data:
        data = data[data.Type != 'Workbook']

    def get_path_list(row):
        path = _metadata.determine_path(row)
        name = _common.get(row, 'Name')
        if name:
            if path:
                return _common.path_string_to_list(path + ' >> ' + name)
            else:
                return _common.path_string_to_list(name)
        else:
            return list()

    # noinspection PyTypeChecker
    full_path_series = data.apply(get_path_list, axis=1) if isinstance(data, pd.DataFrame) else data

    return _common.get_shared_path_root(full_path_series)


def _archive_tree_items(session: Session, datasource_output, workbook_id, tree_root, sync_token, status: Status):
    items_api = ItemsApi(session.client)
    datasources_api = DatasourcesApi(session.client)
    trees_api = TreesApi(spy.client)

    # CRAB-32796: if the datasource has roughly 20,000 or more items, we must archive manually

    # Get datasource again with updated item counts.
    datasource_output = datasources_api.get_datasource(id=datasource_output.id)
    counts = dict.fromkeys((
        SeeqNames.Properties.signal_count,
        SeeqNames.Properties.condition_count,
        SeeqNames.Properties.asset_count,
        SeeqNames.Properties.scalar_count,
        SeeqNames.Properties.user_group_count,
    ), 0)
    for property_output in datasource_output.additional_properties:
        if property_output.name in counts:
            try:
                counts[property_output.name] += int(property_output.value)
            except ValueError:
                pass
    known_count = sum(counts.values())

    # We need to use a heuristic because Metrics and Displays aren't included in this count. Assume that:
    # - There are close to 0 user groups
    # - There are no more metrics or displays than there are items of any other type
    potential_count = (6 / 4) * known_count
    archive_manually = potential_count > DATASOURCE_CLEANUP_ITEM_COUNT_THRESHOLD

    if archive_manually:

        status.df = pd.DataFrame([{'Items Checked': 0, 'Items Archived': 0}])
        status.update()
        item_counts = types.SimpleNamespace(checked=0, archived=0)

        def update():
            status.df['Items Checked'] = item_counts.checked
            status.df['Items Archived'] = item_counts.archived
            status.update()

        def paginated_iter(paginated_function, pagesize=40):
            offset = 0
            limit = pagesize
            result = paginated_function(offset, limit)
            yield from result
            while result is not None and len(result) == pagesize:
                offset += pagesize
                result = paginated_function(offset, limit)
                yield from result

        def get_property(item: TreeItemOutputV1, property_name: str) -> Optional[str]:
            for prop in item.properties:
                if prop.name == property_name:
                    return prop.value
            return None

        def get_children(parent_id, offset, limit):
            if not _common.is_guid(parent_id):
                return
            scope = workbook_id
            if not _common.is_guid(workbook_id):
                scope = EMPTY_GUID
            return safely(lambda: trees_api.get_tree(id=parent_id,
                                                     scope=[scope],
                                                     offset=offset,
                                                     limit=limit,
                                                     include_descendants=False).children,
                          action_description=f'get asset children of {parent_id}',
                          status=status.create_inner(f'Get asset children of {parent_id}', errors='catalog'),
                          additional_errors=[400])

        def children_to_archive(parent_id):
            child: TreeItemOutputV1
            for child in paginated_iter(functools.partial(get_children, parent_id)):
                if get_property(child, SeeqNames.Properties.sync_token) != sync_token:
                    yield child.id
                item_counts.checked += 1
                if item_counts.checked % 10 == 0:
                    update()
                if child.has_children:
                    yield from children_to_archive(child.id)

        root_data_id = _metadata.get_scoped_data_id({'Type': 'Asset', 'Name': tree_root}, workbook_id)
        root_search = spy.search(pd.Series({'Datasource Class': datasource_output.datasource_class,
                                            'Datasource ID': datasource_output.datasource_id,
                                            'Data ID': root_data_id}),
                                 workbook=workbook_id,
                                 status=status.create_inner('Find Tree Root'))
        if len(root_search) != 1:
            raise SPyRuntimeError
        root_id = root_search.loc[0, 'ID']

        for item_id in children_to_archive(root_id):
            try:
                items_api.archive_item(id=item_id)
                item_counts.archived += 1
                if item_counts.archived % 10 == 0:
                    update()
            except ApiException as e:
                if 'does not have MANAGE access' in get_api_exception_message(e):
                    status.warn(f'Warning: could not archive stale tree item {item_id} because user '
                                f'<strong>{session.user.name} ({session.user.email})</strong> does '
                                f'not have MANAGE permissions to it.')
                elif status.errors == 'raise':
                    raise e
                else:
                    status.warn(str(e))

        status.df = pd.DataFrame()
        status.update()
    else:
        datasource_clean_up_input = DatasourceCleanUpInputV1()
        datasource_clean_up_input.sync_token = sync_token
        datasource_clean_up_input.item_data_id_regex_filter = _tree_root_to_data_id_regex(workbook_id, tree_root)

        datasources_api.clean_up(id=datasource_output.id, body=datasource_clean_up_input)
