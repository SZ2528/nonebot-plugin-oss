from pydantic import BaseModel, field_validator
from typing import Set


class Config(BaseModel):
    superusers: Set[str]
    oss_api_client_id: int
    oss_api_client_secret: str
    oss_command_priority: int = 10
