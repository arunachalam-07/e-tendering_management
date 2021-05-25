from flask import Flask,render_template,request
from flask.wrappers import Request
from forms import contactForm,PlaceBid
from flask_bootstrap import Bootstrap
from tender import gettender,placeBid,Winner,show_winner
from eth_account.messages import encode_defunct


import datetime
import requests
app=Flask(__name__)
Bootstrap(app)
app.secret_key='0220'
@app.route('/contact',methods=['GET','POST'])
def contact():
    form =contactForm()
    return render_template('contact.html',form=form)

@app.route('/')
def viewtender():
    li=gettender()
    bo=datetime.datetime.fromtimestamp((li[2]))
    bc=datetime.datetime.fromtimestamp((li[4]))
    return render_template('showing_tenders.html',arr=li,bo=bo,bc=bc)
@app.route('/placebid')
def placebid():
    return render_template('placebid.html',)
@app.route('/submitbid',methods=['POST','GET'])
def submitbid():
    fun=""
    if request.method=='POST':
     fun=placeBid(request.form['address'],int(request.form['bid']) ,request.form['test']) 
    return render_template('submit_bid.html',x=(fun))

@app.route('/declarewinner')
def winner():
    return render_template('winner.html')

@app.route('/declare_winner',methods=['POST','GET'])
def declare_winner():
    win=""
    if request.method=='POST':
        win=Winner(request.form['address'])
    return render_template('showing_winner.html',win=win)

@app.route('/winner')
def viewwinner():
    val=show_winner()
    x=''
    if(val=='0x0000000000000000000000000000000000000000'):
        x='Winner will be declared after tender bidding ends'
    else:
        txt='The Winner is '
        x=txt.append(str(val))
    return render_template('view_winner.html',x=x)


if __name__=='__main__':
    app.run(debug=True)

