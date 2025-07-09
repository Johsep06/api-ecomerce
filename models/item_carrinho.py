from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class ItemCarrinho(Base):
    __tablename__ = "itens_carrinho"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_carrinho = Column("id_carrinho", Integer, ForeignKey("carrinhos.id"))
    id_produto = Column("id_produto", Integer, ForeignKey("produtos.id"))
    quantidade = Column("quantidade", Integer)
    preco_unitario = Column("preco_unitario", Float)
    
    carrinho = relationship("Carrinho", back_populates="itens_carrinho")
    produto = relationship("Produto", back_populates="itens_carrinho")

    def __init__(self, id_carrinho:int, id_produto:int, quantidade:int):
        self.id_carrinho = id_carrinho
        self.id_produto = id_produto
        self.quantidade = quantidade