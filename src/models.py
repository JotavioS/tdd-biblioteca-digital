from sqlalchemy import create_engine, Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import uuid

Base = declarative_base()

class LivroModel(Base):
    __tablename__ = 'livros'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    disponivel = Column(Boolean, default=True)
    
    emprestimos = relationship("EmprestimoModel", back_populates="livro")

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    emprestimos = relationship("EmprestimoModel", back_populates="usuario")

class EmprestimoModel(Base):
    __tablename__ = 'emprestimos'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    livro_id = Column(String, ForeignKey('livros.id'), nullable=False)
    usuario_id = Column(String, ForeignKey('usuarios.id'), nullable=False)
    data_emprestimo = Column(DateTime, default=datetime.now)
    data_devolucao = Column(DateTime, nullable=True)
    
    livro = relationship("LivroModel", back_populates="emprestimos")
    usuario = relationship("UsuarioModel", back_populates="emprestimos")

# Configuração do banco de dados
engine = create_engine('sqlite:///biblioteca.db', echo=False)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()