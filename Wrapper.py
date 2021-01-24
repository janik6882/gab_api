import requests
import json


class gab():
    def __init__(self, token=None):
        self.token = token
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': token,
        }
        self.auth_head = self.headers
        self.auth_head["Authorization"] = token
        self.base = "https://gab.com/api/v1/"
        self.s = requests.Session()
        self.s_auth = requests.Session()
        self.s.headers.update(self.headers)
        self.s_auth.headers.update(self.auth_head)

    def get_timeline(self):
        url = self.base + "timelines/explore"
        params = {}
        r = self.s.get(url, headers=self.headers)
        data = json.loads(r.content)
        return data

    def get_followers(self, id, maxId=None, limit=None, pos=None):
        # maximum for limit is 25, everything above will count as 25
        temp_url = self.base + "accounts/{UserId}/followers"
        url = temp_url.format(UserId=id)
        params = {
                "limit": limit,
                "max_id": maxId,
                "pos": pos,
        }
        r = self.s_auth.get(url, params=params)
        data = json.loads(r.content)
        return data

    def get_following(self, id, maxId=None, limit=None, pos=None):
        # maximum for limit is 25, everything above will go as 25
        temp_url = self.base + "accounts/{userId}/following"
        url = temp_url.format(userId=id)
        params = {
                  "limit": limit,
                  "pos": pos,
                  "max_id": maxId,
                }
        r = self.s_auth.get(url, params=params)
        print (r.content)
        data = json.loads(r.content)
        return data

    def get_statuses(self, id, pinned=None, limit=None, pos=None):
        # max limit 25
        temp_url = self.base + "accounts/{userId}/statuses"
        url = temp_url.format(userId=id)
        params = {
                 "pinned": pinned,
                 "limit": limit,
                 "pos": pos,
                }
        r = self.s_auth.get(url, params=params)
        data = json.loads(r.content)
        return data


def main():
    creds = json.load(open("creds.json", "r"))
    input = json.load(open("input.json", "r"))
    api = gab(creds["token"])
    x = api.get_statuses(input["id"], limit=50, pos=500)
    print (x)
    print (len(x))
    json.dump(x, open("out.json", "w"))


if __name__ == '__main__':
    main()
