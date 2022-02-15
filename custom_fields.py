from datetime import date, datetime

from bson import ObjectId


class PydanticObjectId(ObjectId):
    """Custom validator class for MongoDB ObjectId"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class VFDate(date):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, datetime):
            return v

        if not isinstance(v, str):
            raise TypeError('str required')
        # Parse date as usual in VF
        return datetime.strptime(v, '%Y%m%d')