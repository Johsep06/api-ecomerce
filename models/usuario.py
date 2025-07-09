from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=True, unique=True)
    senha = Column("senha", String, nullable=True)
    admin = Column("admin", Boolean, default=False)

    enderecos = relationship("Endereco", back_populates="usuario", cascade="all, delete")
    carrinhos = relationship("Carrinho", back_populates="usuario")
    comentarios = relationship("Comentarios", back_populates="usuario")
    
    def __init__(self, nome:str, email: str, senha:str, admin:bool=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
        