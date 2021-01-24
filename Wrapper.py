import requests
import json


class gab():
    def __init__(self, token=None):
        self.token = token
        self.headers = {
                        "Accept":"application/json",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
                        }
        self.auth_head = self.headers
        self.auth_head["__cfduid"] = token
        self.base = "https://gab.com/api/v1/"

    def get_timeline(self):
        url = self.base + "timelines/explore"
        r = requests.get(url, headers=self.headers)
        data = json.loads(r.content)
        return data

def main():
    creds = json.load(open("creds.json", "r"))
    api = gab(creds["token"])
    x = api.get_timeline()
    json.dump(x, open("out.json", "w"))


if __name__ == '__main__':
    main()
