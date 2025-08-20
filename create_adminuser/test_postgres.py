import psycopg2
import pytest
import time


@pytest.fixture(scope="session")
def db_connection():
    """Wait for the Postgres container and return a connection."""
    for i in range(10):  # retry for ~10 * 3s = 30s
        try:
            conn = psycopg2.connect(
                dbname="WESHAI",
                user="weshaiadmin",
                password="supersecret",
                host="localhost",
                port="5432"
            )
            conn.autocommit = True
            yield conn
            conn.close()
            return
        except Exception as e:
            print(f"Retrying DB connection... {e}")
            time.sleep(3)
    pytest.fail("Could not connect to Postgres container")


def test_database_exists(db_connection):
    """Check that the WESHAI database exists."""
    cur = db_connection.cursor()
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    dbs = [row[0] for row in cur.fetchall()]
    cur.close()

    assert "WESHAI" in dbs, "WESHAI database was not created!"
