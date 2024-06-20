from flask import Flask, render_template
from flask_socketio import SocketIO, send
import requests
import json
app = Flask(__name__)
app.config['SECRET'] = 'secrect123'
socketio = SocketIO(app, cors_allowed_origins='*')

# Global variable to store the token
token = None

def login_and_get_token(username, password):
    url = "http://127.0.0.1:8080/api/auth/login"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        global token
        token = response.json().get('token')
        print("Token received and saved:", token)
    else:
        print("Error logging in:", response.text)

@socketio.on('message')
def handle_message(data):
    print(data)
    print(type(data))
    
    if isinstance(data, str):
        try:
            data = json.loads(data) 
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return  

    answer = data.get('answer')
    chat_id = data.get('chat_id')
    typeM = data.get('type')

    print("answer:", answer)
    send(data, broadcast=True)

    if typeM == "q":
        url = "http://127.0.0.1:8080/api/chat/message"
        headers = {'Authorization': f'Bearer {token}'}
        data = {"content": answer, "chat_id": chat_id}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            print("Message saved successfully")
        else:
            print("Error saving message:", response.json())
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':

    login_and_get_token('chatbot', '12345678')
    socketio.run(app, host="localhost")
