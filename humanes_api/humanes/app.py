import settings
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import ArgumentError
from humanes.domain.socies import Account
from humanes.infraestructure.database import SessionLocal

app = FastAPI()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to check the health of the API
@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/socies", response_model=list[Account])
def list_socies(db: Session = Depends(get_db)):
    try:
        accounts = db.query(Account).all()
        if not accounts:
            return {"error": "Account data not found."}
        return accounts
    except Exception:
        raise HTTPException(status_code=404, detail="Socies not found")
