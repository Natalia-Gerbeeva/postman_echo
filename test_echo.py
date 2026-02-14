import requests
import pytest

BASE_URL = "https://postman-echo.com"

# Фикстура: простой набор параметров для GET-запроса
@pytest.fixture
def query_params():
    return {"foo": "bar"}

# Проверяем, что GET-запрос без параметров возвращает 200
def test_get_basic():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200

# Проверяем GET-запрос с query-параметрами
def test_get_with_query(query_params):
    response = requests.get(f"{BASE_URL}/get", params=query_params)
    assert response.status_code == 200
    assert response.json()["args"] == query_params

# Проверяем, что POST-запрос с form-данными проходит
def test_post_form_data():
    response = requests.post(f"{BASE_URL}/post", data={"key": "value"})
    assert response.status_code == 200

# Проверяем POST-запрос с JSON-телом
def test_post_json():
    json_body = {"name": "Alice", "age": 30}
    response = requests.post(f"{BASE_URL}/post", json=json_body)
    assert response.status_code == 200
    assert response.json()["json"] == json_body

# Проверяем отправку кастомного заголовка
def test_custom_header():
    headers = {"Custom-Header": "Test"}
    response = requests.get(f"{BASE_URL}/get", headers=headers)
    assert response.status_code == 200
    assert response.json()["headers"]["custom-header"] == "Test"
# Test CI run
