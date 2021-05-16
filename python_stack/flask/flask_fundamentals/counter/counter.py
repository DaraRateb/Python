from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'topsecert'

  
@app.route('/counter/')
def refresh():
    if 'refresh' in session:
        session['refresh'] = session['refresh'] + 1 
    else:
        session['refresh'] = 1
    return render_template ("index.html",x= session['refresh'])

@app.route('/destroy_session/')
def destroy():
    session.clear()
    session.pop('refresh', None)
    return render_template ("index.html")



if __name__=="__main__":
    app.run(debug=True)