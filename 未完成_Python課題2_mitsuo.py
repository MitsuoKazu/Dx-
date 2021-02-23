#★OpenCVライブラリを使用する
import cv2
#-------------------------------------
#★対象画像はプログラム実行時にパラメーターとして1枚指定する(途中）
import tkinter
import tkinter.filedialog as fd
root = tkinter.Tk()
root.withdraw()

# Fileのdialogを呼び出し、Pathを取得する

file_path = fd.askopenfilename()
#★対象画像が見つからない場合は、その旨を表示してプログラムを終了する
if not len(file_path) > 0:
    print("END")

#imageを読み込む
image = cv2.imread(file_path)
#-------------------------------------

#★★画像サイズを変える、いろんな画像で試す★★
#-------------------------------------

cascade_facefile = 'haarcascade_frontalface_alt.xml'
cascade_eyefile = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(cascade_facefile)
eye_cascade = cv2.CascadeClassifier(cascade_eyefile)



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))


for (x,y,w,h) in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#-------------------------------------       
#★処理を施した画像を表示する際に、画面の下部に「Press Esc to Exit」と表示する
fontType = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'Press Esc to Exit',(0,370), fontType, 1, (255, 255, 255), 3)

#-------------------------------------
#★元の画像は、プログラム実行後編集されていないこと
cv2.imwrite('./out.jpg', image)
cv2.imshow('./out.jpg', image)

#-------------------------------------
#★処理を施した画像の表示後、Escキーが押されたら画面を閉じる処理を行う
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

#-------------------------------------




