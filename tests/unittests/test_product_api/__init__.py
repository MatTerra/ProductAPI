from unittest.mock import Mock

from pytest import fixture


@fixture(autouse=True)
def success_response(mocker):
    mock = mocker.patch("utils.controller.product_api.success_response")
    mock.side_effect = lambda status_code=200, message="OK", data={}: {
        "status_code": status_code,
        "message": message,
        "data": data
    }
    return mock


@fixture
def dao_mock():
    return Mock()
