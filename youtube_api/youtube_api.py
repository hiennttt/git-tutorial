from googleapiclient.discovery import build

api_key = 'AIzaSyAZ3-DvipL_pytGusuI4kvxeOGehbA5ZOI'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()

print(response)