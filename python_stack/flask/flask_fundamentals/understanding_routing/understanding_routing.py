from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return"Hello World!"
@app.route('/dojo')
def callDojo():
    return"Dojo"

@app.route('/say/<name>')
def callname(name):
    return"Hi "+name+"!"

@app.route('/repeat/<int:num>/<word>')
def callname1(num, word):
    x=""
    for i in range (int(num)):
        x +="<p>"+ word +"</p>"
    return x

@app.errorhandler(404)
def handle_bad_request(e):
    return f'bad request!{404}'
    

if __name__=="__main__":
    app.run(debug=True)