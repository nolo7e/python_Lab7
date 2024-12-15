# Лабораторная работа №7. REST. FastAPI. Swagger

## Запуск проекта 

```bash
docker-compose up
```
![alt text](1.jpg)
![alt text](9.png)

## Демонстрация

### Swagger
![alt text](2.jpg)

### Получение списка всех терминов.

```
curl -X 'GET' 'http://localhost:8000/terms/'
```

![alt text](3.jpg)

### Получение информации о конкретном термине по ключевому слову.


```
curl -X GET "http://127.0.0.1:8000/terms/search/?keyword=CQRS"
```

![alt text](4.png)

### Получение термина по id

```
curl -X GET "http://127.0.0.1:8000/terms/1"
```

![alt text](5.png)


### Добавление нового термина с описанием.
```
curl -X POST "http://127.0.0.1:8000/terms/" ^ -H "Content-Type: application/json" ^ -d "{\"keyword\": \"Новый термин\", \"description\": \"Описание нового термина\"}"
```
![alt text](6.png)


### Обновление существующего термина.

```
curl -X PUT "http://127.0.0.1:8000/terms/5" ^ -H "Content-Type: application/json" ^ -d "{\"keyword\": \"Обновленный термин\", \"description\": \"Обновленное описание термина\"}"
```

![alt text](7.png)


### Удаление термина из глоссария.

``` 
curl -X DELETE "http://127.0.0.1:8000/terms/5"
```

![alt text](8.jpg)
