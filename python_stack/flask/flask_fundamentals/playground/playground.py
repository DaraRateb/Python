from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play/<int:num>/<newcolor>')                           
def blocks(num,newcolor):
    return render_template('index.html',num_times=num,color_pick=newcolor)  


    
if __name__=="__main__":
    app.run(debug=True)      