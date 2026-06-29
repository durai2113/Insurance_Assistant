"""Upload API endpoints for PDF ingestion."""

from fastapi import APIRouter, File, HTTPException, UploadFile, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.services.upload_service import process_pdf, save_pdf

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Store and process an uploaded PDF document."""

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    try:
        file_path = save_pdf(file)
        process_pdf(file_path, db, file.filename)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - defensive runtime guard
        raise HTTPException(
            status_code=500,
            detail="Failed to process the uploaded PDF.",
        ) from exc

    return {"message": "PDF uploaded and processed successfully."}
