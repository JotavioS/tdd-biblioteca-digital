import pytest
from src.livro import Livro


class TestLivro:
    """Testes para a classe Livro seguindo TDD"""
    
    def test_criar_livro_com_dados_validos(self):
        """RED: Teste que falha - criar livro com dados válidos"""
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