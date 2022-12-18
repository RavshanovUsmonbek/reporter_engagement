from typing import Optional
from pylon.core.tools import log
from pylon.core.tools import web
from pydantic import ValidationError
from tools import rpc_tools
from flask import url_for



from tools import rpc_tools


class RPC:
    integration_name = 'reporter_engagement'

    @web.rpc(f'backend_performance_test_create_integration_validate_{integration_name}')
    @rpc_tools.wrap_exceptions(ValidationError)
    def backend_performance_test_create_integration_validate(self, data: dict, pd_kwargs: Optional[dict] = None, **kwargs) -> dict:
        return data

    @web.rpc(f'backend_performance_execution_json_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def backend_make_execution_json_config(self, integration_data: dict) -> dict:
        """ Prepare execution_json for this integration """
        'integration_data -> {"id": <hash_id>}'
        integration_data["report_url"] = url_for('api.v1.issues.perf_report', project_id='1').rstrip('1/')
        integration_data["query_url"] = url_for('api.v1.issues.issues', project_id='1').rstrip('1/')
        return integration_data


    @web.rpc(f'ui_performance_test_create_integration_validate_{integration_name}')
    @rpc_tools.wrap_exceptions(ValidationError)
    def ui_performance_test_create_integration_validate(self, data: dict, pd_kwargs: Optional[dict] = None,
                                                             **kwargs) -> dict:

        return data

    @web.rpc(f'ui_performance_execution_json_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def ui_make_execution_json_config(self, integration_data: dict) -> dict:
        """ Prepare execution_json for this integration """
        data = {}
        data["report_url"] = url_for('api.v1.issues.perf_report', project_id='1').rstrip('1/')
        data["query_url"] = url_for('api.v1.issues.issues', project_id='1').rstrip('1/')
        data["id"] = integration_data['id']
        return data
