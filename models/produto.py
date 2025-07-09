from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from database import Base

class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    descricao = Column("descricao", String)
    preco_unitario = Column("preco_unitario", Float)
    imagem_path = Column("imagem_path", String)
    
    comentarios = relationship("Comentario", back_populates="produto", cascade="all, delete")
    itens = relationship("ItemCarrinho", back_populates="produto")
    
    def __init__(self, titulo:str, descricao:str, preco_unitario:float, imagem_path:str):
        self.titulo = titulo
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.imagem_path = imagem_path