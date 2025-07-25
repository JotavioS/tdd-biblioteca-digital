# Sistema de Empréstimo de Livros - Biblioteca Digital

Projeto desenvolvido seguindo metodologia TDD (Test-Driven Development) com Python.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.9
- **Framework de Testes**: PyTest
- **Bibliotecas**: 
  - SQLAlchemy (integração com banco de dados SQLite)
  - Pydantic (validação de dados)
- **Banco de Dados**: SQLite
- **Ferramentas**: Git, Docker

## Funcionalidades

- Cadastro de livros
- Cadastro de usuários
- Controle de empréstimos
- Controle de devoluções

## Ciclo TDD

1. **Red**: Escrever teste que falha
2. **Green**: Implementar código mínimo para teste passar
3. **Refactor**: Melhorar código mantendo testes passando

## Como executar

```bash
pip install -r requirements.txt
pytest
```