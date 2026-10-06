from datetime import datetime, timezone

class Account:
    _records = {}
    _next_id = 1

    def __init__(self, name, email, address, phone_number=None, account_id=None):
        self.id = account_id
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.date_joined = datetime.now(timezone.utc).date().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
            "date_joined": self.date_joined,
        }

    @classmethod
    def reset(cls):
        cls._records = {}
        cls._next_id = 1

    @classmethod
    def create(cls, data):
        account = cls(data["name"], data["email"], data["address"], data.get("phone_number"))
        account.id = cls._next_id
        cls._next_id += 1
        cls._records[account.id] = account
        return account

    @classmethod
    def find(cls, account_id):
        return cls._records.get(account_id)

    @classmethod
    def all(cls):
        return list(cls._records.values())

    @classmethod
    def delete(cls, account_id):
        return cls._records.pop(account_id, None)
