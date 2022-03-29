import cv2
import face_recognition as fr

cap = cv2. VideoCapture(0)

model = load_model("model.hdf5")
predicted_class = np.argmax(model.predict(face_image)