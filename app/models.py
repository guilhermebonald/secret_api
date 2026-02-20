from sqlalchemy import Column, Integer, String, Text
from database import Base

# Modelos para o SQLAlchemy, representando a tabela de segredos no banco de dados.


class Secret(Base):
    __tablename__ = "secrets"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    servico = Column(String, nullable=False)
    conteudo_criptografado = Column(Text, nullable=False)
