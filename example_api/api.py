from flask import Flask, request, jsonify

app = Flask(import_name='example-api')

#110 Cyber, 135 Ratanious
allowed_users = ['110', '135']

@app.route('/hello')
def hello():
    user = request.args.get('user')
    print(user)
    if user is None:
        text = "Invalid user. Open a ticket and request a developer."
    else:
        found = False
        for x in allowed_users:
            if x == user:
                found = True
                break
        if not found:
            text = "User is not allowed."
        else:
            name = request.args.get('name')
            if name is None:
                text = 'Hello.'
            else:
                text = ("Hello %s!" % name)
    return jsonify(text)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
