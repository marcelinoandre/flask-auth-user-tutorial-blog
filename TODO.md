- Criar ambiente  Virtual
- Ativar ambiente Virtual
- Adicionar o arquivo README.md
- Instalar dependências
- Criar arquivo database.py e importar o SQLAlchemy
- Modelar Usuario
- Criar o arquivo app.py
    - importar LoginManager, login_user do flask_login
- Configirações de boot do flask
- Conectar no BD
- criar uma rota hello_world
- Executar o app para verificar se está tudo ok
- Acesse o flask shell para executarmos os comandos para criação do banco de dados e da tabela user
```python
flask shell
 ```
- Criando a base e a tabela user
```python
db.create_all()
```

- Crie um usuário atraves da model user
```python
user = User(name='Andre Marcelino', email='marcelinoandre@gmail.com', password='102030')
 ```
- Adicione no usuario no BD, e efetive o commit da operaçãp
```python
db.session.add(user)
db.session.commit()
```
-- Tudo certo até aqui? então vamos commitar nossas alterações até aqui.

