from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return "hi"

@app.route('/<variable>')
def index_variable(variable):
    return "you gave variable "+str(variable)


app.run(debug=True,host='0.0.0.0')
