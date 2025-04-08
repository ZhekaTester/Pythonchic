import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Lesson_9.models import Base
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

DB_URL = 'postgresql://postgres:ztest@localhost:5432/mydatabase'


@pytest.fixture(scope='module')
def engine():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()