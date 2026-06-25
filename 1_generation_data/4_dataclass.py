from dataclasses import dataclass
from datetime import date

from faker import Faker


@dataclass
class User:
    id: str
    name: str
    email: str
    phone: str
    address: str
    birth_date: date
    registration_date: date
    is_active: bool

    @classmethod
    def generate_data(cls):
        fake = Faker()

        return cls(
            id=fake.uuid4(),
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=90),
            registration_date=fake.date_this_decade(),
            is_active=fake.boolean(chance_of_getting_true=80)
        )


user1 = User.generate_data()
print(user1.address)
user2 = User.generate_data()
print(user2.address)
