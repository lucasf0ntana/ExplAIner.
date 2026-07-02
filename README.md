# ExplAIner 

**ExplAIner** é uma plataforma de estudos gamificada que utiliza Inteligência Artificial para gerar questões de múltipla escolha com base no tema escolhido pelo usuário. O sistema permite selecionar a dificuldade, quantidade de fases e acompanhar a pontuação, ranking e sequência de acertos (foguinho/streak), tornando o estudo mais dinâmico, rápido e eficiente para alunos do Ensino Médio.

## Integrantes da Equipe
* Lucas Ribeiro Fontana
* Josué Fernando Silva Melo
* Weber Anjos de Souza Sodré
* Álvaro Pires de Souza
* Antônio Henrique de Paula Reis
* Henrique Saddi Meinicke

## Stack Tecnológica
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6+)
* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-CORS
* **Banco de Dados:** MySQL

---

## Arquitetura e Estrutura do Backend

O projeto adota uma arquitetura robusta baseada no padrão **Service Pattern / Clean Architecture**, separando responsabilidades de forma clara e isolada:
* **Models:** Representação declarativa das tabelas estruturais e interações diretas de persistência com o banco de dados.
* **Services:** Camada isolada que concentra as regras de negócio complexas do ecossistema de gamificação.
* **Controllers (Blueprints):** Controladores de rotas encarregados de expor os endpoints da API HTTP e gerir as requisições/respostas JSON.

### Modelos de Dados Implementados (Models)
1. **Aluno (`alunos`):** Mapeamento completo contendo os dados cadastrais cruciais, pontuação acumulada (`pontos`) e a ofensiva de dias ativos (`foguinho`).
2. *Estrutura de tabelas prontas via SQL (Próximos Mapeamentos):* `Tema`, `Questao`, `Desafio`, `desafio_questao`, `aluno_desafio` e `Ranking`.

### Rotas da API (Endpoints)

#### Módulo de Alunos (`aluno_controller`)
| Método | Rota | Descrição | Status HTTP |
| :--- | :--- | :--- | :--- |
| **POST** | `/alunos` | Cadastra um novo aluno no sistema (valida duplicidade de e-mail) | `201 Created` |
| **GET** | `/alunos` | Lista todos os alunos cadastrados com as respetivas pontuações | `200 OK` |
| **GET** | `/alunos/<id>` | Busca os detalhes específicos de um único aluno por ID | `200 OK` / `404` |
| **PUT** | `/alunos/<id>` | Atualiza dados cadastrais de forma parcial ou total do aluno | `200 OK` / `404` |
| **DELETE** | `/alunos/<id>` | Remove de forma permanente o registro do aluno do sistema | `204 No Content` |

---

## Funcionalidades do Frontend

A interface gráfica adota um design minimalista e moderno baseado em cartões centralizados estruturados com CSS Grid e Flexbox. Toda a comunicação com a API Flask ocorre de forma assíncrona por meio de requisições `fetch`.

* **Cadastro (`index.html` + `script.js`):** Captação de dados dinâmicos com envio direto via JSON. O campo ID foi removido da interface visual, delegando a responsabilidade de autoincremento ao banco de dados.
* **Consulta (`ler.html` + `ler.js`):** Campo de busca por ID numérico que renderiza em tempo real um painel estilizado com o Nome, E-mail, Ofensiva (Foguinho 🔥) e Pontuação (✨) do aluno.
* **Listagem (`listar.html` + `listar.js`):** Tabela integrada ao layout padrão que consome o endpoint de listagem global para apresentar o panorama completo dos estudantes salvos.
* **Edição (`atualizar.html` + `atualizar.js`):** Formulário inteligente que envia para a API apenas os campos que o utilizador modificou, prevenindo sobreescritas acidentais.
* **Remoção (`deletar.html` + `deletar.js`):** Painel de ação crítica com trigger de aviso visual e caixa de dupla confirmação nativa do navegador para deleções seguras.

---

## Como Executar o Projeto

Antes de começar, certifique-se de ter instalado em sua máquina:
* **Python 3.x**
* **Git** (opcional)

---

## 💻 Passo a Passo para Rodar o Projeto

Siga os comandos abaixo no seu terminal (Prompt de Comando ou PowerShell):

### 1. Acessar a pasta do backend
```bash
cd backend
```

### 2. Criar o Ambiente Virtual (.venv)
Cria um ambiente isolado para evitar conflitos de bibliotecas globais:
```bash
python -m venv .venv
```

### 3. Ativar o Ambiente Virtual
* **No Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\activate
  ```
* **No Windows (Prompt de Comando - CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

### 4. Configurar as Variáveis de Ambiente
Crie o arquivo `.env` copiando as configurações de exemplo:
```bash
cp .env.example .env
```
*(Se o comando `cp` não funcionar no CMD do Windows, use: `copy .env.example .env`)*

### 5. Instalar as Dependências
Para evitar erros de scripts corrompidos (`Fatal error in launcher`), instale as dependências chamando diretamente o executável do Python do ambiente:

```powershell
# Instalar pacotes do arquivo de requerimentos
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# Garantir a instalação dos pacotes principais e drivers de banco
.\.venv\Scripts\python.exe -m pip install flask flask-sqlalchemy pymysql
```

### 6. Executar a Aplicação
Inicie o servidor Flask utilizando o Python do ambiente virtual:
```bash
.\.venv\Scripts\python.exe app.py
```

---

## 🐛 Resolução de Problemas Comuns

### Erro: "Fatal error in launcher: Unable to create process..."
Esse erro ocorre no Windows quando a pasta do projeto é movida de lugar ou sincronizada no OneDrive. 
* **Solução:** Nunca use o comando `pip install` diretamente se o erro persistir. Use sempre o prefixo `.\.venv\Scripts\python.exe -m pip install <pacote>`.
