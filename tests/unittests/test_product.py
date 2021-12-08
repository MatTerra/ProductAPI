from pytest import mark

from utils.entity.product import Product


class TestProduct:
    @staticmethod
    @mark.parametrize("cotas", [
        1,
        5,
        10
    ])
    def test_remaining_cotas_init(cotas):
        product = Product(cotas=cotas)
        assert product.remaining_cotas == cotas

    @staticmethod
    def test_simple_visualization():
        product = Product()
        vis = product.simple_visualization()
        assert vis == {"id_": product.id_,
                       "cota_price": product.cota_price,
                       "remaining_cotas": product.remaining_cotas,
                       "name": product.name,
                       "picture_url": product.picture_url}
