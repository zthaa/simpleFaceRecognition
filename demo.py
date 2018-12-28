import cv2, os

path = r"D:\starlib"
count = 0
file_list = os.listdir(path)
for i in file_list:
    filepath = os.path.join(path, i)
    image_list = os.listdir(filepath)
    for i in image_list:
        imagepath = os.path.join(filepath, i)
        print(imagepath)
        # imagepath = r"D:\starlib\fuck0\0.jpg"
        image = cv2.imread(imagepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(r".\haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(5, 5)
        )
        if len(faces) == 0:
            newpath = os.getcwd() +"\\strlib"
            newname = os.path.join(newpath, str(count)+".jpg")
            os.renames(imagepath, newname)
            count += 1
# print("发现{0}个人脸".format(len(faces)))
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+w), (0, 255, 0), 2)
#
# cv2.imshow("picture", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()