# mobile-apps-versions
python scripts for fetching apple/google dev apis

# Install
- Please install pipenv: `pip3 install pipenv`
- Install dependencies: `pipenv install`
- Write environment variables in .env file

```
GOOGLE_PACKAGE_NAMES=abc.developer.name1,abcd.other.name3
GOOGLE_PATH_TO_SA_FILE=service_account_file.json
APPLE_KEY_ID=123ABC123A
APPLE_ISSUER_ID=123aze-123a-123aze-123a-123aze
APPLE_PATH_TO_KEY=./apple_key_file.p8
```

# Run
- To retrieve iOS apps versions, please run `pipenv run ios`
- To retrieve android apps versions, please run `pipenv run android`
