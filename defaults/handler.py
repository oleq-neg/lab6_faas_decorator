import random
import string

def random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

def call_my_api(obj):
    return {
        "status": "ok",
        "applied_defaults": obj
    }

def handle(event, context):
    # Получаем входное значение [4]
    obj = event.body if isinstance(event.body, dict) else {}

    # Если поле "name" отсутствует — случайная строка [4]
    if obj.get("name", None) is None:
        obj["name"] = random_name()

    # Если поле 'color' отсутствует — значение 'blue' [4]
    if obj.get("color", None) is None:
        obj["color"] = "blue"

    # Выполнить API-вызов и вернуть результат [4]
    result = call_my_api(obj)

    return {
        "statusCode": 200,
        "body": result
    }