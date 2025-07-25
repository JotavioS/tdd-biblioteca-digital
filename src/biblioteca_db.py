import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session

from src.models import EmprestimoModel, LivroModel, UsuarioModel


class BibliotecaDB:
    """Classe que gerencia operações da biblioteca com banco de dados"""

    def __init__(self, db: Session):
        self.db = db

    def criar_livro(self, livro_data: Dict[str, Any]) -> str:
        """Cria um novo livro no banco de dados"""
        livro = LivroModel(
            id=str(uuid.uuid4()),
            titulo=livro_data["titulo"],
            autor=livro_data["autor"],
            isbn=livro_data["isbn"],
            disponivel=True,
        )

        self.db.add(livro)
        self.db.commit()
        self.db.refresh(livro)

        return livro.id

    def criar_usuario(self, usuario_data: Dict[str, Any]) -> str:
        """Cria um novo usuário no banco de dados"""
        usuario = UsuarioModel(
            id=str(uuid.uuid4()), nome=usuario_data["nome"], email=usuario_data["email"]
        )

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)

        return usuario.id

    def emprestar_livro(self, livro_id: str, usuario_id: str) -> Optional[str]:
        """Empresta um livro para um usuário"""
        # Verificar se o livro existe e está disponível
        livro = self.db.query(LivroModel).filter(LivroModel.id == livro_id).first()
        if not livro or not livro.disponivel:
            return None

        # Verificar se o usuário existe
        usuario = (
            self.db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
        )
        if not usuario:
            return None

        # Criar o empréstimo
        emprestimo = EmprestimoModel(
            id=str(uuid.uuid4()),
            livro_id=livro_id,
            usuario_id=usuario_id,
            data_emprestimo=datetime.now(),
            data_devolucao=None,
        )

        # Marcar livro como indisponível
        livro.disponivel = False

        self.db.add(emprestimo)
        self.db.commit()
        self.db.refresh(emprestimo)

        return emprestimo.id

    def devolver_livro(self, livro_id: str, usuario_id: str) -> bool:
        """Devolve um livro emprestado"""
        # Encontrar o empréstimo ativo
        emprestimo = (
            self.db.query(EmprestimoModel)
            .filter(
                EmprestimoModel.livro_id == livro_id,
                EmprestimoModel.usuario_id == usuario_id,
                EmprestimoModel.data_devolucao.is_(None),
            )
            .first()
        )

        if not emprestimo:
            return False

        # Encontrar o livro
        livro = self.db.query(LivroModel).filter(LivroModel.id == livro_id).first()
        if not livro:
            return False

        # Realizar a devolução
        emprestimo.data_devolucao = datetime.now()
        livro.disponivel = True

        self.db.commit()

        return True

    def listar_livros_disponiveis(self):
        """Lista todos os livros disponíveis"""
        return self.db.query(LivroModel).filter(LivroModel.disponivel == True).all()

    def listar_emprestimos_ativos(self):
        """Lista todos os empréstimos ativos"""
        return (
            self.db.query(EmprestimoModel)
            .filter(EmprestimoModel.data_devolucao.is_(None))
            .all()
        )
