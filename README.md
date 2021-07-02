# Sistema Funworks

Sistema para consultar e gerenciar as mensalidades dos associados.

## Como subir o projeto:

 - Clonar o projeto e entrar na pasta:
```
git clone https://github.com/Perceu/funworks.git
cd funworks
```
 - Criar Virtual Env
```
python -m venv .venv
```
 - Ativar Virtual Env
```
Linux: source .venv\bin\activate
    ||
Windows: .venv\Scripts\activate
```
 - Instalar Dependencias
```
(.venv)# pip install -r requiriments.txt
```
 - Criar Enviroment
```
(.venv)# cp contrib/env-sample .env
```
 - Criar Enviroment

```
(.venv)# cp contrib/env-sample .env
```

Para subir um postgres use o docker dentro da pasta docker, mas caso queira so desenvolver local basta comentar a linha `DATABASE_URL` no .env

## Para rodar o projeto

 - Para rodar migrações/criar banco
```
(.venv)# python manage.py migrate
```
 - Para rodar local
```
(.venv)# python manage.py runserver
```
 - Para criar o primeiro usuario
```
(.venv)# python manage.py createsuperuser
```

