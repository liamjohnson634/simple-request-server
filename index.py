from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/open-secret')
def opensecret():
  return "keep calm and carry on"

@app.route('/pick-the-secret')
def pickthesecret():
  return render_template('pick-the-secret.html')

if __name__ == '__main__':
  app.run(debug=True) 