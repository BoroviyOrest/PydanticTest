from typing import Hashable, List, Type, Optional

from pydantic import create_model, BaseModel, validator

from custom_fields import VFDate
from validators import is_editable, is_obligatory

NUMBER = 1
STRING = 2
SINGLE_SELECTION = 3
MULTIPLE_SELECTION = 4
DATE = 5
BOOLEAN = 6
PRODUCT_SELECTION = 8
TEXT_AREA = 10

# Data types are just examples and for more specific validation we can introduce custom types like VFDate
VF_DATATYPE_TO_PYTHON_TYPE_MAPPER = {
    NUMBER: int,
    STRING: str,
    SINGLE_SELECTION: Hashable,
    MULTIPLE_SELECTION: List[Hashable],
    DATE: VFDate,
    BOOLEAN: bool,
    PRODUCT_SELECTION: dict,  # it's more then just dict, but too much work for POC
    TEXT_AREA: str,
}


def vf_config_to_pydantic_model(
        model_name: str,
        base_model: Type[BaseModel],
        vf_fields: list[dict]
) -> Type[BaseModel]:
    fields = dict()
    validators = dict()

    for field in vf_fields:
        field_id = field['field_id']

        data_type = VF_DATATYPE_TO_PYTHON_TYPE_MAPPER[field['data_type']]
        fields[field_id] = (Optional[data_type], ...)

        if 'editable_in_statuses' in field:
            validators[f'is_editable_{field_id}'] = validator(field_id, allow_reuse=True)(
                is_editable(field['editable_in_statuses']))
        if 'obligatory_from_status' in field:
            validators[f'is_obligatory_{field_id}'] = validator(field_id, allow_reuse=True)(
                is_obligatory(field['obligatory_from_status']))

    pydantic_model = create_model(
        __model_name=model_name,
        __base__=base_model,
        __validators__=validators,
        **fields
    )
    return pydantic_model
