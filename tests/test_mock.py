import requests
import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}
    return mock


def test_api_call(mock_response):
    assert mock_response.status_code == 200, "Status code is not equal 200"
    assert mock_response.json() == {"message": "Success"}