from flask import Flask
import math2
app = Flask(__name__)

@app.route('/')
def hello():
    variable = math2.add()
    return 'Hello World! C est moi Benoit!' + variable

if __name__ == '__main__':
    app.run(debug=True)