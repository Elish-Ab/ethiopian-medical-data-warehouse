from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_name: str
    class_label: str
    confidence: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResultResponse(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True