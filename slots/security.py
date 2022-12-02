from pylon.core.tools import log, web
from ..tools.main import get_engagements_json


class Slot:
    integration_name = 'reporter_engagement'
    section_name = 'reporters'

    @web.slot(f'security_{section_name}_content')
    def toggle_content(self, context, slot, payload):
        engagements_json = get_engagements_json(self)
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
