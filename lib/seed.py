#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
import random

from models import (Company, Freebie, Dev)

if __name__ == "__main__":
    engine = create_engine("sqlite:///freebies.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()
    
    fake = Faker()

# Create fake companies
    companies = []

    for _ in range(3):
        company = Company(
            name=fake.company(),
            founding_year=random.randint(1950, 2022)
        )

        session.add(company)
        session.commit()

        companies.append(company)

# Create fake devs

    devs = []

    for _ in range(5):
        dev = Dev(
            name=f'{fake.first_name()} {fake.last_name()}'
        )

        session.add(dev)
        session.commit()

        devs.append(dev)

# Create fake freebies

    cool_items = ["Pencil", "Lanyard", "Notebook", "Backback", "Coozie", "Sticker"]

    freebies = []

    for company in companies:
        for _ in range(random.randint(1, 2)):
            freebie = Freebie(
                item_name=random.choice(cool_items),
                value=random.randint(1, 100),
                company_id=company.id,
                dev_id=random.randint(1, 5)
            )

            freebies.append(freebie)

            session.bulk_save_objects(freebies)
            session.commit()
        
    session.commit()
    session.close()