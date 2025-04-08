from Lesson_9.models import Student

def test_create_student(db_session):

    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert student is not None
    assert student.name == "Иван Иванов"


def test_update_student(db_session):

    # Создаем студента для теста
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()

    student.name = "Петр Сидоров"
    db_session.commit()


    updated = db_session.query(Student).filter_by(email="petr@example.com").first()
    assert updated.name == "Петр Сидоров"


def test_delete_student(db_session):

    student = Student(name="Сергей Сергеев", email="sergey@example.com")
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted is None
