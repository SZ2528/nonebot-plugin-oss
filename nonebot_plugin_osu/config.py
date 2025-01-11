from pydantic import BaseModel, field_validator
from typing import Set


class Config(BaseModel):
    superusers: Set[str]
    osu_api_client_id: int
    osu_api_client_secret: str
    osu_command_priority: int = 10
