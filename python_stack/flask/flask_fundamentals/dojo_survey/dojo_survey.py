from flask import Flask, render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def survey():
    name= request.form['name']
    location = request.form['location']
    lang=request.form['lang']
    comment=request.form['comment']
    return render_template('result.html',name=name, location=location, lang=lang, comment=comment)


    
if __name__=="__main__":
    app.run(debug=True)
