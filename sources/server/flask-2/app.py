from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    button_property = request.form['button_property']
    print(f"Button property: {button_property}")
    return ''

if __name__ == '__main__':
    app.run()