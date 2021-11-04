from googleapiclient import discovery
from google.oauth2 import service_account
import os

package_names_str = os.environ['GOOGLE_PACKAGE_NAMES']
sa_file = os.environ['GOOGLE_PATH_TO_SA_FILE']

package_names = str.split(package_names_str, ",")


scopes = ['https://www.googleapis.com/auth/androidpublisher']


credentials = service_account.Credentials.from_service_account_file(sa_file, scopes=scopes)

service = discovery.build('androidpublisher', 'v3', credentials=credentials)

for package_name in package_names:
    request = service.edits().insert(packageName=package_name)
    response = request.execute()
    editId = response['id']
    request = service.edits().tracks().list(packageName=package_name, editId=editId)
    response = request.execute()
    print(package_name)
    for track in response["tracks"]:
        print(track["track"])
        for release in track["releases"]:
            if release["status"] != 'draft':
                print("Release", release["name"])
            if release["status"] == 'inProgress':
                print('Release in progress!')
                print("User Fraction", release["userFraction"])
    print("")
    print("***************")
    print("")
