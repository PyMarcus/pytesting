import pytest
import sqlalchemy
from sqlalchemy.sql import text


@pytest.fixture
def database_conn():
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    connection = engine.connect()
    yield connection
    connection.close()


def test_database_conn(database_conn):
    result = database_conn.execute(text("SELECT 1"))
    assert result.fetchone()[0] == 1

