from sqlalchemy.orm import Session
from my_project.models import DetectionResult
from my_project.schemas import DetectionResultCreate

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetectionResult).offset(skip).limit(limit).all()

def create_detection_result(db: Session, detection: DetectionResultCreate):
    db_detection = DetectionResult(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
