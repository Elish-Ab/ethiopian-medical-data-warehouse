import torch
import os
import shutil
from PIL import Image
import logging
from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(filename='detection.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DB_URL = 'postgresql://postgres:elish@localhost:5432/telegram_data_db'
engine = create_engine(DB_URL)
metadata = MetaData()

# Define the detection_results table
detection_results = Table(
    'detection_results', metadata,
    Column('id', Integer, primary_key=True),
    Column('image_name', String),
    Column('class_label', String),
    Column('confidence', Float),
    Column('x_min', Float),
    Column('y_min', Float),
    Column('x_max', Float),
    Column('y_max', Float)
)
metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Directory paths
photos_dir = 'photos'

# Function to process image detections
def process_image(image_path):
    try:
        img = Image.open(image_path)
        results = model(img)
        detections = results.xyxy[0].tolist()  # Extract detection details
        
        with Session() as session:
            for detection in detections:
                x_min, y_min, x_max, y_max, confidence, class_id = detection
                class_label = results.names[int(class_id)]
                
                # Insert detection results into the database
                insert_query = detection_results.insert().values(
                    image_name=os.path.basename(image_path),
                    class_label=class_label,
                    confidence=confidence,
                    x_min=x_min,
                    y_min=y_min,
                    x_max=x_max,
                    y_max=y_max
                )
                session.execute(insert_query)
            session.commit()

        logging.info(f"Processed {image_path} with {len(detections)} detections.")
    except Exception as e:
        logging.error(f"Error processing {image_path}: {e}")

# Function to process all images
def process_all_images():
    for filename in os.listdir(photos_dir):
        file_path = os.path.join(photos_dir, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            process_image(file_path)

if __name__ == "__main__":
    process_all_images()
