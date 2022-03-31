from flask import Flask, render_template, request,redirect
import random


app = Flask(__name__)

data = {}


@app.route('/', methods=['GET''POST'])
def home_post():
    if request.method == 'POST':
        a={}
        original_url = request.form.get('in_1')
        short_url = random.randint(1, 100)
        a[short_url] = original_url
        data[short_url] = original_url
        return render_template('home.html', a = a)
    return render_template('home.html')

@app.route('/history')
def history_get():
    return render_template('history.html', data=data)

@app.route('/sh/<short>')
def fun(short):
    if int(short) in data:
        return "Redirect to {}".format(data[int(short)])
    return "incorrect URL"




if __name__ == "__main__":
    app.run(debug=True)