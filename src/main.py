import db_manager
from models import Category, Subcategory, Movement, MovementType

def run():
    new_cat = Category("MyCategory")
    db_manager.session.add(new_cat)
    new_subcat = Subcategory("MySubcategory",new_cat)
    db_manager.session.add(new_subcat)
    new_mt = MovementType("Gasto")
    db_manager.session.add(new_mt)
    new_mov = Movement(new_mt, '2021-09-04', new_subcat, new_cat)
    db_manager.session.add(new_mt)
    db_manager.session.commit()

if __name__ == "__main__":
    db_manager.Base.metadata.create_all(db_manager.engine)
    run()