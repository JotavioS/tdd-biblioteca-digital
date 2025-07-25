#!/usr/bin/env python3
"""
Sistema de Empréstimo de Livros - Biblioteca Digital
Desenvolvido seguindo metodologia TDD (Test-Driven Development)
"""

from src.biblioteca import Biblioteca
from src.biblioteca_db import BibliotecaDB
from src.livro import Livro
from src.models import SessionLocal, get_db
from src.usuario import Usuario


def demonstrar_sistema_memoria():
    """Demonstra o funcionamento do sistema em memória"""
    print("=== Sistema de Biblioteca em Memória ===")

    # Criar biblioteca
    biblioteca = Biblioteca()

    # Criar livros
    livro1 = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
    livro2 = Livro(
        titulo="Dom Casmurro", autor="Machado de Assis", isbn="978-8525406958"
    )

    # Criar usuários
    usuario1 = Usuario(nome="João Silva", email="joao@email.com")
    usuario2 = Usuario(nome="Maria Santos", email="maria@email.com")

    # Adicionar à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_usuario(usuario1)
    biblioteca.adicionar_usuario(usuario2)

    print(f"Livros cadastrados: {len(biblioteca.livros)}")
    print(f"Usuários cadastrados: {len(biblioteca.usuarios)}")

    # Emprestar livro
    resultado = biblioteca.emprestar_livro(livro1.id, usuario1.id)
    print(f"Empréstimo realizado: {resultado}")
    print(f"Livro '{livro1.titulo}' disponível: {livro1.disponivel}")
    print(f"Empréstimos ativos: {len(biblioteca.emprestimos)}")

    # Tentar emprestar livro já emprestado
    resultado2 = biblioteca.emprestar_livro(livro1.id, usuario2.id)
    print(f"Tentativa de emprestar livro já emprestado: {resultado2}")

    # Devolver livro
    resultado3 = biblioteca.devolver_livro(livro1.id, usuario1.id)
    print(f"Devolução realizada: {resultado3}")
    print(f"Livro '{livro1.titulo}' disponível após devolução: {livro1.disponivel}")

    print()


def demonstrar_sistema_banco():
    """Demonstra o funcionamento do sistema com banco de dados"""
    print("=== Sistema de Biblioteca com Banco de Dados ===")

    # Criar sessão do banco
    db = SessionLocal()
    biblioteca_db = BibliotecaDB(db)

    try:
        # Criar livros
        livro1_id = biblioteca_db.criar_livro(
            {
                "titulo": "O Senhor dos Anéis",
                "autor": "J.R.R. Tolkien",
                "isbn": "978-8533613379",
            }
        )

        livro2_id = biblioteca_db.criar_livro(
            {
                "titulo": "Harry Potter e a Pedra Filosofal",
                "autor": "J.K. Rowling",
                "isbn": "978-8532511010",
            }
        )

        # Criar usuários
        usuario1_id = biblioteca_db.criar_usuario(
            {"nome": "Ana Costa", "email": "ana@email.com"}
        )

        usuario2_id = biblioteca_db.criar_usuario(
            {"nome": "Pedro Oliveira", "email": "pedro@email.com"}
        )

        print(f"Livro 1 criado com ID: {livro1_id}")
        print(f"Livro 2 criado com ID: {livro2_id}")
        print(f"Usuário 1 criado com ID: {usuario1_id}")
        print(f"Usuário 2 criado com ID: {usuario2_id}")

        # Emprestar livro
        emprestimo_id = biblioteca_db.emprestar_livro(livro1_id, usuario1_id)
        print(f"Empréstimo criado com ID: {emprestimo_id}")

        # Listar livros disponíveis
        livros_disponiveis = biblioteca_db.listar_livros_disponiveis()
        print(f"Livros disponíveis: {len(livros_disponiveis)}")
        for livro in livros_disponiveis:
            print(f"  - {livro.titulo} por {livro.autor}")

        # Listar empréstimos ativos
        emprestimos_ativos = biblioteca_db.listar_emprestimos_ativos()
        print(f"Empréstimos ativos: {len(emprestimos_ativos)}")

        # Devolver livro
        devolucao = biblioteca_db.devolver_livro(livro1_id, usuario1_id)
        print(f"Devolução realizada: {devolucao}")

        # Verificar livros disponíveis após devolução
        livros_disponiveis_apos = biblioteca_db.listar_livros_disponiveis()
        print(f"Livros disponíveis após devolução: {len(livros_disponiveis_apos)}")

    finally:
        db.close()

    print()


def main():
    """Função principal"""
    print("Sistema de Empréstimo de Livros - Biblioteca Digital")
    print("Desenvolvido seguindo metodologia TDD")
    print("=" * 50)
    print()

    # Demonstrar sistema em memória
    demonstrar_sistema_memoria()

    # Demonstrar sistema com banco de dados
    demonstrar_sistema_banco()

    print("Demonstração concluída!")
    print("Execute 'pytest -v' para rodar todos os testes.")


if __name__ == "__main__":
    main()
