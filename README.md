# ⚽ FutStats

FutStats é uma aplicação desenvolvida em Python que consome uma API de futebol para buscar estatísticas de jogadores e realizar comparações de desempenho entre atletas.

O sistema permite pesquisar jogadores por nome e comparar métricas como jogos disputados e gols marcados, retornando automaticamente um “vencedor” entre os jogadores analisados.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/futstats.git
cd futstats
````

---

### 2. Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

Ativar no Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar API

Crie um arquivo `.env` na raiz do projeto com:

```env
API_KEY=sua_chave_da_api
API_HOST=api-football-v1.p.rapidapi.com
```

> ⚠️ Este projeto utiliza a API-Football (via RapidAPI)

---

### 5. Executar o projeto

```bash
python main.py
```

---

## ▶️ Como usar o sistema

Ao iniciar o programa, o usuário pode buscar ou comparar jogadores.

### 🔎 Buscar jogador

Exemplo:

```
Messi
```

Saída esperada:

* Nome completo
* Idade
* Nacionalidade
* Jogos
* Gols

---

### ⚔️ Comparar jogadores

Exemplo:

```
Ronaldo
Neymar
```

Saída:

```
Jogos: Ronaldo 223 x Neymar 56
Gols: Ronaldo 193 x Neymar 35

🏆 Vencedor geral: Ronaldo
```

---

## 🧠 Funcionalidades

* Busca de jogadores por nome via API
* Tratamento de dados da API
* Exibição de estatísticas
* Comparação entre dois jogadores
* Definição automática de vencedor

---

## 📁 Estrutura do projeto

```
FutStats/
│
├── main.py
├── api.py
├── services/
│   ├── player_service.py
│   └── comparison_service.py
├── utils/
│   └── helpers.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚠️ Problemas conhecidos

* A API pode retornar jogadores com nomes semelhantes
* Alguns dados podem variar conforme a API
* Dependência de internet ativa
* Limite de requisições dependendo do plano da API

---

## 🚧 Melhorias futuras

* Interface gráfica (Tkinter ou Web com Flask)
* Dashboard com gráficos de desempenho
* Sistema de ranking de jogadores
* Melhor filtragem por ID do jogador
* Cache local para reduzir chamadas na API

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos, com foco em consumo de APIs REST e manipulação de dados em Python.

```
```
