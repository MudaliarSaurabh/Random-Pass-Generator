from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "hello,world"

if __name__=="__main__":#if  statement is provoked using python command
  app.run(host='0.0.0.0',debug=True)