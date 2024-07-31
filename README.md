# Запуск локально
1. Создать файл .env
2. Создать переменыне окружения:
- ```DJANGO_DEBUG = False```
- ```DJANGO_SECRET_KEY = <your secret key>```

- ```DJANGO_DATABASE_NAME = article```
- ```DJANGO_DATABASE_USER = user```
- ```DJANGO_DATABASE_PASSWORD = pass123```
- ```DJANGO_DATABASE_HOST = db```
- ```DJANGO_DATABASE_PORT = 5432```

### Нужны для PostgreSQL в Docker
- ```POSTGRES_DB=article```
- ```POSTGRES_USER=user```
- ```POSTGRES_PASSWORD=pass123```
- ```PGPORT=5432```

# Документация к API
```http://.../api/docs/```
