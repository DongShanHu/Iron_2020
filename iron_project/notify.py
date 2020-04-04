
import requests
from flask import Flask, jsonify, request
app = Flask(__name__)

client_id = '	UdyS7Ci1cMhm9Esdt1dMO7'
callback_url = 'http://127.0.0.1:5000/callback'
URL = f'https://notify-bot.line.me/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={callback_url}&scope=notify&state=NO_STATE'
print(URL)


code = 's0YkgYvR8O4JG6oQXji3Tw'
client_secret = 'tatlHnvLtlpkA1sXVLyJBnDnCX0PdnsrOQutBt7VnQY'
headers = {
    'Content-type': 'application/x-www-form-urlencoded'
}

payload = {
    'code': code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': callback_url,
    'grant_type': 'authorization_code'
}
token = 'RmId9D93wRmhJkHN3Ja2PfJepjAL3bPj75TWGu9aVQe'
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {token}'
}

payload = {
    'message': 'Hello World',
}

res = requests.post('https://notify-api.line.me/api/notify',
                    data=payload, headers=headers)
res = requests.post('https://notify-bot.line.me/oauth/token',
                    data=payload, headers=headers)


@app.route("/callback")
def callback():
    return jsonify({'data': request.url})


if __name__ == "__main__":
    app.run()
