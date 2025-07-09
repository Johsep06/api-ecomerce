from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Carrinho(Base):
    __tablename__ = "carrinhos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_usuario = Column("id_usuario", Integer, ForeignKey("usuarios.id"))
    valor_total = Column("valor_total", Float, default=0)
    data_pedido = Column("data_pedido", DateTime)
    
    usuario = relationship("Usuario", back_populates="carrinhos")
    itens = relationship("ItemCarrinho", back_populates="carrinhos", cascade="all, delete")
    
    def __init__(self, id_usuario:int):
        self.id_usuario = id_usuario