from unittest.mock import Mock

from tests.unittests.test_product_api import success_response, dao_mock
from utils.controller import product_api
from utils.entity.product import Product


class TestRead:
    @staticmethod
    def test_read_one_no_filter(dao_mock: Mock):
        product = Product()
        dao_mock.get_all.return_value = 1, [product]
        response = product_api.read.__wrapped__(dao=dao_mock)
        dao_mock.get_all.assert_called_with(length=20, offset=0,
                                            filters=None)

        assert response == {"status_code": 200,
                            "message": "List of products",
                            "data": {"total": 1,
                                     "results": [{"id_": product.id_,
                                                  "cota_price": product.cota_price,
                                                  "remaining_cotas": product.remaining_cotas,
                                                  "name": product.name,
                                                  "picture_url": product.picture_url}]}}
