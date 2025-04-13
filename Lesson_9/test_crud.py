from Lesson_9.models import Student
from sqlalchemy import text

def test_create_student(db_session):
    # Создаем нового студента
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Проверяем
    student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert student is not None
    assert student.name == "Иван Иванов"

def test_update_student(db_session):
    # Сначала создаем студента для теста
    original_student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(original_student)
    db_session.commit()

    # Редактируем данные
    student_to_update = db_session.query(Student).filter_by(email="petr@example.com").first()
    student_to_update.name = "Петр Сидоров"  # Меняем имя
    db_session.commit()

    # Проверка через raw SQL
    result = db_session.execute(
        text("SELECT name FROM students WHERE email = 'petr@example.com'")
    )
    assert result.scalar() == "Петр Сидоров"

def test_delete_student(db_session):
    #  тест для удаления
    student_to_delete = Student(name="Сергей Сергеев", email="sergey@example.com")
    db_session.add(student_to_delete)
    db_session.commit()

    # Проверяем, что студент создан
    assert db_session.query(Student).filter_by(email="sergey@example.com").count() == 1

    # Удаляем студента
    db_session.delete(student_to_delete)
    db_session.commit()

    result = db_session.execute(
        text("SELECT COUNT(*) FROM students WHERE email = 'sergey@example.com'")
    )
    assert result.scalar() == 0