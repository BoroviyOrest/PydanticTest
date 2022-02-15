from config_to_pydantic import vf_config_to_pydantic_model
from models import BaseEventModel

custom_fields = [
    {
        'field_id': 'online_offline',
        'data_type': 3,
        'editable_in_statuses': [10, 20],
        'obligatory_from_status': 20,
        'is_system_field': False,
        'value_list': [],
    }
]

EventModel = vf_config_to_pydantic_model('EventModel', BaseEventModel, custom_fields)


data_to_validate = {
    'type': 1,
    'description': 'description',
    'status': 20,
    'plan_account': '620baa694426319dc0f48219',
    'start_date': '20220215',
    'end_date': '20220228',
    'online_offline': 'value_id',
}
event = EventModel(**data_to_validate)

print(event)
print(event.json())
