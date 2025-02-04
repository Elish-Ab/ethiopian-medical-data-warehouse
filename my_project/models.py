from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DetectionResult(Base):
    __tablename__ = 'detection_results'

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Float)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)