from kaggle.api.kaggle_api_extended import KaggleApi
import datetime, os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Refresh credentials
os.chdir('./Creds')
gauth = GoogleAuth()
credential_file = 'gdrive.txt'
gauth.LocalWebserverAuth()
gauth.SaveCredentialsFile(credential_file)

#Update Dataset
api = KaggleApi()
api.authenticate()
api.dataset_metadata("YourName/YourDataset",".")
api.dataset_create_version(".", version_notes=f"Updated on {datetime.datetime.now().strftime('%Y-%m-%d')}")
