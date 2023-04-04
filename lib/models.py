from sqlalchemy import (ForeignKey, Column, Integer, String, MetaData, PrimaryKeyConstraint)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

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

    freebies = relationship("Freebie", backref=backref("company"))
    devs = association_proxy('freebies', 'dev', creator=lambda dv: Freebie(dev=dv))
    
    
    def __repr__(self):
        return f'Id: {self.id} ' \
            + f'Company: {self.name} ' \
            + f'Founding Year: {self.founding_year}'
    
    def give_freebie(session, dev, item_name, value):
        company = session.query(Company).filter_by(id=dev).first()
        freebie = Freebie(
            item_name=item_name,
            value=value,
            company_id=company.id,
            dev_id=dev
        )
        session.add(freebie)
        session.commit()

    @classmethod
    def oldest_company(session):
        companies_by_age = [record for record in session.query(Company).order_by(Company.founding_year.desc())]
        first = companies_by_age[0]
        return first    



class Dev(Base):
    __tablename__ = 'devs'
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    name= Column(String())

    def __repr__(self):
        return f'Id: {self.id} ' \
            + f'Name: {self.name}'
    
    freebies = relationship("Freebie", backref="dev")
    companies = association_proxy("freebies", "company", creator=lambda cp: Freebie(company=cp))

    def received_one(item_name):
        for item_name in Dev:
            if item_name == item_name:
                return True
            return False

    def give_away(dev, freebie, session):
        my_freebies = [record for record in session.query(Freebie).filter_by(dev_id=self.id)]
        if freebie in my_freebies:
            freebie.dev = dev




    
class Freebie(Base):
   __tablename__ = "freebies"
   __table_args__ = (PrimaryKeyConstraint("id"), )

   id = Column(Integer())
   item_name = Column(String())
   value = Column(Integer())
   company_id = Column(Integer(), ForeignKey("companies.id"))
   dev_id = Column(Integer(), ForeignKey("devs.id"))

   def __repr__(self):
       return f'Id: {self.id} '\
        + f'Name: {self.item_name} ' \
        + f'Value: {self.value}'
   
   def print_details(session):
        freebie = session.query(Freebie).first()
        return (f"{freebie.dev.name} owns a {freebie.item_name} from {freebie.company.name}.")
   