import cv2
#haar za zaznavanje obrazov od spredaj
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#shranjevanje videota od kamere v spremenljivko
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#spremenljivke za določanje ali se uporabi blur ali pa frame (gumb "b" za blur in "f" za okvir okoli zaznanega obraza)
blur = False
framed = False
#while zanka katera se prekini ko uporabnik pritisne tipko "q"
while True:
    open,frame = cap.read()
    if (open):
        #naredimo kopijo video frame-a kater je črnobel zato ker funkcija detectMultiScale deluje samo na črno bleih slikah
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #detectMultiScale funkcijo uporabimo da najdemo vse obraze v našem črno belem frame-u
        f = face.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors= 7)

        for x,y,w,h in f:
            #če je spremenljivka blur = True se čez najdene obraze da gaussian blur
            if blur:
                #označimo od "podobraza" okvir
                sub = frame[y:y+h , x:x+w]
                #čez njegov okvir dodamo gaussian blur
                sub = cv2.GaussianBlur(sub, (23, 23), 30)
                #združimo naš zamegljen okvir z našim originalnim frame-om
                frame[y:y+sub.shape[0], x:x+sub.shape[1]] = sub
            # če je spremenljivka framed = True se čez najdene obraze da okvir
            if framed:
                cv2.rectangle(frame, (x,y), (x+h,y+w),(0,255,0),2)
        #prikažemo kamero v novem oknu
        cv2.imshow('faceBlur', frame)
    ch = 0xFF &cv2.waitKey(1)
    if ch == ord("b"):
        blur = not blur
    if ch == ord("f"):
        framed = not framed
    if ch == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
