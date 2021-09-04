import db_manager
from models import Category, Subcategory, Movement, MovementType, Account

def run():
    new_cat = Category("MyCategory")
    db_manager.session.add(new_cat)
    new_subcat = Subcategory("MySubcategory",new_cat)
    db_manager.session.add(new_subcat)
    new_mt = MovementType("Gasto")
    db_manager.session.add(new_mt)
    new_acct = Account("Visa Scotia")
    db_manager.session.add(new_acct)
    new_mov = Movement(new_mt, '2021-09-04', new_subcat, new_acct, 9.99, "MyDescription")
    db_manager.session.add(new_mov)
    db_manager.session.commit()

if __name__ == "__main__":
    db_manager.Base.metadata.create_all(db_manager.engine)
    run()