import db_manager
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

class Category(db_manager.Base):
    
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    subcategories = relationship("Subcategory", back_populates="category")

    def __init__(self, name, description=None):
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
    movements = relationship("Movement", back_populates="subcategory")

    def __init__(self, name, category, description=None):
        self.name = name
        self.description = description
        self.category = category

    def __repr__(self):
        return f'<Subcategory::{self.name}>'
    def __str__(self):
        return self.name

class MovementType(db_manager.Base):
    
    __tablename__ = 'movement_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    movements = relationship("Movement", back_populates="movement_type")
    
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<MovementType::{self.name}>'
    def __str__(self):
        return self.name

class Account(db_manager.Base):
    
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    movements = relationship("Movement", back_populates="account")
    
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Account::{self.name}>'
    def __str__(self):
        return self.name

class Movement(db_manager.Base):
    
    __tablename__ = 'movement'

    id = Column(Integer, primary_key=True)
    movement_type_id = Column(Integer, ForeignKey('movement_type.id'))
    movement_type = relationship("MovementType", back_populates="movements")
    date = Column(Date, nullable=False)
    description = Column(String)
    subcategory_id = Column(Integer, ForeignKey('subcategory.id'))
    subcategory = relationship("Subcategory", back_populates="movements")
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="movements")
    value = Column(Float, nullable=False)
    

    def __init__(self, movement_type, date, subcategory, account, value, description=None):
        self.description = description
        self.subcategory = subcategory
        self.movement_type = movement_type
        self.date = date
        self.account = account
        self.value = value

    def __repr__(self):
        return f'<Movement::{self.description}>'
    def __str__(self):
        return self.description