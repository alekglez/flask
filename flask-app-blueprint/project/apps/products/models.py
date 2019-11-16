# -*- coding: utf-8 -*-

from project.extensions import db


class Product(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False, unique=True)
    category = db.Column(db.Unicode, unique=False)
    supplier = db.Column(db.Unicode, unique=False)
    price = db.Column(db.Float)

    @classmethod
    def create(cls, **data):
        """
        Try to create a product.
        :param data: Expected ---> name, category, supplier, price
        :return: product, error
        """

        try:
            product = cls(**data)
            db.session.add(product)
            db.session.commit()
            return product, False

        except Exception as error:
            return False, error

    @classmethod
    def update(cls, product_id, **data):
        product = cls.get_by_id(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)

            db.session.commit()
            return product, False

    @classmethod
    def get_by_id(cls, product_id):
        return cls.query.get(product_id)

    @classmethod
    def all_products(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, product_id):
        product = cls.get_by_id(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return product

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'supplier': self.supplier,
            'price': self.price
        }
