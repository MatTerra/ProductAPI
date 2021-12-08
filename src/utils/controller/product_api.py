from dataclasses import fields

from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api import error_response, success_response, use_dao

from utils.database.product_dao import ProductDAO
from utils.entity.product import Product


@use_dao(ProductDAO, "API Unavailable")
def probe(dao: GenericSQLDAO = None):
    total, _ = dao.get_all(length=1, offset=0, filters=None)
    return success_response(message="API Ready",
                            data={"available": total})


@use_dao(ProductDAO, "Unable to list product")
def read(length: int = 20, offset: int = 0,
         dao: GenericSQLDAO = None, **kwargs):
    filters = dict()

    entity_attributes = [field.name for field in fields(Product)]

    for key, value in kwargs.items():
        if key not in entity_attributes:
            continue

        filters[key] = value.split(',', 1) \
            if str(value).count(',') >= 1 \
               and str(value).split(',')[0] in \
               dao.database.ALLOWED_COMPARATORS \
            else value

    total, results = dao.get_all(length=length, offset=offset,
                                 filters=filters if filters else None)
    return success_response(message="List of products",
                            data={"total": total,
                                  "results": [result.simple_visualization()
                                              for result
                                              in results]})


@use_dao(ProductDAO, "Unable to retrieve product")
def read_one(id_: str, dao: GenericSQLDAO = None):
    result = dao.get(id_=id_)

    if not result:
        return success_response(status_code=404,
                                message="Product not found in database",
                                data={"id_": id_})

    return success_response(message="Product retrieved",
                            data={"Product": dict(result)})


@use_dao(ProductDAO, "Unable to create product")
def create(entity: dict, dao: GenericSQLDAO = None):
    entity_to_create = Product(**entity)

    dao.create(entity=entity_to_create)

    return success_response(message="Product created",
                            data={"Product": dict(entity_to_create)})


@use_dao(ProductDAO, "Unable to update product")
def update(id_: str, entity: dict, dao: GenericSQLDAO = None):
    entity_to_update = dao.get(id_)

    if not entity_to_update:
        return error_response(status_code=404,
                              message="Product not found",
                              data={"id_": id_})

    entity_fields = dao.fields.keys()

    for key, value in entity.items():
        if key not in entity_fields:
            raise KeyError("{key} not in {entity}"
                           .format(key=key,
                                   entity=dao.return_class))

        entity_to_update.__dict__[key] = value

    dao.update(entity_to_update)

    return success_response(message="Product updated",
                            data={"Product": dict(entity_to_update)})


@use_dao(ProductDAO, "Unable to delete product")
def delete(id_: str, dao: GenericSQLDAO):
    entity = dao.get(id_=id_)

    if not entity:
        return error_response(status_code=404,
                              message="Product not found",
                              data={"id_": id_})

    dao.remove(entity)

    return success_response(message="Product deleted",
                            data={"Product": dict(entity)})
