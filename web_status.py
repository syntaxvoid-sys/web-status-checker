import requests
url = input("Enter target URL (e.g., https://example.com)")

with open("wordlist.txt" , "r") as file:
    for line in file:
        path = line.strip()
        target = url + path
        response = requests.get(target)
        if response.status_code == 200:
            print(target, response)
        