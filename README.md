# Sistema de Empréstimo de Livros - Biblioteca Digital

Um sistema completo de gerenciamento de biblioteca desenvolvido seguindo a metodologia **TDD (Test-Driven Development)**, implementado em Python com integração a banco de dados SQLite.

## 🚀 Funcionalidades

### Gestão de Livros
- ✅ Cadastro de livros com título, autor e ISBN
- ✅ Controle de disponibilidade
- ✅ Empréstimo e devolução
- ✅ Validação de dados obrigatórios

### Gestão de Usuários
- ✅ Cadastro de usuários com nome e email
- ✅ Geração automática de ID único (UUID)
- ✅ Controle de livros emprestados
- ✅ Validação de dados obrigatórios

### Sistema de Empréstimos
- ✅ Empréstimo de livros disponíveis
- ✅ Controle de data de empréstimo
- ✅ Devolução com registro de data
- ✅ Validação de regras de negócio
- ✅ Persistência em banco de dados SQLite

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Pydantic** - Validação de dados e modelos
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **pytest** - Framework de testes
- **UUID** - Geração de identificadores únicos

## 🧪 Cobertura de Testes

O projeto possui **17 testes** cobrindo:

- ✅ **4 testes** para classe Livro
- ✅ **3 testes** para classe Usuario
- ✅ **7 testes** para classe Biblioteca
- ✅ **3 testes** de integração com banco

## 📋 Metodologia TDD

O projeto foi desenvolvido seguindo rigorosamente o ciclo TDD:

### 🔴 RED - Escrever teste que falha
1. **Livro**: Testes para criação, validação e empréstimo
2. **Usuario**: Testes para criação e validação
3. **Biblioteca**: Testes para gestão de livros, usuários e empréstimos
4. **Integração**: Testes para persistência em banco de dados

### 🟢 GREEN - Implementar código mínimo
1. **Livro**: Implementação com Pydantic
2. **Usuario**: Implementação com Pydantic
3. **Biblioteca**: Lógica de negócio em memória
4. **BibliotecaDB**: Persistência com SQLAlchemy

### 🔵 REFACTOR - Melhorar código
1. **Modelos**: Separação de responsabilidades
2. **Integração**: Configuração de banco de dados
3. **Demonstração**: Arquivo main.py para showcase
4. **Documentação**: README completo

## 🚀 Como Usar

### Instalação
```bash
pip install -r requirements.txt
```

### Executar Demonstração
```bash
python main.py
```

### Executar Testes
```bash
# Todos os testes
pytest -v

# Testes específicos
pytest tests/test_livro.py -v
pytest tests/test_biblioteca.py -v
pytest tests/test_integration.py -v
```

## 📈 Exemplo de Uso

```python
from src.biblioteca import Biblioteca
from src.livro import Livro
from src.usuario import Usuario

# Criar biblioteca
biblioteca = Biblioteca()

# Criar e adicionar livro
livro = Livro(titulo="1984", autor="George Orwell", isbn="978-0451524935")
biblioteca.adicionar_livro(livro)

# Criar e adicionar usuário
usuario = Usuario(nome="João Silva", email="joao@email.com")
biblioteca.adicionar_usuario(usuario)

# Emprestar livro
resultado = biblioteca.emprestar_livro(livro.id, usuario.id)
print(f"Empréstimo: {resultado}")  # True
```

---

**Desenvolvido seguindo as melhores práticas de TDD e Clean Code.**