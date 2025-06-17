import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    'name': 'example',
    'created_at': datetime.now()
}

json_string = json.dumps(data, cls=CustomEncoder, indent=4)
print(json_string)