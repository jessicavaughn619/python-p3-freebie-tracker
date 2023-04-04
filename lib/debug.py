#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Company, Dev, Freebie)

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# Company.freebies
    first_company = session.query(Company).first()
    company_freebies = session.query(Freebie).filter_by(company_id=first_company.id)
    # print([record for record in company_freebies])

# Company.devs
    first_company_freebies = session.query(Freebie).filter_by(company_id=first_company.id).first()
    company_devs = session.query(Dev).filter_by(id=first_company_freebies.id)
    # print([record for record in company_devs])

# Dev.freebies
    first_dev = session.query(Dev).first()
    dev_freebies = session.query(Freebie).filter_by(dev_id=first_dev.id)
    # print([record for record in dev_freebies])

# Dev.companies
    first_dev_freebies = session.query(Freebie).filter_by(dev_id=first_dev.id).first()
    # print([record for record in first_dev_freebies])
    dev_companies = session.query(Company).filter_by(id=first_dev_freebies.id)
    # print([record for record in dev_companies])

# Freebie.dev
    dev = session.query(Freebie.dev)
    
# Freebie.company
    company = session.query(Freebie.company)

# # Freebie aggregates
#     def print_details():
#         freebie = session.query(Freebie).first()
#         print(f"{freebie.dev.name} owns a {freebie.item_name} from {freebie.company.name}.")

# # Company aggregates
#     def give_freebie(dev, item_name, value):
#         company = session.query(Company).filter_by(id=dev).first()
#         freebie = Freebie(
#             item_name=item_name,
#             value=value,
#             company_id=company.id,
#             dev_id=dev
#         )
#         session.add(freebie)
#         session.commit()

    # @classmethod 
    # def oldest_company():
    #     companies_by_age = [record for record in session.query(Company).order_by(Company.founding_year.desc())]
    #     first = companies_by_age[0]
    #     return first

# # Dev aggregates
#     def received_one(item_name):
#         for item_name in dev:
#             if item_name == item_name:
#                 return True
#             return False

    def give_away(self, dev, freebie):
        my_freebies = [record for record in session.query(Freebie).filter_by(dev_id=self.id)]
        if freebie in my_freebies:
            freebie.dev = dev








    import ipdb; ipdb.set_trace()
