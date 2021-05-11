from flask import Flask,render_template
app = Flask(__name__) 

@app.route("/")
def blocks ():
    return render_template('board.html',num_row=8, num_col=8) 

@app.route("/<int:x>/<int:y>/")
def blocks2 (x=8,y=8):
    return render_template('board.html',num_row=x, num_col=y) 

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def colors (x,y,color1,color2):
    return render_template('board.html',num_row=x, num_col=y,color1=color1,color2=color2)



if __name__== '__main__':
    app.run(debug=True)