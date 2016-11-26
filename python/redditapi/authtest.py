import requests
import argparse
import requests.auth

auth_url = "https://www.reddit.com/api/v1/access_token"

parser = argparse.ArgumentParser(description='Your delicious reddity details')
parser.add_argument('user', help='Your reddit username)')
parser.add_argument('password', help='Your reddit password')
parser.add_argument('clientid', help='Reddit api client id')
parser.add_argument('secretkey', help='Reddit api secret key')
args = parser.parse_args()

user=args.user
password=args.password
client_id=args.clientid
secret_key=args.secretkey
client_auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
headers = {"User-Agent": "ChangeMeClient/0.1 by OhDearMoshe"}
post_data = {"grant_type": "password", "username": user, "password": password}

auth_string="grant_type=password&username=%s&password=%s" % (user, password)
r = requests.post(auth_url, auth=client_auth, data=post_data, headers=headers)
access_token = r.json()['access_token']
headers["Authorization"] = "bearer %s" % access_token
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
print response.json()

thread_create = {
    "title" : "test2",
    "text" : "test",
    "kind" : "self",
    "sr" : "expodm"
}

response = requests.post("https://oauth.reddit.com/api/submit", headers=headers, data=thread_create)
print response.json()
