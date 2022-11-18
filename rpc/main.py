# from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import web

from tools import rpc_tools


class RPC:
    integration_name = 'reporter_issues'

    @web.rpc(f'dusty_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def make_dusty_config(self, context, test_params, scanner_params):
        """ Prepare dusty config for reporter """
        result = {"engagement": scanner_params}
        return 'reporter_issues', result
