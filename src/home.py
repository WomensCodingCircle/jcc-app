from flask import Flask

app = Flask(__name__)
app.jinja_env.auto_reload = True

@app.route('/')
def landing_page():
   return 'Hello, this is the JCC Web application!'

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=9999, use_reloader=True)