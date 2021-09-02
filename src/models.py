import db_manager
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

class Category(db_manager.Base):
    
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    create_date = Column(Date)
    subcategories = relationship("Subcategory", back_populates="category")
    

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Category::{self.name}>'
    def __str__(self):
        return self.name

class Subcategory(db_manager.Base):
    
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="subcategories")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Subcategory::{self.name}>'
    def __str__(self):
        return self.name