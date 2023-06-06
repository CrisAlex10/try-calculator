from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        

        return render_template('index.html', result=result)
    except Exception:
        return render_template("index,.html", "error")

if __name__ == '__main__':
    app.run(debug=True)