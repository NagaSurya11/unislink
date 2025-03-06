from pydantic import BaseModel

class Availability(BaseModel):
    available: bool