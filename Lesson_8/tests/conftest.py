import pytest
from Lesson_8.api.project_api import ProjectsAPI


@pytest.fixture(scope="module")
def projects_api():
    # Эти значения нужно заменить на реальные перед запуском тестов
    base_url = "https://yougile.com"
    api_token = "your_api_token_here"

    return ProjectsAPI(base_url, api_token)


@pytest.fixture(scope="module")
def created_project_id(projects_api):
    # Создаем временный проект для тестов
    project_data = {
        "name": "Temp Project for Tests",
        "description": "This project will be deleted after tests"
    }
    response = projects_api.create_project(project_data)
    assert response.status_code == 201

    project_id = response.json()["id"]
    yield project_id
