from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/secrets", response_model=schemas.SecretResponse)
def create_secret(secret: schemas.SecretCreate, db: Session = Depends(get_db)):
    db_secret = models.Secret(
        titulo=secret.titulo,
        servico=secret.servico,
        conteudo_criptografado=secret.conteudo,  # Adicionar a lógica de criptografia
    )
    db.add(db_secret)
    db.commit()
    db.refresh(db_secret)
    return db_secret


@app.get("/secrets", response_model=list[schemas.SecretResponse])
def list_secrets(db: Session = Depends(get_db)):
    return db.query(models.Secret).all()


@app.get("/secrets/{secret_id}", response_model=schemas.SecretResponse)
def get_secret(secret_id: int, db: Session = Depends(get_db)):
    secret = db.query(models.Secret).filter(models.Secret.id == secret_id).first()
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    return secret


@app.delete("/secrets/{secret_id}", response_model=schemas.SecretResponse)
def delete_secret(secret_id: int, db: Session = Depends(get_db)):
    secret = db.query(models.Secret).filter(models.Secret.id == secret_id).first()
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")
    db.delete(secret)
    db.commit()
    return {"detail": "Secret deleted"}


@app.patch("/secrets/{secret_id}", response_model=schemas.SecretResponse)
def update_secret(
    secret_id: int, secret_update: schemas.SecretUpdate, db: Session = Depends(get_db)
):
    secret = db.query(models.Secret).filter(models.Secret.id == secret_id).first()
    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")

    if secret_update.titulo is not None:
        secret.titulo = secret_update.titulo
    if secret_update.servico is not None:
        secret.servico = secret_update.servico
    if secret_update.conteudo is not None:
        secret.conteudo_criptografado = (
            secret_update.conteudo
        )  # Adicionar a lógica de criptografia

    db.commit()
    db.refresh(secret)
    return secret
