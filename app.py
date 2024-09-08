from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the book recommendation page
@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
