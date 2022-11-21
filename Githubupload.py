import requests 
import base64

token = "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"

repo = 'ktarkowski3/twitterHandles'
path = r'Marlin_Yield.json'
#This will change depending on which json file you want to use from previous py a.k.a 1inch_Mdextech.json or Marlin_Yield.json

data = open("Marlin_Yield.json", "r").read()

r = requests.put(
    f'https://api.github.com/repos/{repo}/contents/{path}',
    headers = {
        'Authorization': f'Token {token}'
    },
    json = {
        "message": "add new file",
        "content": base64.b64encode(data.encode()).decode(),
        "branch": "master"
    }
)
print(r.status_code)
print(r.json())
