# 🚨 OpenCV Motion-Based Intrusion Alarm

A lightweight Python + OpenCV security tool that detects motion in real-time,
captures intruder snapshots, and logs all security events with timestamps.

![Demo](demo.gif)

---

## 🔍 How It Works

The system captures a continuous webcam feed and applies **background subtraction**
to isolate moving objects from the static environment. When a moving contour
exceeds a defined pixel threshold, it triggers the alarm — saving a timestamped
snapshot and logging the event to a local file.

Key techniques used:
- `cv2.absdiff()` for frame differencing
- Contour detection via `cv2.findContours()`
- Automated image capture with `cv2.imwrite()`

---

## ⚙️ Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/smritiesharma/OpenCV_Motion-Based_Intrusion_Alarm.git
cd OpenCV_Motion-Based_Intrusion_Alarm
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the alarm**
```bash
python intrusion_alarm.py
```

> Make sure your webcam is connected. Press `Q` to quit.

---

## 📁 Output

- Captured images are saved in the `captured_images/` folder
- Each image is timestamped for audit trail purposes

---

## 🚀 Potential Extensions

- 🔔 **SMS/Email Alerts** — Integrate Twilio or SMTP to send real-time notifications
- 🧠 **Face Recognition** — Layer in `face_recognition` library to identify known vs unknown persons
- 📊 **Event Dashboard** — Build a simple Flask web UI to view the event log and snapshots
- 🌐 **IoT Integration** — Push alerts to a Raspberry Pi buzzer or LED system

---

## 🛠️ Built With

- Python 3.x
- OpenCV (`cv2`)

---

## 👤 Author

**Smritie Sharma**
B.Tech CSE (AIML) | IILM University
[GitHub](https://github.com/smritiesharma)
