from typing import List, Dict, Any, Optional
from src.livro import Livro
from src.usuario import Usuario
from datetime import datetime


class Biblioteca:
    """Classe que gerencia o sistema de empréstimos da biblioteca"""
    
    def __init__(self):
        self.livros: List[Livro] = []
        self.usuarios: List[Usuario] = []
        self.emprestimos: List[Dict[str, Any]] = []
    
    def adicionar_livro(self, livro: Livro) -> None:
        """Adiciona um livro ao acervo da biblioteca"""
        self.livros.append(livro)
    
    def adicionar_usuario(self, usuario: Usuario) -> None:
        """Adiciona um usuário à biblioteca"""
        self.usuarios.append(usuario)
    
    def emprestar_livro(self, livro_id: str, usuario_id: str) -> bool:
        """Empresta um livro para um usuário"""
        # Encontrar o livro
        livro = self._encontrar_livro(livro_id)
        if not livro:
            return False
        
        # Encontrar o usuário
        usuario = self._encontrar_usuario(usuario_id)
        if not usuario:
            return False
        
        # Verificar se o livro está disponível
        if not livro.disponivel:
            return False
        
        # Realizar o empréstimo
        if livro.emprestar():
            emprestimo = {
                'livro_id': livro_id,
                'usuario_id': usuario_id,
                'data_emprestimo': datetime.now(),
                'data_devolucao': None
            }
            self.emprestimos.append(emprestimo)
            return True
        
        return False
    
    def _encontrar_livro(self, livro_id: str) -> Optional[Livro]:
        """Encontra um livro pelo ID"""
        for livro in self.livros:
            if livro.id == livro_id:
                return livro
        return None
    
    def _encontrar_usuario(self, usuario_id: str) -> Optional[Usuario]:
        """Encontra um usuário pelo ID"""
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None