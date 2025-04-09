import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .form_page import FormPage


@allure.title("Тест на проверку заполнения формы")
@allure.feature("FORM")
@allure.description("Проверка заполнения всех ячеек формы, подсвечивание красным, если не заполнено")
@allure.severity("critical")
def test_form_submission():
    with allure.step("Открыть страницу формы по ссылке"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(driver)

    with allure.step("Ввести данные в поля, поле zip code оставить пустым"):
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        form_page.fill_form(data)

    with allure.step("Нажатие кнопки Submit (отправка формы)"):
        form_page.submit_form()

    form_page.wait_for_zip_code()

    with allure.step("Проверить, что поле Zip code подсвечено красным"):
        alert_danger_color = "rgba(248, 215, 218, 1)"
        color_zip = form_page.get_zip_code_color()
        assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

    with allure.step("Проверить, что остальные поля подсвечены зеленым"):
        alert_success_color = "rgba(209, 231, 221, 1)"
        fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        for field_name in fields:
            field_color = form_page.get_field_color(field_name)
            assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"

    driver.quit()
    