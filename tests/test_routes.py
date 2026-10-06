import unittest
from service import create_app

class AccountsRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True})
        self.client = self.app.test_client()

    def create_account(self):
        return self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@doe.com",
                "address": "123 Main St.",
                "phone_number": "555-1212",
            },
        )

    def test_create_account(self):
        response = self.create_account()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "John Doe")

    def test_list_accounts(self):
        self.create_account()
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_read_account(self):
        self.create_account()
        response = self.client.get("/accounts/1")
        self.assertEqual(response.status_code, 200)

    def test_read_missing_account(self):
        response = self.client.get("/accounts/999")
        self.assertEqual(response.status_code, 404)

    def test_update_account(self):
        self.create_account()
        response = self.client.put("/accounts/1", json={"phone_number": "555-1111"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["phone_number"], "555-1111")

    def test_update_missing_account(self):
        response = self.client.put("/accounts/999", json={"name": "Nobody"})
        self.assertEqual(response.status_code, 404)

    def test_delete_account(self):
        self.create_account()
        response = self.client.delete("/accounts/1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.client.get("/accounts").json, [])

    def test_delete_missing_account(self):
        response = self.client.delete("/accounts/999")
        self.assertEqual(response.status_code, 404)

    def test_validation(self):
        response = self.client.post("/accounts", json={"name": "Only Name"})
        self.assertEqual(response.status_code, 400)
