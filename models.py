from typing import Optional, Hashable, List

from bson import ObjectId
from pydantic import BaseModel, Field

from custom_fields import PydanticObjectId, VFDate


class BaseDBModel(BaseModel):
    id: PydanticObjectId = Field(alias='_id', default_factory=PydanticObjectId)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class BaseEventModel(BaseDBModel):
    type: Hashable  # For all drop-downs we need to validate if data type is hashable
    description: str
    status: int = 20
    plan_account: PydanticObjectId
    start_date: VFDate
    end_date: VFDate
    remark: str = ''


class BaseObjectiveModel(BaseModel):
    objective: Hashable
    kpi: Hashable
    amount: int = 0


class BaseActualCostModel(BaseModel):
    invoice_ref: str
    amount: int


class BasePlannedCostModel(BaseModel):
    budget_name: str
    budget_year: str
    cost_type: str
    planned_cost: str
    actual_costs: List[BaseActualCostModel]


class BaseActivationModel(BaseDBModel):
    activation: Hashable  # For all drop-downs we need to validate if data type is hashable
    activation_category: Hashable
    event_id: Optional[PydanticObjectId]
    start_date: VFDate
    end_date: VFDate
    objectives: List[BaseObjectiveModel]
    planned_costs: List[BasePlannedCostModel]
    planned_costs_total: int = 0
    actual_costs_total: int = 0
