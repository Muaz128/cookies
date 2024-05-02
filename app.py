from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

# Replace 'WEBHOOK_URL' with your actual webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1233946939075203072/-KjYETJtd8I4cmIvU8k2UIa0JA1mW5RAArFVaCmp2rlU5zv1MJ8OkoKYBNv-Awc8E1fg'

def get_cookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies
        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie.name] = cookie.value
        return cookies_dict
    except Exception as e:
        print('Error fetching cookies:', e)
        return None

def send_to_webhook():
    try:
        test_message = {'message': 'This is a test message from the proxy server'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(WEBHOOK_URL, data=json.dumps(test_message), headers=headers)
        if response.status_code != 200:
            print('Failed to send test message to webhook:', response.text)
        else:
            print('Test message sent to webhook successfully')
    except Exception as e:
        print('Error sending test message to webhook:', e)

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is missing', 400

    cookies = get_cookies(url)
    if cookies:
        send_to_webhook()
        return jsonify(cookies)
    else:
        return 'Failed to fetch cookies', 500

if __name__ == '__main__':
    send_to_webhook()
    app.run(debug=True)
