from typing import List, Optional
from uuid import UUID,uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    
class Resources(str,Enum):
    r1 = "resource1"
    r2 = "resource2"
    r3 = "resource3"
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    gender : Gender
    roles : List[Role]
    resources : List[Resources]

class UserUpdate(BaseModel):
    first_name : Optional[str]
    last_name : Optional[str]
    roles : Optional[List[Role]]
    resources : Optional[List[Resources]]