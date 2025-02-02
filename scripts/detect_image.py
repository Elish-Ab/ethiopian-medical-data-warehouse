import torch
import os
import shutil
from PIL import Image

# Load the YOLOv5 model (pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'yolov5s' for speed (you can switch to 'yolov5m' or 'yolov5l' for accuracy)

# Create directories for storing medical and non-medical images if they don't exist
os.makedirs('medical_images', exist_ok=True)
os.makedirs('non_medical_images', exist_ok=True)

# Path to the 'photos' directory where images are stored
photos_dir = 'photos'

# Function to classify an image as 'medical' or 'non-medical'
def classify_image(image_path):
    # Load the image using PIL (it can be any image file)
    img = Image.open(image_path)

    # Run inference with YOLOv5 model
    results = model(img)

    # Print the results for debugging (optional)
    results.print()

    # Get the detected classes and confidence scores
    detected_classes = results.xyxy[0][:, -1].tolist()  # Detected class IDs
    confidence_scores = results.xyxy[0][:, -2].tolist()  # Confidence scores

    # Predefined list of class IDs that might be related to medical objects (you can adjust this based on your needs)
    # For simplicity, I will assume a few general medical-related objects, but you can fine-tune for more specific medical objects
    medical_class_ids = [1, 47, 53, 56]  # Example: [person, bottle, chair, clock] (these are just placeholders, replace with actual IDs)

    # Iterate over detected classes and confidence scores
    for detected_class, score in zip(detected_classes, confidence_scores):
        if detected_class in medical_class_ids and score > 0.5:  # Confidence threshold of 50%
            return 'medical'  # If a medical object is detected, classify as medical
    
    # If no medical-related objects found, classify as non-medical
    return 'non-medical'

# Function to classify all images in the photos directory
def classify_and_move_images():
    # Iterate through all the images in the photos directory
    for filename in os.listdir(photos_dir):
        file_path = os.path.join(photos_dir, filename)
        
        # Check if the file is an image (you can add more checks for other file types if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Classify the image (medical or non-medical)
            image_class = classify_image(file_path)
            
            # Define destination directories for medical and non-medical images
            if image_class == 'medical':
                destination = os.path.join('medical_images', filename)
            else:
                destination = os.path.join('non_medical_images', filename)
            
            # Move the image to the corresponding folder
            shutil.move(file_path, destination)
            print(f"Moved {filename} to {image_class} folder.")

if __name__ == "__main__":
    # Run the classification and move the images
    classify_and_move_images()
