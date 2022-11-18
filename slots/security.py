from pylon.core.tools import log, web
from json import dumps


class Slot:
    integration_name = 'reporter_issues'
    section_name = 'reporters'

    @web.slot(f'security_{section_name}_content')
    def toggle_content(self, context, slot, payload):
        project_id = self.context.rpc_manager.call.project_get_id()
        result = self.context.rpc_manager.call.engagement_list_engagements(project_id)
        
        items = result['items'] if result['ok'] else tuple()
        engagements = []
        for index, engagement in enumerate(items):
            obj = {
                'description': engagement.name,
                'id': str(engagement.hash_id)
            }
            if index == 0:
                obj['is_default'] = True

            engagements.append(obj)
  
        engagements_json = dumps(engagements)
        with context.app.app_context():
            return self.descriptor.render_template(
                'test_toggle/content.html',
                project_integrations=engagements_json
            )


    @web.slot(f'security_{section_name}_scripts')
    def toggle_scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'test_toggle/scripts.html',
            )
