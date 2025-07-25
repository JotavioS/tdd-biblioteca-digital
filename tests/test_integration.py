import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, LivroModel, UsuarioModel, EmprestimoModel
from src.biblioteca_db import BibliotecaDB


class TestIntegrationBiblioteca:
    """Testes de integração com banco de dados seguindo TDD"""
    
    @pytest.fixture
    def setup_db(self):
        """Setup do banco de dados de teste"""
        # Criar banco de dados em memória para testes
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        db = SessionLocal()
        biblioteca_db = BibliotecaDB(db)
        
        yield biblioteca_db, db
        
        db.close()
    
    def test_salvar_livro_no_banco(self, setup_db):
        """RED: Teste que falha - salvar livro no banco de dados"""
        biblioteca_db, db = setup_db
        
        # Arrange
        livro_data = {
            'titulo': '1984',
            'autor': 'George Orwell',
            'isbn': '978-0451524935'
        }
        
        # Act
        livro_id = biblioteca_db.criar_livro(livro_data)
        
        # Assert
        assert livro_id is not None
        livro_salvo = db.query(LivroModel).filter(LivroModel.id == livro_id).first()
        assert livro_salvo is not None
        assert livro_salvo.titulo == '1984'
        assert livro_salvo.autor == 'George Orwell'
        assert livro_salvo.isbn == '978-0451524935'
        assert livro_salvo.disponivel is True
    
    def test_salvar_usuario_no_banco(self, setup_db):
        """RED: Teste que falha - salvar usuário no banco de dados"""
        biblioteca_db, db = setup_db
        
        # Arrange
        usuario_data = {
            'nome': 'João Silva',
            'email': 'joao@email.com'
        }
        
        # Act
        usuario_id = biblioteca_db.criar_usuario(usuario_data)
        
        # Assert
        assert usuario_id is not None
        usuario_salvo = db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
        assert usuario_salvo is not None
        assert usuario_salvo.nome == 'João Silva'
        assert usuario_salvo.email == 'joao@email.com'
    
    def test_emprestar_livro_com_banco(self, setup_db):
        """RED: Teste que falha - emprestar livro usando banco de dados"""
        biblioteca_db, db = setup_db
        
        # Arrange
        livro_data = {'titulo': '1984', 'autor': 'George Orwell', 'isbn': '978-0451524935'}
        usuario_data = {'nome': 'João Silva', 'email': 'joao@email.com'}
        
        livro_id = biblioteca_db.criar_livro(livro_data)
        usuario_id = biblioteca_db.criar_usuario(usuario_data)
        
        # Act
        emprestimo_id = biblioteca_db.emprestar_livro(livro_id, usuario_id)
        
        # Assert
        assert emprestimo_id is not None
        
        # Verificar se o livro foi marcado como indisponível
        livro = db.query(LivroModel).filter(LivroModel.id == livro_id).first()
        assert livro.disponivel is False
        
        # Verificar se o empréstimo foi registrado
        emprestimo = db.query(EmprestimoModel).filter(EmprestimoModel.id == emprestimo_id).first()
        assert emprestimo is not None
        assert emprestimo.livro_id == livro_id
        assert emprestimo.usuario_id == usuario_id
        assert emprestimo.data_devolucao is None