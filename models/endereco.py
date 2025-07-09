from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Endereco(Base):
    __tablename__ = "enderecos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("id_usuario", ForeignKey("usuarios.id"))
    rua = Column("rua", String)
    numero = Column("numero", Integer)
    bairro = Column("bairro", String)
    cidade = Column("cidade", String)
    estado = Column("estado", String)
    cep = Column("cep", String)
    complemento = Column("complemento", String)
    
    usuario = relationship("Usuario", back_populates="enderecos")
    
    def __init__(self, usuario:int, rua:str, numero:int, bairro:str,
                 cidade:str, estado:str, cep:str, complemento:str):
        self.usuario = usuario
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento
        