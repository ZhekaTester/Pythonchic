from Lesson_9.models import Student
from sqlalchemy import text  # Добавьте этот импорт


def test_create_student(db_session):
    """Тест создания студента"""
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Проверка через text()
    result = db_session.execute(text("SELECT COUNT(*) FROM students WHERE email = 'ivan@example.com'"))
    assert result.scalar() == 1
