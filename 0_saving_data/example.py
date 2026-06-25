from enum import Enum

CURRENCY_USD = 'usd'

data = {"name": 'Alex', 'age': 33}

print(CURRENCY_USD)
print(data['name'])


class Protocol(str, Enum):
    """Network protocols."""

    HTTP = "http"
    HTTPS = "https"


print(Protocol.HTTP.value)