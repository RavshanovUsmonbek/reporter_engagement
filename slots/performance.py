from pylon.core.tools import log, web
from ..tools.main import get_engagements_json

class Slot:
    integration_name = 'reporter_engagement'
    section_name = 'reporters'

    @web.slot(f'backend_performance_{section_name}_content')
    def backend_toggle_content(self, context, slot, payload):
        project_integrations = get_engagements_json(self)
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance/content.html',
                project_integrations=project_integrations,
                instance_name_prefix=payload.get('instance_name_prefix', '')
            )

    @web.slot(f'backend_performance_{section_name}_scripts')
    def backend_toggle_scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance/scripts.html',
            )

    @web.slot(f'ui_performance_{section_name}_content')
    def ui_toggle_content(self, context, slot, payload):
        project_integrations = get_engagements_json(self)
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance/content.html',
                project_integrations=project_integrations,
                instance_name_prefix=payload.get('instance_name_prefix', '')
            )

    @web.slot(f'ui_performance_{section_name}_scripts')
    def ui_toggle_scripts(self, context, slot, payload):
        with context.app.app_context():
            return self.descriptor.render_template(
                'performance/scripts.html',
            )
