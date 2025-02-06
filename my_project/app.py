import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from my_project.models import DetectionResult
from my_project.schemas import DetectionResultCreate, DetectionResultResponse
from my_project.crud import get_detection_results, create_detection_result
from my_project.database import SessionLocal, engine

# Initialize FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the YOLO Detection API"}

# Get all detection results
@app.get("/detections/", response_model=list[DetectionResultResponse])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = get_detection_results(db, skip=skip, limit=limit)
    return detections

# Create a new detection result
@app.post("/detections/", response_model=DetectionResultResponse)
def create_detection(detection: DetectionResultCreate, db: Session = Depends(get_db)):
    return create_detection_result(db=db, detection=detection)

if __name__ == "__main__":
    uvicorn.run("my_project.main:app", host="127.0.0.1", port=8000, reload=True)
