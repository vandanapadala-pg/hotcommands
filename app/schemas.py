from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import datetime

class Parameter(BaseModel):
    name: str
    type: str
    required: bool = False
    default: Optional[Any] = None
    description: Optional[str] = ""
    options: Optional[List[Any]] = []
    validation_regex: Optional[str] = None

class HotCommandBase(BaseModel):
    user_id: str
    command_name: str = Field(..., regex=r"^[a-zA-Z][a-zA-Z0-9_]*$")
    query_text: str
    query_type: str = Field(..., regex=r"^(nl2sql|direct_sql|tool_call)$")
    domain: Optional[str] = None
    category: Optional[str] = None
    parameters: Optional[List[Parameter]] = []
    metadata: Optional[Dict[str, Any]] = {}

class HotCommandCreate(HotCommandBase): pass
class HotCommandUpdate(BaseModel):
    query_text: Optional[str] = None
    query_type: Optional[str] = None
    domain: Optional[str] = None
    category: Optional[str] = None
    parameters: Optional[List[Parameter]] = []
    metadata: Optional[Dict[str, Any]] = {}

class HotCommandOut(HotCommandBase):
    id: int
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config: orm_mode = True

class SaveSpaceRequest(BaseModel):
    user_id: str
    space_name: str
    content: str
    content_type: str

class SpaceOut(BaseModel):
    id: int
    user_id: str
    space_name: str
    content: str
    content_type: str
    is_shared: bool
    shared_with: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config: orm_mode = True

class ShareSpaceRequest(BaseModel):
    user_id: str
    space_name: str
    shared_with: str
