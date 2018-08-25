import sys
import random
import hashlib
from flask import render_template
from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

# set app secret
app.secret_key = b'my secret toilet'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/open-secret')
def opensecret():
  return "keep calm and have fun"

@app.route('/pick-the-secret')
def pickthesecret():
  return render_template('pick-the-secret.html')

@app.route('/changing-secret')
def changingsecret():
  m = hashlib.sha256()
  m.update(str(random.random()).encode('ascii'))
  return m.hexdigest()

@app.route('/your-session-secret')
def yoursessionsecret():
  m = hashlib.sha256()
  m.update(str(random.random()).encode('ascii'))

  if session.get('your-session-secret', 0) == 0:
    session['your-session-secret'] = m.hexdigest()

  return session.get('your-session-secret')

@app.route('/choose-session-secret', methods=['GET'])
def choosesessionsecretform():
  return render_template('choose-session-secret.html')

@app.route('/choose-session-secret', methods=['POST'])
def choosesessionsecretput():
  session['chosen-session-secret'] = request.form['chosen-session-secret']
  return redirect(url_for('chosensessionsecret'))

@app.route('/chosen-session-secret')
def chosensessionsecret():
  return session.get('chosen-session-secret', 'No Session Secret Chosen')

if __name__ == '__main__':
  app.run(debug=True) 