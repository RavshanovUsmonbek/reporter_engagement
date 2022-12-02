import json


def get_engagements_json(module):
    project_id = module.context.rpc_manager.call.project_get_id()
    result = module.context.rpc_manager.call.engagement_list_engagements(project_id)
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
    return json.dumps(engagements)