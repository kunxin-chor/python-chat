from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


messages = []

@app.route("/")
def index():
    print(messages)
    return render_template('index.html', messages=messages)
    
@app.route("/", methods=['POST'])
def save_message():
    username = request.form.get("username")
    msg = request.form.get("message")
    # store the username/message into a dictionary
    posting = {
        'username' : username,
        'message' : msg
    }
    messages.append(posting)
    return redirect('/')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)