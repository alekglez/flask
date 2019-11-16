# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from .models import Product


products = Blueprint('products', __name__, url_prefix='/')


@products.route('/products/', methods=['GET'])
@products.route('/products/<product_id>', methods=['GET'])
def get(product_id=None, **kwargs):
    if not product_id:
        return jsonify([product.as_dict() for product in Product.all_products()]), 200

    product = Product.get_by_id(product_id)
    return jsonify(product and product.as_dict()), 200 if product else 204


@products.route('/products/', methods=['POST'])
def post(**kwargs):
    return _create_or_update('create', **kwargs)


@products.route('/products/<product_id>', methods=['PUT'])
def put(product_id, **kwargs):
    return _create_or_update('update', product_id=product_id, **kwargs)


@products.route('/products/<product_id>', methods=['DELETE'])
def delete(product_id, **kwargs):
    try:
        product = Product.delete(product_id)
        return jsonify(product and product.as_dict()), 200 if product else 204

    except Exception as error:
        return return_error(str(error))


def _create_or_update(method, *args, **kwargs):
    data = request.json
    if not data:
        return return_error('No data provided!')

    data.update(**kwargs)

    try:
        product, error = getattr(Product, method)(*args, **data)
        if error:
            return return_error(str(error))

        return jsonify(product.as_dict()), 200

    except Exception as error:
        return return_error(str(error))


def return_error(msg='An error occurred!'):
    return jsonify({'error': msg}), 400
