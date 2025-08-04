from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

router = APIRouter(prefix="/api/forms", tags=["forms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/wheel-specifications")
def create_wheel_spec(spec: schemas.WheelSpecificationSchema, db: Session = Depends(get_db)):
    new_spec = models.WheelSpecification(**spec.dict())
    db.add(new_spec)
    db.commit()
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": spec.formNumber,
            "submittedBy": spec.submittedBy,
            "submittedDate": spec.submittedDate,
            "status": "Saved"
        }
    }

@router.get("/wheel-specifications")
def get_filtered_wheel_specs(formNumber: str, submittedBy: str, submittedDate: str, db: Session = Depends(get_db)):
    spec = db.query(models.WheelSpecification).filter_by(
        formNumber=formNumber,
        submittedBy=submittedBy,
        submittedDate=submittedDate
    ).first()
    if not spec:
        raise HTTPException(status_code=404, detail="Specification not found")
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [spec.__dict__]
    }

@router.post("/bogie-checksheet")
def create_bogie_form(data: schemas.BogieChecksheetSchema, db: Session = Depends(get_db)):
    new_bogie = models.BogieChecksheet(**data.dict())
    db.add(new_bogie)
    db.commit()
    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": data.formNumber,
            "inspectionBy": data.inspectionBy,
            "inspectionDate": data.inspectionDate,
            "status": "Saved"
        }
    }
