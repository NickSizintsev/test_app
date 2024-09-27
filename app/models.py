from pydantic import BaseModel, field_validator
from typing import Annotated, List, Any
from annotated_types import Gt


class UserBase(BaseModel):
    user_id: Annotated[int, Gt(0)]

    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls, user_id):
        # if type(user_id) != int:
        #     raise ValueError("ID should be int")
        if user_id <= 0:
            raise ValueError("ID should be greater than 0")
        return user_id

class UserPredict(BaseModel):
    status: str = "success"
    data: List[float]

    # @field_validator("data")
    # @classmethod
    # def validate_data(cls, data):
    #     if not data:
    #         raise ValueError("Data is empty")
    #     return data
    #
    # @field_validator("status")
    # @classmethod
    # def validate_data(cls, status):
    #     if type(status) != str:
    #         raise ValueError("Status must be str type")
    #     return status

class UserPredictError(BaseModel):
    status: str = "error"
    message: str = "Something went wrong"

