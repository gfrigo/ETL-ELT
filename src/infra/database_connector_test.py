from .database_connector import DatabaseConnector

def test_connect():
    print()
    print(DatabaseConnector.connection)
    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    print()
    print(DatabaseConnector.connection)
    assert DatabaseConnector.connection is not None