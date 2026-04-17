from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.s3_service import upload_file_to_s3

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    result = upload_file_to_s3(file.file, file.filename)

    return {
        "message": "File uploaded successfully",
        "file_name": file.filename,
        "s3_details": result
    }