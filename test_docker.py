import requests

def test_root():
    r = requests.get("http://localhost:8080")
    print("Status:", r.status_code)
    print("Response:", r.json())

if __name__ == "__main__":
    test_root()
