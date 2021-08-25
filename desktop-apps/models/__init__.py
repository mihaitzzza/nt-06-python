from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DOUBLE
from sqlalchemy.orm import relationship

SQLAlchemyBaseModel = declarative_base()


class CustomModel:
    id = Column(INTEGER, autoincrement=True, primary_key=True)


class Ingredient(SQLAlchemyBaseModel, CustomModel):
    __tablename__ = 'ingredients'
    name = Column(VARCHAR(200), unique=True, default=None)
    price = Column(DOUBLE, default=0.00)
    quantity = Column(INTEGER, default=1)
    pizza = relationship('Pizza', secondary='pizza_ingredients')


class Pizza(SQLAlchemyBaseModel, CustomModel):
    __tablename__ = 'pizza'
    name = Column(VARCHAR(200), unique=True, default=None)
    ingredients = relationship('Ingredient', secondary='pizza_ingredients')
    size = Column(INTEGER, default=32)


class PizzaIngredient(SQLAlchemyBaseModel, CustomModel):
    __tablename__ = 'pizza_ingredients'
    pizza_id = Column(INTEGER, ForeignKey(Pizza.id))
    pizza = relationship(Pizza)
    ingredient_id = Column(INTEGER, ForeignKey(Ingredient.id))
    ingredient = relationship(Ingredient)
    quantity = Column(INTEGER, default=1)
