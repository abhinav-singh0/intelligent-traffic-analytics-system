from ultralytics import YOLO
import cv2
import os

# Load trained YOLO model
model = YOLO("best.pt")


def detect_vehicles(image_path):

    # Run prediction
    results = model.predict(source=image_path, conf=0.5,imgsz=320)

    result = results[0]

    # Vehicle counters
    car_count = 0
    truck_count = 0
    bus_count = 0

    # Original class names
    names = model.names

    # Process detections
    for box in result.boxes:

        class_id = int(box.cls[0])
        class_name = names[class_id].lower()

        # Merge classes
        if "car" in class_name:
            new_label = "car"
            car_count += 1

        elif "bus" in class_name:
            new_label = "bus"
            bus_count += 1

        else:
            new_label = "truck"
            truck_count += 1

        # Bounding box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Confidence
        conf = float(box.conf[0])

        # Draw rectangle
        cv2.rectangle(
            result.orig_img,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Draw label
        label = f"{new_label} {conf:.2f}"

        cv2.putText(
            result.orig_img,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Output path
    output_path = os.path.join(
        "static/outputs",
        os.path.basename(image_path)
    )

    # Save output image
    cv2.imwrite(output_path, result.orig_img)

    # Analytics dictionary
    analytics = {
        "cars": car_count,
        "trucks": truck_count,
        "buses": bus_count
    }

    return output_path, analytics
