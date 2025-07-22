# face_match.py
import sys
from pdf2image import convert_from_path
import face_recognition
import os

def convert_pdf(pdf_path):
    pages = convert_from_path(pdf_path, 200)
    image_path = "uploads/aadhaar.jpg"
    pages[0].save(image_path, 'JPEG')
    return image_path

def compare_faces(aadhaar_img, selfie_img):
    try:
        aadhaar_face = face_recognition.load_image_file(aadhaar_img)
        selfie_face = face_recognition.load_image_file(selfie_img)

        aadhaar_enc = face_recognition.face_encodings(aadhaar_face)
        selfie_enc = face_recognition.face_encodings(selfie_face)

        if not aadhaar_enc or not selfie_enc:
            print("ERROR: Face not detected")
            return

        result = face_recognition.compare_faces([aadhaar_enc[0]], selfie_enc[0])
        distance = face_recognition.face_distance([aadhaar_enc[0]], selfie_enc[0])[0]

        if result[0]:
            print(f"PASS:{distance}")
        else:
            print(f"FAIL:{distance}")

    except Exception as e:
        print(f"ERROR:{str(e)}")

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    selfie_path = sys.argv[2]
    aadhaar_img = convert_pdf(pdf_path)
    compare_faces(aadhaar_img, selfie_path)
