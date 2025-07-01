import requests

API_BASE = "https://api.example.com/sellers"

def test_create_seller_success():
    payload = {"name": "Test Seller", "email": "test@example.com"}
    r = requests.post(f"{API_BASE}/", json=payload)
    assert r.status_code == 201
    assert r.json()["id"] is not None

def test_create_seller_missing_field():
    payload = {"email": "test@example.com"}
    r = requests.post(f"{API_BASE}/", json=payload)
    assert r.status_code == 400
