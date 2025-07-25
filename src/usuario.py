import uuid
from typing import List, Optional

from pydantic import BaseModel


class Usuario(BaseModel):
    """Classe que representa um usuário da biblioteca"""

    nome: str
    email: str
    id: Optional[str] = None
    livros_emprestados: List[str] = []

    def __init__(self, **data):
        if "id" not in data:
            data["id"] = str(uuid.uuid4())
        if "livros_emprestados" not in data:
            data["livros_emprestados"] = []
        super().__init__(**data)
