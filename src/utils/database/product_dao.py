from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.entity.product import Product


class ProductDAO(GenericSQLDAO):
    def __init__(self, **kwargs):
        super().__init__(database_type=PostgreSQLHelper,
                         return_class=Product,
                         **kwargs)