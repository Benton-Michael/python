from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():

    return render_template('index.html')
    # returns Hello Flask within the h1 section of index.html


@app.route('/success')            
def success():
    return "Success"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<nameSay>')
def say(nameSay):
    print(nameSay)
    return "Hi, " + nameSay

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

@app.route('/hello')
def helloBro():                 # using the name helloBro for this method because the one below is already named hello() like Kyle showed me
    return "Hey Bro!"

@app.route('/hello/<name>') # the variable name here is arbitrary ( we could use banana instead of name)
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


