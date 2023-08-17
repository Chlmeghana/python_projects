import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=1)  # Create a hand detector with a confidence threshold
while True:
    ret, frame = cap.read()
    hands,frame = detector.findHands(frame)
    #cv2.rectangle(frame,(20,460),(70,460),(0,0,255),200)
    if hands:
        fing=detector.fingersUp(hands[0])
        if(fing==[0,0,0,0,0]):
            cv2.putText(frame,"brake",(20,460),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0, 255, 0),2,cv2.LINE_4)
            auto.press('up')
        elif(fing==[1,1,1,1,1]):
            cv2.putText(frame,"accelerate",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0, 255, 0),2,cv2.LINE_8)
    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
