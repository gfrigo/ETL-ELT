#pylint: disable=all
from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from .load_data import LoadData
from src.errors.load_error import LoadError

class RepositorySpy:

    def __init__(self) -> None:
        self.insert_artist_attribute = []

    def insert_artist(self, data):
        self.insert_artist_attribute.append(data)

def test_load_data():
    repository = RepositorySpy()
    load_data = LoadData(repository)

    load_data.load(transform_contract_mock)
    assert repository.insert_artist_attribute == transform_contract_mock.load_content

def test_load_data_error():
    repository = RepositorySpy()
    load_data = LoadData(repository)

    try:
        load_data.load('ErrorEntry')
    except Exception as exception:
        print(exception)
        assert isinstance(exception, LoadError)