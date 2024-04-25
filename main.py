from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', endpoint='get_started')
def get_started():
    return render_template('get_started.html')


@app.route('/about',endpoint='about')
def about():
    return render_template('about.html')

@app.route('/documentation', endpoint='documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/team', endpoint='team')
def team():
    return render_template('team.html')

@app.route('/contact', endpoint='contact')
def team():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True) 