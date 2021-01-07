from flask import Flask
app = Flask(__name__)
from parser_vk_bot import parser

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()