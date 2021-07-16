# Задача 1

Необходимо создать абстрактный класс Connection, который симулирует подключение к устройству, принимая на вход следующие параметры: ip, host, login, password
Реализовать валидацию входных параметров по следующим условиям:
    1) Пароль не короче 8 символов и не больше 16
    2) IP принадлежит к IPV4
Можно писать функцию самому или использовать pydantic в качестве валидации
От этого класса создать два интерфейса подключения: Telnet и SSL
Реализовать методы (фиктивные):
    1) Открытие соединения
    2) Закрытие соединения
    3) Отправка команды
    4) Получение принтаута

# Задача 2

Реализовать функцию accum, которая принимает на вход строку символов и преобразует ее в следующий вид:
accum("abcd") -> "A-Bb-Ccc-Dddd"

# Задача 3

Создать простой API-интерфейс используя библиотеку FastAPI. 
Реализовать методы:
    1) GET "/users/{user_id}" – для получения информации о пользователе
    2) PUT "/users/{user_id}/" – для редактирования информации о пользователе
    3) POST "/users/" - добавить нового пользователя
    4) DELETE "/users/{user_id}" – для удаления пользователя

БД можно создать фейковую, даже используя словарь вида:

```python
users = {
    'ivanov': {
        'id': 1111,
        'email': 'ivanov@mail.ru',
        'is_verified': True
    }
}
```