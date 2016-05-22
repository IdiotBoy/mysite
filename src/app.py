from flask import Flask
from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
  return send_from_directory("src/static", "index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80, debug=True)
  #app.run(debug=True)
