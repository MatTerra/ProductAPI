from unittest.mock import Mock

from pytest import raises, fixture

from utils.controller import product_api
from tests.unittests.test_product_api import success_response, dao_mock


class TestProbe:
    @staticmethod
    def test_ok(dao_mock):
        dao_mock.get_all.return_value = 0, []
        response = product_api.probe.__wrapped__(dao_mock)
        assert response == {"status_code": 200,
                            "message": "API Ready",
                            "data": {"available": 0}}

    @staticmethod
    def test_fail(dao_mock):
        dao_mock.get_all.side_effect = RuntimeError
        with raises(RuntimeError):
            product_api.probe.__wrapped__(dao_mock)
