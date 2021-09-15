# Bot Trello-Discord

Esse bot permite que os usuários solicitem pelo discord as tarefas pendentes para eles que estão no trello.

## Como Configurar
1. Rode o comando:
```
pip install -r "requirements.txt"
```
2. Cadastre os membros com seus respectivos <a href="https://developer.atlassian.com/cloud/trello/rest/">IDs do trello</a> no arquivo ```MembersId.py```
3. <a href="https://discord.com/developers/applications" Crie o BOT no discord </a> e o adicione no seu servidor
4. Substitua o Token do seu BOT no final do arquivo ```main.py```
5. Inicie o programa em algum ambiente, como por exemplo o <a href="https://replit.com/">Replit</a>
6. Interaja com o BOT pelo discord!

## Comandos no discord e retornos
### >>> Oi
```
Olá, {nome do usuário}! Tudo bem?
```

### >>> Tarefas {nome}
```
{nome do usuário}, você precisa fazer as seguintes tarefas:
{lista de tarefas do trello}
```
   
```
Poxa, {nome do usuário}, eu não te conheço ainda! Peça para alguém da VP te cadastrar no BOT :)
```
