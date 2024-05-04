from database import db
from peewee import *


class Category(Model):
    categoryID = IntegerField(primary_key=True)
    categoryName = TextField()

    class Meta:
        database = db
        table_name = 'category'

    @staticmethod
    def create_category(categoryName):
        return Category.create(categoryName=categoryName)

    @staticmethod
    def read_category(categoryID):
        return Category.select().where(Category.categoryID == categoryID).get()

    @staticmethod
    def update_category(categoryID, categoryName):
        return Category.update(categoryName=categoryName).where(Category.categoryID == categoryID).execute()

    @staticmethod
    def delete_category(categoryID):
        return Category.delete().where(Category.categoryID == categoryID).execute()