import requests, time, json, os
from authlib.jose import jwt

KEY_ID = os.environ['APPLE_KEY_ID']
ISSUER_ID = os.environ['APPLE_ISSUER_ID']
PATH_TO_KEY = os.environ['APPLE_PATH_TO_KEY']
EXPIRATION_TIME = int(round(time.time() + (20.0 * 60.0))) # 20 minutes timestamp (do not inscrease!)

with open(PATH_TO_KEY, 'r') as f:
    PRIVATE_KEY = f.read()

header = {
    "alg": "ES256",
    "kid": KEY_ID,
    "typ": "JWT"
}

payload = {
    "iss": ISSUER_ID,
    "exp": EXPIRATION_TIME,
    "aud": "appstoreconnect-v1"
}

# Create the JWT
token = jwt.encode(header, payload, PRIVATE_KEY)

# API Request
JWT = 'Bearer ' + token.decode()
URL = 'https://api.appstoreconnect.apple.com/v1/apps'
HEAD = {'Authorization': JWT}

r = requests.get(URL, params={'limit': 200}, headers=HEAD)

# Write the response in a pretty printed JSON file
with open('output.json', 'w') as out:
    out.write(json.dumps(r.json(), indent=4))

for app in r.json()["data"]:
    versions = requests.get(app["relationships"]["appStoreVersions"]["links"]["related"], headers=HEAD)
    print("******{}******".format(app["attributes"]["name"]))
    for version in versions.json()["data"]:
        print("Version", version["attributes"]["versionString"])
    print("")
    