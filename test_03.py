import pytest

from dz_test03 import get_thecat


def test_get_thecat(mocker):
    mock_get = mocker.patch('dz_test03.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://example.com/image1.jpg'},
        {'url': 'https://example.com/image2.jpg'}
    ]


    cat_data = get_thecat()

    assert cat_data == [
        {'url': 'https://example.com/image1.jpg'},
        {'url': 'https://example.com/image2.jpg'},
    ]


def test_get_thecat_error(mocker):
    mock_get = mocker.patch('dz_test03.requests.get')
    mock_get.return_value.status_code = 404


    cat_data = get_thecat()

    assert cat_data == None
