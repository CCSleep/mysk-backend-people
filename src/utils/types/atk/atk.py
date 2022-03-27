from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

from student_teacher.people import People


class ATKMethodEnum(str, Enum):
    oral = "oral"
    rt = "rtpcr"
    nusal = "nusal"
    other = "other"


class AtkRecord(BaseModel):
    id: int
    tester: People
    result: bool
    date: str
    method: ATKMethodEnum
    place: str
    evidence: str
