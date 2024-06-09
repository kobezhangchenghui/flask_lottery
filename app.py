from flask import Flask, render_template
import random

app = Flask(__name__)

employees = ['赵一', '钱二', '孙三', '李四', '周五', '吴六', '郑七', '王八']


@app.route('/')
def hello_world():
    return render_template('index.html', employees=employees)


@app.route('/lottery')
def lottery():
    winners = random.sample(employees, 3)
    return render_template('index.html', employees=employees, winners=winners)


if __name__ == '__main__':
    app.run(debug=True)
