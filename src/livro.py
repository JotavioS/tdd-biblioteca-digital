from pydantic import BaseModel
from typing import Optional
import uuid


class Livro(BaseModel):
    """Classe que representa um livro na biblioteca"""
    
    titulo: str
    autor: str
    isbn: str
    disponivel: bool = True
    id: Optional[str] = None
    
    def __init__(self, **data):
        if 'id' not in data:
            data['id'] = str(uuid.uuid4())
        super().__init__(**data)
    
    def emprestar(self) -> bool:
        """Empresta o livro se estiver disponível"""
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver(self) -> bool:
        """Devolve o livro tornando-o disponível novamente"""
        if not self.disponivel:
            self.disponivel = True
            return True
        return False