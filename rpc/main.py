from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import web

from tools import rpc_tools, secrets_tools


class RPC:
    integration_name = 'reporter_engagement'

    @web.rpc(f'dusty_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def make_dusty_config(self, context, test_params, scanner_params):
        """ Prepare dusty config for reporter """  

        result = {
            "engagement_id": scanner_params,
            "url": secrets_tools.unsecret(
                "{{secret.galloper_url}}",
                project_id=test_params['project_id']
            ),
            "token": secrets_tools.unsecret(
                "{{secret.auth_token}}",
                project_id=test_params['project_id']
            ),
            "project_id": test_params['project_id']
        }

        return 'engagement', result
