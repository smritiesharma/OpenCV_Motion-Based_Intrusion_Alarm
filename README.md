# 🚨 OpenCV Motion-Based Intrusion Alarm

A lightweight, real-time computer vision script that uses your webcam to detect motion, log security events, and capture snapshots of potential intruders. Built using Python and OpenCV.

## 💡 The "Hostel" Use Case
This tool was built with practical security in mind. It's the perfect zero-cost solution for keeping an eye on your university hostel room door while you're away attending classes or grabbing lunch. Just point your laptop camera at the door, run the script, and let it quietly monitor your space.

![Intrusion Alarm Demonstration](demo.gif)

## ✨ Features
* **Motion Tracking:** Highlights moving objects with real-time green bounding boxes.
* **Adjustable Sensitivity:** Easily tweak the contour threshold to ignore false positives like moving shadows or ceiling fans.
* **Automated Snapshots:** Captures and saves a `.jpg` image of the intruder directly to an `/alerts` folder the moment motion is detected.
* **Persistent Logging:** Writes every detection event with an exact timestamp to a `log.txt` file for auditing.
* **Graceful Exit:** Safely releases camera hardware and shuts down processes with a simple keystroke.

## 🛠️ How it Works
The system relies on a classic background-subtraction pipeline:
1. **Initialization:** The script captures the first frame as a static "background" reference.
2. **Differencing & Thresholding:** It constantly compares new frames against the background. Using absolute differencing and binary thresholding, it isolates areas of the image that have significantly changed.
3. **Dilation & Contours:** The algorithm uses dilation to close gaps in the detected motion mask, then draws mathematical contours around the moving objects.
4. **Logic Gate:** If the contour area exceeds the predefined `sensitivity` threshold, the alarm triggers.

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/OpenCV_Motion-Based_Intrusion_Alarm.git](https://github.com/smritiesharma/OpenCV_Motion-Based_Intrusion_Alarm.git)
   cd OpenCV_Motion-Based_Intrusion_Alarm

2. **Install dependencies:**
   ```bash
    pip install opencv-python numpy

3. **Run the script:**
   ```bash
   python intrusion_alarm.py
  (Note: If you are on Windows and the standard command doesn't work, use the Python launcher: py intrusion_alarm.py)

4. **Shutdown:**
  Press the q key while focused on the video window to safely exit the application and save the final logs.
