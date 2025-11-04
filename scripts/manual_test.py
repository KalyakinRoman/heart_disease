import requests
import json


def main():
    data = json.load(open("data/example_request.json"))
    response = requests.post("http://localhost:8000/prediction", json=data)
    print(response.json())

if __name__ == "__main__":
    main()