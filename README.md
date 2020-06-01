# PetOdonto
**Sistema para Gestão de Dentistas de Odontológicos**

Uma instância deste sistema está disponível no link:
http://petsorriso-dev.herokuapp.com/

``` 
Credenciais:
Login: user
Senha: petodonto123
```

### Instalação

Para instalar as dependências requeridas:

```
pip install -r requirements.txt
```

Note que é necessário criar um bucket na Amazon AWS e adicionar no arquivo base.py:

```python

# AWS
AWS_ACCESS_KEY_ID = '##YOUR_KEY_ID##'
AWS_SECRET_ACCESS_KEY = '##YOUR_SECRET_KEY##'
AWS_STORAGE_BUCKET_NAME = '##YOUR_BUCKET_NAME##'
AWS_S3_REGION_NAME = '##YOUR_REGION_NAME##'
AWS_S3_ENDPOINT_URL = '##YOUR_ENDPOINT_URL##'
S3DIRECT_DESTINATIONS = {
    'arquivos_cirurgia': {
        'key': 'uploads/images',
        'auth': lambda u: u.is_authenticated,
        'allowed': ['image/jpeg', 'image/png'],
    }
}

```

Agora vamos migrar os modelos para o banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

Agora crie um usuario adminstrador:

```
python manage.py createsuperuser
```

Rode o projeto:

```
python manage.py runserver
```

#### Principais Tecnologias utilizadas

* Django Framework
* Django Rest Framework
* Bootstrap 4
* JQuery
* Heroku 
