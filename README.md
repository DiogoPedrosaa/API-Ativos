# API-Ativos

Este projeto foi desenvolvido durante o estágio na Secretaria Municipal da Fazenda de Maceió, com o objetivo de criar uma API para o gerenciamento de ativos. A API permite a manipulação, consulta e atualização de informações relacionadas aos ativos, contribuindo para a substituição de planilhas manuais, tornando o processo mais eficiente e automatizado.
(O Projeto não foi oficializado, então os codigos apresentados aqui, não estão sendo utilizados em nenhuma aplicação funcional.)

## Funcionalidades

- **Cadastro de ativos**: Registra novos ativos no sistema.
- **Listagem de ativos**: Exibe todos os ativos cadastrados.
- **Atualização de ativos**: Atualiza as informações dos ativos existentes.
- **Exclusão de ativos**: Remove ativos do sistema.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework

## Como rodar

1. Clone este repositório:
    ```bash
    git clone https://github.com/DiogoPedrosaa/API-Ativos.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Realize as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

4. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

Agora você pode acessar a API em `http://127.0.0.1:8000`.

## Endpoints

### **Fabricante**

- **POST /api/fabricantes/**  
  Cria um novo fabricante.
  
- **GET /api/fabricantes/**  
  Retorna todos os fabricantes.

- **GET /api/fabricantes/{id}/**  
  Retorna os detalhes de um fabricante específico.

- **PUT /api/fabricantes/{id}/**  
  Atualiza as informações de um fabricante.

- **DELETE /api/fabricantes/{id}/**  
  Remove um fabricante.

### **Tag**

- **POST /api/tags/**  
  Cria uma nova tag.
  
- **GET /api/tags/**  
  Retorna todas as tags.

- **GET /api/tags/{id}/**  
  Retorna os detalhes de uma tag específica.

- **PUT /api/tags/{id}/**  
  Atualiza as informações de uma tag.

- **DELETE /api/tags/{id}/**  
  Remove uma tag.

### **Ativo**

- **POST /api/ativos/**  
  Cria um novo ativo.
  
- **GET /api/ativos/**  
  Retorna todos os ativos.

- **GET /api/ativos/{id}/**  
  Retorna os detalhes de um ativo específico.

- **PUT /api/ativos/{id}/**  
  Atualiza as informações de um ativo.

- **DELETE /api/ativos/{id}/**  
  Remove um ativo.

### **Setor**

- **POST /api/setores/**  
  Cria um novo setor.
  
- **GET /api/setores/**  
  Retorna todos os setores.

- **GET /api/setores/{id}/**  
  Retorna os detalhes de um setor específico.

- **PUT /api/setores/{id}/**  
  Atualiza as informações de um setor.

- **DELETE /api/setores/{id}/**  
  Remove um setor.

### **Login**

- **POST /api/login/**  
  Realiza o login de um usuário com `username` e `password`.
