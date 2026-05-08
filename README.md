# 🚦 Intelligent Traffic Analytics System

An AI-powered traffic analytics system built using **YOLOv8**, **Flask**, and **OpenCV** for real-time vehicle detection and traffic analysis.

The system detects and classifies vehicles from uploaded traffic images, generates bounding boxes with confidence scores, and provides live analytics such as vehicle counting.

---

## 🔗 Live Demo

https://YOUR_RENDER_LINK.onrender.com

---

## 📂 GitHub Repository

https://github.com/abhinav-singh0/intelligent-traffic-analytics-system

---

# ✨ Features

✅ Vehicle Detection using YOLOv8  
✅ Traffic Image Upload Interface  
✅ Bounding Box Visualization  
✅ Vehicle Classification  
✅ Vehicle Counting Analytics  
✅ Clean Flask Web Application  
✅ Responsive Modern UI  

---

# 🚘 Vehicle Classes

The system simplifies multiple traffic classes into three major categories:

- 🚗 Car
- 🚛 Truck
- 🚌 Bus

This improves:
- prediction consistency
- UI readability
- traffic analytics quality

---

# 🧠 How The System Works

## 1. Dataset Preparation

The original dataset was obtained from Kaggle traffic detection data.

TFRecord annotations were converted into YOLO annotation format using a custom preprocessing pipeline.

Dataset Source:

https://www.kaggle.com/code/quackaddict7/object-detection-detecting-vehicles-in-traffic

---

## 2. YOLOv8 Training

The model was trained using Ultralytics YOLOv8.

### Training Configuration

| Parameter | Value |
|---|---|
| Model | YOLOv8 Nano |
| Epochs | 50 |
| Image Size | 640 |
| Batch Size | 16 |

---

## 3. Detection Pipeline

The uploaded image passes through:

```text
Image Upload
      ↓
YOLOv8 Inference
      ↓
Bounding Box Detection
      ↓
Vehicle Class Mapping
      ↓
Analytics Generation
      ↓
Output Visualization
```

---

# 📊 Analytics

The system automatically computes:

- Total Cars
- Total Trucks
- Total Buses

This transforms the project from a simple detector into an intelligent traffic analytics application.

---

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Flask |
| Deep Learning | YOLOv8 |
| Computer Vision | OpenCV |
| ML Framework | PyTorch |
| Frontend | HTML, CSS |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
intelligent-traffic-analytics-system/
│
├── app.py
├── best.pt
├── requirements.txt
├── Procfile
├── .python-version
├── .gitignore
│
├── static/
│   ├── uploads/
│   └── outputs/
│
├── templates/
│   └── index.html
│
└── utils/
    └── detector.py
```

---

# 🚀 Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/abhinav-singh0/intelligent-traffic-analytics-system.git

cd intelligent-traffic-analytics-system
```

---

## 2. Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📸 Sample Output

The system generates:

- vehicle bounding boxes
- confidence scores
- analytics dashboard

Example:

```text
Cars: 5
Trucks: 2
Buses: 1
```

---

# 📈 Future Improvements

- Real-time video analytics
- Vehicle tracking
- Speed estimation
- Traffic density monitoring
- Multi-camera support
- DeepSORT / ByteTrack integration

---

# 🎓 Academic Context

This project was developed as part of the **Computer Vision** course at:

**Indian Institute of Technology Dharwad**

The project was carried out under the supervision of:

**Dr. Shashaank Aswatha Mattur**
---

# 🙏 Acknowledgements

- Ultralytics YOLOv8
- Kaggle traffic dataset
- OpenCV
- Flask
- PyTorch

---

# 📧 Contact

### Abhinav Singh
Indian Institute of Technology Dharwad

📧 ee25mt010@iitdh.ac.in

GitHub:
https://github.com/abhinav-singh0
