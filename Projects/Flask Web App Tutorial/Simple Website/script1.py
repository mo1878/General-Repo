# import Flask Class from flask library
from flask import Flask, render_template 


# app variable used to store the flask object: instantiating
app = Flask(__name__)

@app.route('/homepage/') # Decorator 
def home():
    return render_template('home.html')

@app.route('/about/') # Decorator 
def about():
    return render_template('about.html')

if __name__ == '__main__': # If __name__ == '__main__' the run the app, which is true when theh script is run
    app.run(debug=True) # if this script is imported to another script then this will not be true 
