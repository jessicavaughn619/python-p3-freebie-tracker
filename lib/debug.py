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

# Dev.freebies
    first_dev = session.query(Dev).first()
    dev_freebies = session.query(Freebie).filter_by(dev_id=first_dev.id)
    print([record for record in dev_freebies])

# Dev.companies

# Freebie.dev
    dev = session.query(Freebie.dev)
    
# Freebie.company
    company = session.query(Freebie.company)







    import ipdb; ipdb.set_trace()
