from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from humanes.domain.socies import Account
from humanes.infraestructure.database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to check the health of the API
@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/")
def home():
    return "Humanes API de Socies"

@app.get("/socies", response_model=list[Account])
def list_socies(db: Session = Depends(get_db)):
    try:
        accounts = db.query(Account).all()
        if not accounts:
            return {"error": "Account data not found."}
        return accounts
    except Exception:
        raise HTTPException(status_code=404, detail="Socies not found")


@app.get("/socies/get_status/{socie_id}")
def get_status(db: Session = Depends(get_db)):
    return {
        "account_data": {
            "name": "Gideon",
            "last_name": "Nav",
            "venture": "",
            "dni": "1234",
            "zip_code": "234",
            "address": "ninth house",
            "phone": "1234",
            "email": "gideon_rocks@theninth.com",
        },
        "socie_type": "humane",
        "fees": None,
        "invoices": None,
        "activated": False,
        "socie": True,
        "provider": False,
    }
