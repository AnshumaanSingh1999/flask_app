from unittest import result
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
    #return 'Hello, World!'
   
@app.route('/report',methods=['POST','GET'])
def ew():
    if request.method =="POST":
        t=int(request.form['t'])
        h=int(request.form['h'])
        w=int(request.form['w'])
        r=int(request.form['r'])
        s=t+h+w+r     
        return render_template('report.html', result=s)
        #return redirect(url_for("t",t),))
    else:
        return render_template('index.html')
    #return 'Hello, World!'




if __name__ =="__main__":
    app.debug=True
    app.run()

