import pytest
from pydantic import ValidationError

from src.usuario import Usuario


class TestUsuario:
    """Testes para a classe Usuario seguindo TDD"""

    def test_criar_usuario_com_dados_validos(self):
        """RED: Teste que falha - criar usuário com dados válidos"""
        # Arrange
        nome = "João Silva"
        email = "joao@email.com"

        # Act
        usuario = Usuario(nome=nome, email=email)

        # Assert
        assert usuario.nome == nome
        assert usuario.email == email
        assert usuario.id is not None
        assert usuario.livros_emprestados == []

    def test_criar_usuario_sem_nome_deve_falhar(self):
        """RED: Teste que falha - criar usuário sem nome"""
        # Arrange
        email = "joao@email.com"

        # Act & Assert
        with pytest.raises(ValidationError):
            Usuario(email=email)

    def test_criar_usuario_sem_email_deve_falhar(self):
        """RED: Teste que falha - criar usuário sem email"""
        # Arrange
        nome = "João Silva"

        # Act & Assert
        with pytest.raises(ValidationError):
            Usuario(nome=nome)
