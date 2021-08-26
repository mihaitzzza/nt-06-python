from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Pizza, PizzaIngredient, Ingredient

engine = create_engine('mysql+mysqldb://root:Mihai10!@localhost:3306/nt_06_desktop_app')
Session = sessionmaker(engine)


def create_pizza(name):
    with Session() as session:
        pizza = Pizza(name=name)
        session.add(pizza)
        session.commit()


def get_pizza_list():
    with Session() as session:
        pizza_list = session.query(Pizza).all()
        # pizza_list = session.query(Pizza).join(PizzaIngredient.pizza_id == Pizza.id).join(Ingredient, Ingredient.id == PizzaIngredient.ingredient_id).filter(Ingredient.name.contains('abc')).all()
        # pizza_list = session.query(Pizza).filter(Pizza.name.contains('Pizza')).all()
        # pizza_list = session.query(Pizza).filter(Pizza.id > 5).all()
        return pizza_list
