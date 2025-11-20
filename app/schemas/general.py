import time

from pydantic import BaseModel

class CreateSuccess(BaseModel):
    message: str = "Request was succesfull"
    timestamp: int = int(time.time())
