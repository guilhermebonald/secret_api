from pydantic import BaseModel
from typing import Optional


# Modelo de Entrada da API para criação de um novo segredo.
class SecretCreate(BaseModel):
    titulo: str
    servico: str
    conteudo: str


# Modelos de Entrada da Api para atualização dos dados.
class SecretUpdate(BaseModel):
    titulo: Optional[str] = None
    servico: Optional[str] = None
    conteudo: Optional[str] = None


# Modelo de Saída da API, incluindo o campo de ID e o conteúdo criptografado
class SecretResponse(BaseModel):
    id: int
    titulo: str
    servico: str
    conteudo: str

    class Config:
        from_attributes = True
