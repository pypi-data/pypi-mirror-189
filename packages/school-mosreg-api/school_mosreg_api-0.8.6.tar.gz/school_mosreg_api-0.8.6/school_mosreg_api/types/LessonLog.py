from datetime import datetime
from pydantic import BaseModel

class LessonLogEntries(BaseModel):
    """Отметка о посещаемости (Данный класс - 1 отметка)\n~~~"""
    
    person: int = None
    lesson: int = None
    person_str: str = None
    lesson_str: str = None
    comment: str = None
    status: str = None
    createdDate: datetime = None
