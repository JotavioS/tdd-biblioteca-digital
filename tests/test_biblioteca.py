from src.biblioteca import Biblioteca
from src.livro import Livro
from src.usuario import Usuario


class TestBiblioteca:
    """Testes para a classe Biblioteca seguindo TDD"""

    def test_criar_biblioteca(self):
        """RED: Teste que falha - criar biblioteca"""
        # Act
        biblioteca = Biblioteca()

        # Assert
        assert biblioteca.livros == []
        assert biblioteca.usuarios == []
        assert biblioteca.emprestimos == []

    def test_adicionar_livro(self):
        """RED: Teste que falha - adicionar livro à biblioteca"""
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")

        # Act
        biblioteca.adicionar_livro(livro)

        # Assert
        assert len(biblioteca.livros) == 1
        assert biblioteca.livros[0] == livro

    def test_adicionar_usuario(self):
        """RED: Teste que falha - adicionar usuário à biblioteca"""
        # Arrange
        biblioteca = Biblioteca()
        usuario = Usuario(nome="João Silva", email="joao@email.com")

        # Act
        biblioteca.adicionar_usuario(usuario)

        # Assert
        assert len(biblioteca.usuarios) == 1
        assert biblioteca.usuarios[0] == usuario

    def test_emprestar_livro_sucesso(self):
        """RED: Teste que falha - emprestar livro com sucesso"""
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        usuario = Usuario(nome="João Silva", email="joao@email.com")
        biblioteca.adicionar_livro(livro)
        biblioteca.adicionar_usuario(usuario)

        # Act
        resultado = biblioteca.emprestar_livro(livro.id, usuario.id)

        # Assert
        assert resultado is True
        assert livro.disponivel is False
        assert len(biblioteca.emprestimos) == 1
        assert biblioteca.emprestimos[0]["livro_id"] == livro.id
        assert biblioteca.emprestimos[0]["usuario_id"] == usuario.id

    def test_emprestar_livro_indisponivel(self):
        """RED: Teste que falha - tentar emprestar livro já emprestado"""
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        usuario1 = Usuario(nome="João Silva", email="joao@email.com")
        usuario2 = Usuario(nome="Maria Santos", email="maria@email.com")
        biblioteca.adicionar_livro(livro)
        biblioteca.adicionar_usuario(usuario1)
        biblioteca.adicionar_usuario(usuario2)
        biblioteca.emprestar_livro(livro.id, usuario1.id)

        # Act
        resultado = biblioteca.emprestar_livro(livro.id, usuario2.id)

        # Assert
        assert resultado is False
        assert len(biblioteca.emprestimos) == 1

    def test_devolver_livro_sucesso(self):
        """RED: Teste que falha - devolver livro emprestado"""
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        usuario = Usuario(nome="João Silva", email="joao@email.com")
        biblioteca.adicionar_livro(livro)
        biblioteca.adicionar_usuario(usuario)
        biblioteca.emprestar_livro(livro.id, usuario.id)

        # Act
        resultado = biblioteca.devolver_livro(livro.id, usuario.id)

        # Assert
        assert resultado is True
        assert livro.disponivel is True
        assert biblioteca.emprestimos[0]["data_devolucao"] is not None

    def test_devolver_livro_nao_emprestado(self):
        """RED: Teste que falha - tentar devolver livro não emprestado"""
        # Arrange
        biblioteca = Biblioteca()
        livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
        usuario = Usuario(nome="João Silva", email="joao@email.com")
        biblioteca.adicionar_livro(livro)
        biblioteca.adicionar_usuario(usuario)

        # Act
        resultado = biblioteca.devolver_livro(livro.id, usuario.id)

        # Assert
        assert resultado is False
