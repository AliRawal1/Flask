from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy student data
student_data = {
    "name": "John Ali",
    "marks": {
        "subject1": 90,
        "subject2": 85,
        "subject3": 75,
        "subject4": 60,
        "subject5": 70,
        "subject6": 80,
        "subject7": 95,
    },
}

@app.route('/')
def student_marks():
    return render_template('student_marks.html', student=student_data)

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        percentage = float(request.form['percentage'])
        if percentage >= 40:
            result = "Pass"
        else:
            result = "Fail"
        return render_template('result.html', result=result)
    return render_template('result.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
