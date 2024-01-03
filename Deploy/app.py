from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/gallery')
def galary():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

app.run(debug=True)