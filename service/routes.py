from flask import Blueprint, jsonify, request
from .models import Account

accounts_bp = Blueprint("accounts", __name__)
REQUIRED = ("name", "email", "address")

@accounts_bp.post("/accounts")
def create_account():
    data = request.get_json(silent=True) or {}
    missing = [field for field in REQUIRED if not data.get(field)]
    if missing:
        return jsonify(error="Missing required fields", fields=missing), 400
    return jsonify(Account.create(data).to_dict()), 201

@accounts_bp.get("/accounts")
def list_accounts():
    return jsonify([account.to_dict() for account in Account.all()]), 200

@accounts_bp.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = Account.find(account_id)
    if not account:
        return jsonify(error="Account not found"), 404
    return jsonify(account.to_dict()), 200

@accounts_bp.put("/accounts/<int:account_id>")
def update_account(account_id):
    account = Account.find(account_id)
    if not account:
        return jsonify(error="Account not found"), 404
    data = request.get_json(silent=True) or {}
    for field in ("name", "email", "address", "phone_number"):
        if field in data:
            setattr(account, field, data[field])
    return jsonify(account.to_dict()), 200

@accounts_bp.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    account = Account.delete(account_id)
    if not account:
        return jsonify(error="Account not found"), 404
    return "", 204
