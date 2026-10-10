import cv2
def edit_image():
 p=input("Image path: ").strip().strip('"');i=cv2.imread(p)
 if i is None:print("Could not open image.");return
 while True:
  cv2.imshow("Image Editor",i);k=cv2.waitKey(0)&255
  if k==ord("r"):i=cv2.rotate(i,cv2.ROTATE_90_CLOCKWISE)
  elif k==ord("c"):
   x,y,w,h=cv2.selectROI("Crop",i,False,False);cv2.destroyWindow("Crop")
   if w and h:i=i[y:y+h,x:x+w]
  elif k in (ord("+"),ord("=")):i=cv2.add(i,(20,20,20,0))
  elif k==ord("-"):i=cv2.subtract(i,(20,20,20,0))
  elif k==ord("s"):
   p=input("Save path: ").strip().strip('"') or "edited_image.jpg";print("Saved." if cv2.imwrite(p,i) else "Could not save image.")
  elif k in (ord("q"),27):break
 cv2.destroyAllWindows()
def track_faces():
 c=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
 if c.empty():print("Could not load face detector.");return
 cam=cv2.VideoCapture(0)
 if not cam.isOpened():print("Could not open webcam.");return
 while True:
  ok,f=cam.read()
  if not ok:break
  g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY);faces=c.detectMultiScale(g,1.1,5)
  for x,y,w,h in faces:cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),2)
  cv2.putText(f,f"Faces in view: {len(faces)}",(20,35),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2);cv2.imshow("Live Face Tracking",f)
  if cv2.waitKey(1)&255 in (ord("q"),27):break
 cam.release();cv2.destroyAllWindows()
def main():
 c=input("1. Edit image  2. Track faces: ").strip()
 if c=="1":edit_image()
 elif c=="2":track_faces()
 else:print("Choose 1 or 2.")
if __name__=="__main__":main()
