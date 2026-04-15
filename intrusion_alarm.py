import cv2
import time
import os
from datetime import datetime

class IntrusionAlarm:
    def __init__(self, sensitivity=5000, cooldown=2.0):
        # Configuration
        self.sensitivity = sensitivity # Minimum contour area to trigger alarm
        self.cooldown = cooldown       # Seconds between saving snapshots
        self.last_snapshot_time = 0
        
        # Setup directories and files
        self.alerts_dir = "alerts"
        self.log_file = "log.txt"
        self._prepare_environment()

    def _prepare_environment(self):
        """Creates the alerts directory and initializes the log file if they don't exist."""
        if not os.path.exists(self.alerts_dir):
            os.makedirs(self.alerts_dir)
            print(f"[INFO] Created directory: {self.alerts_dir}/")
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write("--- Intrusion Alarm Log ---\n")

    def log_event(self, message):
        """Appends a timestamped message to the log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def run(self):
        """Main loop for capturing video and detecting motion."""
        print("[INFO] Starting webcam... Press 'q' to exit gracefully.")
        cap = cv2.VideoCapture(0)
        time.sleep(2.0) # Warm up the camera

        background_frame = None

        while True:
            ret, frame = cap.read()
            if not ret:
                print("[ERROR] Could not read from webcam.")
                break

            text_status = "Status: Secure"
            color_status = (0, 255, 0) # Green for secure
            motion_detected_this_frame = False

            # 1. Preprocessing: Grayscale and Gaussian Blur
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # 2. Background Initialization
            if background_frame is None:
                background_frame = gray
                continue

            # 3. Frame Differencing
            frame_delta = cv2.absdiff(background_frame, gray)

            # 4. Thresholding
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

            # 5. Dilation to fill in gaps
            thresh = cv2.dilate(thresh, None, iterations=2)

            # 6. Find Contours
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                # 7. Sensitivity Check
                if cv2.contourArea(contour) < self.sensitivity:
                    continue

                motion_detected_this_frame = True
                text_status = "Status: Movement Detected"
                color_status = (0, 0, 255) # Red for movement

                # 8. Draw Bounding Box
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 9. Trigger Alerts (Snapshot & Logging)
            current_time = time.time()
            if motion_detected_this_frame and (current_time - self.last_snapshot_time) > self.cooldown:
                timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_path = os.path.join(self.alerts_dir, f"intruder_{timestamp_str}.jpg")
                
                # Save snapshot
                cv2.imwrite(image_path, frame)
                print(f"[ALERT] Motion detected! Snapshot saved to {image_path}")
                
                # Log the event
                self.log_event("Motion detected. Snapshot saved.")
                
                self.last_snapshot_time = current_time

            # 10. Visual Output
            cv2.putText(frame, text_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_status, 2)
            cv2.imshow("Intrusion Alarm Feed", frame)

            # 11. Graceful Exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] 'q' pressed. Shutting down gracefully...")
                self.log_event("System shutdown gracefully.")
                break

        # Cleanup
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # You can tweak the sensitivity here. 
    # Lower = more sensitive (detects small things). Higher = less sensitive (ignores shadows).
    alarm = IntrusionAlarm(sensitivity=6000, cooldown=3.0)
    alarm.run()