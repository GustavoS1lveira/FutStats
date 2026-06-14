⚽ FutStats

FutStats é uma aplicação desenvolvida em Python que consome uma API de futebol para buscar estatísticas de jogadores e realizar comparações de desempenho entre atletas.

O sistema permite pesquisar jogadores por nome e comparar métricas como jogos disputados e gols marcados, retornando automaticamente um “vencedor” entre os jogadores analisados.

🚀 Como executar o projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/futstats.git
cd futstats
2. Criar ambiente virtual (opcional, recomendado)
python -m venv venv

Ativar no Windows:

venv\Scripts\activate

Ativar no Linux/Mac:

source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Configurar API

Crie um arquivo .env na raiz do projeto:

API_KEY=sua_chave_da_api
API_HOST=api-football-v1.p.rapidapi.com

⚠️ Este projeto utiliza a API-Football (RapidAPI)

5. Executar o projeto
python main.py
▶️ Como usar o sistema

Ao iniciar o programa, você verá opções no terminal.

🔎 Buscar jogador

Digite o nome de um jogador:

Messi

O sistema retorna informações como:

Nome completo
Idade
Nacionalidade
Jogos
Gols
⚔️ Comparar jogadores

Digite dois nomes quando solicitado:

Ronaldo
Neymar

Exemplo de saída:

Jogos: Ronaldo 223 x Neymar 56
Gols: Ronaldo 193 x Neymar 35

🏆 Vencedor geral: Ronaldo
🧠 Funcionalidades
Busca de jogadores por nome via API
Tratamento de dados retornados
Exibição de estatísticas detalhadas
Comparação entre dois jogadores
Definição automática de vencedor com base em métricas
📁 Estrutura do projeto
FutStats/
│
├── main.py                # Arquivo principal (executar aqui)
├── api.py                # Comunicação com a API
├── services/
│   ├── player_service.py
│   └── comparison_service.py
├── utils/
│   └── helpers.py
├── .env
├── requirements.txt
└── README.md
⚠️ Problemas conhecidos
A API pode retornar jogadores com nomes similares
Alguns jogadores podem aparecer duplicados
Dependência de internet ativa
Limite de requisições dependendo do plano da API
🚧 Possíveis melhorias futuras
Interface gráfica (Tkinter ou Web com Flask)
Dashboard com gráficos (gols, jogos, desempenho)
Sistema de ranking de jogadores
Melhor filtragem por ID do jogador
Cache local para reduzir chamadas na API
👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos, com foco em consumo de APIs REST e manipulação de dados em Python.

✅ Observação final importante

Para o projeto funcionar corretamente:

Internet deve estar ativa
API Key válida deve estar no .env
Executar sempre pelo main.py