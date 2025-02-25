from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from app.database import get_db
from app.models.company import Company
import json

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    responses={404: {"description": "Hittades inte"}},
)


# Pydantic-modeller för validering
class CompanyBase(BaseModel):
    name: str
    contact_info: str
    configuration: Optional[dict] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyResponse(CompanyBase):
    company_id: int

    class Config:
        orm_mode = True


# Hämta alla företag
@router.get("/", response_model=List[CompanyResponse])
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = db.query(Company).offset(skip).limit(limit).all()
    return companies


# Hämta specifikt företag
@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.company_id == company_id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Företag hittades inte")
    return company


# Skapa företag
@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(
        name=company.name,
        contact_info=company.contact_info,
        configuration=company.configuration,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
