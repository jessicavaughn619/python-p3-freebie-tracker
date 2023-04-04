from sqlalchemy import (ForeignKey, Column, Integer, String, MetaData, PrimaryKeyConstraint)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    name = Column(String())
    founding_year = Column(Integer())
    
    def __repr__(self):
        return f'Id: {self.id} ' \
            + f'Company: {self.name} ' \
            + f'Founding Year: {self.founding_year}'

class Dev(Base):
    __tablename__ = 'devs'
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    name= Column(String())

    def __repr__(self):
        return f'Id: {self.id} ' \
            + f'Name: {self.name}'
    
class Freebie(Base):
   __tablename__ = "freebies"
   __table_args__ = (PrimaryKeyConstraint("id"), )

   id = Column(Integer())
   item_name = Column(String())
   value = Column(Integer())
   company_id = Column(Integer(), ForeignKey("companies.id"))
   dev_id = Column(Integer(), ForeignKey("devs.id"))
   
   company = relationship("Company", backref=backref("companies"))
   dev = relationship("Dev", backref=backref("devs"))

   def __repr__(self):
       return f'Id: {self.id} '\
        + f'Name: {self.item_name} ' \
        + f'Value: {self.value}'
   