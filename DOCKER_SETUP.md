# Configuração do Docker para o Sistema de Biblioteca

## 📋 Pré-requisitos

### Windows
1. **Instalar Docker Desktop**:
   - Baixe em: https://www.docker.com/products/docker-desktop/
   - Execute o instalador e siga as instruções
   - Reinicie o computador se solicitado

2. **Verificar Instalação**:
   ```powershell
   docker --version
   docker-compose --version
   ```

3. **Iniciar Docker Desktop**:
   - Abra o Docker Desktop
   - Aguarde até que o status mostre "Docker Desktop is running"

### Linux
1. **Instalar Docker**:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install docker.io docker-compose
   
   # CentOS/RHEL
   sudo yum install docker docker-compose
   ```

2. **Iniciar Docker**:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Adicionar usuário ao grupo docker** (opcional):
   ```bash
   sudo usermod -aG docker $USER
   # Faça logout e login novamente
   ```

### macOS
1. **Instalar Docker Desktop**:
   - Baixe em: https://www.docker.com/products/docker-desktop/
   - Arraste para a pasta Applications
   - Execute e siga as instruções

## 🚀 Comandos Docker para o Projeto

### Build da Imagem
```bash
docker build -t sistema-biblioteca .
```

### Executar Sistema
```bash
# Executar demonstração
docker run --rm sistema-biblioteca

# Executar testes
docker run --rm sistema-biblioteca pytest -v

# Executar com volume para persistência
docker run --rm -v $(pwd)/data:/app/data sistema-biblioteca
```

### Usando Docker Compose
```bash
# Executar sistema principal
docker-compose up --build biblioteca

# Executar testes
docker-compose --profile testing up --build biblioteca-tests

# Modo desenvolvimento
docker-compose --profile development up -d biblioteca-dev
docker exec -it sistema-biblioteca-dev /bin/bash
```

## 🔧 Solução de Problemas

### Erro: "Docker daemon is not running"
- **Windows**: Abra o Docker Desktop
- **Linux**: `sudo systemctl start docker`
- **macOS**: Abra o Docker Desktop

### Erro: "Permission denied"
- **Linux**: Adicione seu usuário ao grupo docker ou use `sudo`
- **Windows/macOS**: Execute como administrador

### Erro: "No space left on device"
```bash
# Limpar imagens não utilizadas
docker system prune -a

# Limpar volumes não utilizados
docker volume prune
```

### Erro: "Port already in use"
```bash
# Verificar containers rodando
docker ps

# Parar container específico
docker stop <container_id>

# Parar todos os containers
docker stop $(docker ps -q)
```

## 📊 Verificação da Instalação

Após instalar o Docker, execute estes comandos para verificar:

```bash
# Verificar versão
docker --version
docker-compose --version

# Testar com hello-world
docker run hello-world

# Verificar se o daemon está rodando
docker info
```

## 🎯 Próximos Passos

Após configurar o Docker:

1. **Teste o build**:
   ```bash
   docker build -t sistema-biblioteca .
   ```

2. **Execute o sistema**:
   ```bash
   docker run --rm sistema-biblioteca
   ```

3. **Execute os testes**:
   ```bash
   docker run --rm sistema-biblioteca pytest -v
   ```

Se tudo funcionar corretamente, você verá a demonstração do sistema e todos os 17 testes passando!