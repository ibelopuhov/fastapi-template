from pydantic import BaseModel

# Fast API
class InData(BaseModel):
    """
    Метоописание запроса к сервису 
    """
    flat: bool = False
    text: str
