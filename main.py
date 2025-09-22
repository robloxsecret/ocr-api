from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

app = FastAPI(title="OCR API", description="Extrahiert Text aus Bildern", version="1.0")

@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image, lang="deu+eng")  # Deutsch + Englisch
        return {"text": text.strip()}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
async def root():
    return {"message": "OCR API läuft! Sende ein Bild an /extract_text"}
