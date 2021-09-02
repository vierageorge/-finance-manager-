import db_manager
from models import Category, Subcategory

def run():
    pass

if __name__ == "__main__":
    db_manager.Base.metadata.create_all(db_manager.engine)
    run()