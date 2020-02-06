from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)
n=''
def print(*args):
    global n

    for i in range(len(args)):
        if i>0:
            n+=','
        n+=str(args[i])
    n+='\n'



#@app.route('/success/<name>')
def success(name):
   global n
   n=''
   # x=exec('x=2\ny=3\nPrint(x+y)')
   # print(x)
   # print(5,Print(5+6))
   try:
       exec(name)
   except Exception as e:
       n = e

   return '>>> %s' %(n)


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
      user = request.form['nm']

      success(user)
      return render_template('login.html', run=n,user=user)

    else:
      user = request.args.get('nm')
      return render_template('login.html', run=n,user=user)

if __name__ == '__main__':
   app.run(debug = True)