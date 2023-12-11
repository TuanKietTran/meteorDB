from pydantic import BaseModel
from sqlalchemy import Column, String
from meteor.database import BaseEntity

from meteor.models import UUIDMixin

class AppSettingsEntity(BaseEntity):
    key = Column(String(255))
    value = Column(String(255))
    description = Column(String(1023))
    type = Column(String(255))

class AppSettings(BaseModel, UUIDMixin):
    key: str
    value: str
    description: str
    type: str