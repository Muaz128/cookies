from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

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
    
    # Return cookies as JSON response
    return jsonify(cookies_dict)

if __name__ == '__main__':
    app.run(debug=True)
