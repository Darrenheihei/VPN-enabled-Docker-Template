import requests
from dotenv import load_dotenv
import os

load_dotenv('.env.app')

def check_ip():
    print("env variables:")
    print("foo:", os.getenv("foo"))

    try:
        response = requests.get('https://httpbin.org/ip')
        print(f"Current Public IP: {response.json()['origin']}")
    except Exception as e:
        print(f"Connection failed (VPN might be down): {e}")

if __name__ == "__main__":
    check_ip()
    # Your script logic here...