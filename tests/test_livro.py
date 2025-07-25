import pytest
from src.livro import Livro
from pydantic import ValidationError


class TestLivro:
    """Testes para a classe Livro seguindo TDD"""
    
    def test_criar_livro_com_dados_validos(self):
        """GREEN: Teste que passa - criar livro com dados válidos"""
        # Arrange
        titulo = "1984"
        autor = "George Orwell"
        isbn = "978-0451524935"
        
        # Act
        livro = Livro(titulo=titulo, autor=autor, isbn=isbn)
        
        # Assert
        assert livro.titulo == titulo
        assert livro.autor == autor
        assert livro.isbn == isbn
        assert livro.disponivel is True
        assert livro.id is not None
    
    def test_criar_livro_sem_titulo_deve_falhar(self):
        """RED: Teste que falha - criar livro sem título"""
        # Arrange
        autor = "George Orwell"
        isbn = "978-0451524935"
        
        # Act & Assert
        with pytest.raises(ValidationError):
            Livro(autor=autor, isbn=isbn)
    
    def test_emprestar_livro_disponivel(self):
        """RED: Teste que falha - emprestar livro disponível"""
        # Arrange
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        
        # Act
        resultado = livro.emprestar()
        
        # Assert
        assert resultado is True
        assert livro.disponivel is False
    
    def test_emprestar_livro_indisponivel(self):
        """RED: Teste que falha - emprestar livro já emprestado"""
        # Arrange
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        livro.emprestar()
        
        # Act
        resultado = livro.emprestar()
        
        # Assert
        assert resultado is False
        assert livro.disponivel is False