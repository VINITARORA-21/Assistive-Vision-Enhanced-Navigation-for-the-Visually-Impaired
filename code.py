import cv2
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound


model = YOLO(r"C:\Users\vinit\OneDrive\Desktop\best.pt")

l = "en-GB"
green_light_text = "Green light detected. It is safe to cross the road now."
green_light_speech = gTTS(text=green_light_text, lang=l, slow=False, tld="com.au")
green_light_speech.save(r'C:\Users\vinit\OneDrive\Desktop\greenllight.mp3')


cap = cv2.VideoCapture(0)


while cap.isOpened():
    
    success, frame = cap.read()

    if success:
        
        results = model(frame)

       
        crosswalk_detected = False
        for r in results:
            for c in r.boxes.cls:
                if r.names[int(c)] == "crosswalk":
                    crosswalk_detected = True
                    break
       
         
        if crosswalk_detected:
            green_light_detected = False
            for r in results:
                for c in r.boxes.cls:
                    if r.names[int(c)] == "green":
                        green_light_detected = True
                        break
           
            
            if green_light_detected:
                playsound(r'C:\Users\vinit\OneDrive\Desktop\greenllight.mp3')
       
        
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        
        break

cap.release()
cv2.destroyAllWindows()
