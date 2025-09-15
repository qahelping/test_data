from faker.providers import BaseProvider
from faker import Faker

fake = Faker()

class StatusProvider(BaseProvider):
    def get_status(self) -> str:
        jira_statuses = [
            "Open",
            "In Progress",
            "Done",
            "To Do",
            "Reopened",
            "Resolved",
            "Closed",
            "In Review",
            "Pending",
            "Blocked",
            "Approved",
            "Waiting for Review",
            "Waiting for QA",
            "In Testing",
            "Failed QA",
            "Ready for Production",
            "Ready for Deployment",
            "Deployed",
            "Rejected",
            "Duplicate",
            "Won't Fix",
            "Cannot Reproduce"
        ]
        return self.random_element(jira_statuses)

fake.add_provider(StatusProvider)

fake.get_status()

def generate_user():
    return {
        'id': fake.uuid4(),
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'birth_date': fake.date_of_birth(minimum_age=18, maximum_age=90),
        'registration_date': fake.date_this_decade(),
        'is_active': fake.boolean(chance_of_getting_true=80)
    }

print(generate_user())

def generate_task(user_id=None):
    return {
        'task_id': fake.bothify('TMSG-####'),
        'responsible_id': user_id or fake.uuid4(),
        'text': fake.text(),
        'status': fake.get_status(),
        'created_at': fake.iso8601()
    }

print(generate_task())
