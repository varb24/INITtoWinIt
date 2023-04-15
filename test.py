#Don't publish to main!
#UPloads a file to a web address.
import requests

#endpoint we want to upload the file to
url = 'https://example.com/upload'
#open contains the file we want to uploads
#The key of the dictionary should match the name of the field in the HTML form that accepts file uploads.
files = {'file': open('filename.txt', 'rb')}

response = requests.post(url, files=files)

print(response.text)