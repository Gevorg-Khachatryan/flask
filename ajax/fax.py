
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def proc():
    name=request.form['name']
    email=request.form['email']
    print(name,email)
    if name and email:
        return jsonify({'name':name})
    return jsonify({'error':"Missing data"})



if __name__ == '__main__':
    app.run(debug=True)