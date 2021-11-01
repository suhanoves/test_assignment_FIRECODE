Тестовое задание компании FIRECODE
======

Данный репозиторий создан для выполнения тестового задания компании FIRECODE на вакансию Python Developer.

* **ФИО**: Суханов Евгений
* [Оригинал ТЗ](./assets/test_assignment.pdf)

## Запуск проекта

* Docker Engine 19.03.0+
* Docker Compose 1.27.0+

```Bash
git clone https://github.com/suhanoves/test_assignment_FIRECODE.git
cd test_assignment_FIRECODE/
docker-compose up -d
```

## Информация о доступах

* Доступ к API:
  * http://127.0.0.1:8088/api/v1/
* Доступ в админку:
  * http://127.0.0.1:8088/admin
  * username: `root`
  * password: `111`

## Описание API

| Endpoint | HTTP Method | CRUD Method | Result | 
|:---:|:---:|:---:|---|
| `city` | GET | READ | Список всех городов |
| `street` | GET | READ | Список всех улиц |
| `shop` | GET | READ | Список всех магазинов |
| `city/{city_id}` | GET | READ | Информация о городе |
| `city/{city_id}/street` | GET | READ | Информация об улицах города |
| `street/{street_id}` | GET | READ | Информация об улице |
| `shop/{shop_id}` | GET | READ | Информация о магазине |
| `shop/?street=&city=&open={0/1}` | GET | READ | Получение списка магазинов по параметрам |

Параметры для поиска магазинов:
* `city_id` - `id` города
* `city__name` - имя города
* `street_id` - `id` улицы
* `street__name` - имя улицы
* `open={0/1}` - статус определяется исходя из параметров «Время открытия»,
«Время закрытия» и текущего времени сервера.
  
| Endpoint | HTTP Method | CRUD Method | Result | 
|:---:|:---:|:---:|---|
| `city` | POST | CREATE | Создание города |
| `street` | POST | CREATE | Создание улицы |
| `shop` | POST | POST | Создание магазина |
| `city/{city_id}` | PUT | UPDATE | Обновление информации о городе |
| `street/{street_id}` | PUT | UPDATE | Обновление информации об улице |
| `shop/{shop_id}` | PUT | UPDATE | Обновление информации о магазине |
| `city/{city_id}` | DELETE | DELETE | Удаление города |
| `street/{street_id}` | DELETE | DELETE | Удаление улицы |
| `shop/{shop_id}` | DELETE | DELETE | Удаление магазина |