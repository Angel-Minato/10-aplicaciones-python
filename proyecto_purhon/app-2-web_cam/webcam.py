import cv2, time, pandas
from datetime import datetime

firs_frame =None
status_list = [None,None]
times=[]
dt= pandas.DataFrame(columns=["Inico","Fin"])

video= cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not video.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()


while True:
    check, frame = video.read()
    status= 0
    if not check:
        print("No se puede capturar el frame. Verifica la cámara.")
        break

    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if firs_frame is None:
        firs_frame = gray
        continue


    delta_frame=cv2.absdiff(firs_frame,gray)

    thresh_frame=cv2.threshold(delta_frame,30,255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for count in cnts:
        if cv2.contourArea(count) < 10000:
            continue
        (x,y,w,h) = cv2.boundingRect(count)
        radio = int((x+h)/3)
        cv2.circle(frame, (x,y), radio, (255,0,0),2)

    status_list.append(status)

    if status_list[-1]== 1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]== 0 and status_list[-2]==1:
        times.append(datetime.now())

        
    cv2.imshow("captura", gray)
    cv2.imshow("no se delta algo",delta_frame)
    cv2.imshow("tre frame", thresh_frame)
    cv2.imshow("ciruclo frame", frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status ==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    dt = dt.append({"Inico":times[i],"Fin":times[i+1] },ignore_Index=True)

#dt.to_csv("Times.csv")    

video.release()
cv2.destroyAllWindows