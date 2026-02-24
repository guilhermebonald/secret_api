from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from security import encrypt_data, decrypt_data

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
    encrypted_content = encrypt_data(secret.conteudo)

    db_secret = models.Secret(
        titulo=secret.titulo,
        servico=secret.servico,
        conteudo_criptografado=encrypted_content,
    )
    db.add(db_secret)
    db.commit()
    db.refresh(db_secret)

    return schemas.SecretResponse(
        id=db_secret.id,
        titulo=db_secret.titulo,
        servico=db_secret.servico,
        conteudo=db_secret.conteudo_criptografado,
    )


@app.get("/secrets", response_model=list[schemas.SecretResponse])
def list_secrets(db: Session = Depends(get_db)):
    """
    Lista todos os segredos com conteúdo criptografado.
    """
    secrets = db.query(models.Secret).all()

    result = []
    for secret in secrets:
        # Descriptografa o conteúdo
        conteudo_descriptografado = decrypt_data(secret.conteudo_criptografado)

        response = schemas.SecretResponse(
            id=secret.id,
            titulo=secret.titulo,
            servico=secret.servico,
            conteudo=conteudo_descriptografado,
        )
        result.append(response)

    return result


@app.get("/secrets/{secret_id}", response_model=schemas.SecretResponse)
def get_secret(secret_id: int, db: Session = Depends(get_db)):
    secret = db.query(models.Secret).filter(models.Secret.id == secret_id).first()

    if not secret:
        raise HTTPException(status_code=404, detail="Secret not found")

    decrypted_content = decrypt_data(secret.conteudo_criptografado)

    return schemas.SecretResponse(
        id=secret.id,
        titulo=secret.titulo,
        servico=secret.servico,
        conteudo=decrypted_content,
    )


@app.delete("/secrets/{secret_id}", status_code=204)
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
        secret.conteudo_criptografado = encrypt_data(secret_update.conteudo)

    db.commit()
    db.refresh(secret)

    conteudo_descriptografado = decrypt_data(secret.conteudo_criptografado)

    return schemas.SecretResponse(
        id=secret.id,
        titulo=secret.titulo,
        servico=secret.servico,
        conteudo=conteudo_descriptografado,
    )
