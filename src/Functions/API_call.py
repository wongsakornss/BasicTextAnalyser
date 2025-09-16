import requests

def fetch_text_from_api():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5, verify=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("content", "")
        else:
            print(f"API Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None