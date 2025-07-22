# 🆔 Aadhaar Face Verification System (React + Node.js + Python)

A full-stack web application that verifies the identity of a user by extracting the face from their Aadhaar card (PDF) and comparing it with a live/selfie image using face recognition.

---

## 🔍 Features

- 📤 Upload Aadhaar PDF and selfie
- 🧠 Automatic face detection and matching
- 📑 Aadhaar PDF converted to image
- ✅ Returns match result and confidence score
- 🌐 Built with React (frontend), Node.js (backend), Python (for ML logic)

---

## 🛠 Tech Stack

| Layer       | Tech            |
|-------------|-----------------|
| Frontend    | React (Vite)    |
| Backend     | Node.js + Express |
| ML Logic    | Python (face_recognition, pdf2image) |
| File Upload | Multer          |

---

## 🚀 How It Works

1. User uploads:
   - Aadhaar card (PDF format)
   - A selfie or recent photo (JPG/PNG)
2. Backend sends files to a Python script
3. Python:
   - Converts Aadhaar PDF → image
   - Detects and encodes faces
   - Compares Aadhaar face with selfie
4. Returns result: ✅ Match / ❌ No Match + confidence score

