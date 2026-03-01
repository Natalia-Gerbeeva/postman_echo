import requests
import pytest
import allure

BASE_URL = "https://postman-echo.com"


@allure.title("GET без параметров возвращает 200")
@allure.description("Проверяем, что базовый GET-запрос работает корректно.")
def test_get_basic():
    with allure.step("Отправляем GET запрос"):
        response = requests.get(f"{BASE_URL}/get")

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


import pytest

@pytest.fixture
def query_params():
    return {"foo": "bar"}

@allure.title("GET с параметрами возвращает их в args")
@allure.description("Отправляем query параметры и проверяем их в ответе.")
def test_get_with_query(query_params):
    with allure.step("Отправляем GET с параметрами"):
        response = requests.get(f"{BASE_URL}/get", params=query_params)

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем args"):
        assert response.json()["args"] == query_params


@allure.title("POST form-data возвращает 200")
@allure.description("Проверяем отправку form-data.")
def test_post_form_data():
    with allure.step("Отправляем POST"):
        response = requests.post(f"{BASE_URL}/post", data={"key": "value"})

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200


@allure.title("POST JSON возвращает отправленные данные")
@allure.description("Проверяем JSON тело ответа.")
def test_post_json():
    json_body = {"name": "Alice", "age": 30}

    with allure.step("Отправляем POST JSON"):
        response = requests.post(f"{BASE_URL}/post", json=json_body)

    with allure.step("Проверяем статус код"):
        assert response.status_code == 200

    with allure.step("Проверяем тело ответа"):
        assert response.json()["json"] == json_body