import os
import sys
import random

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

employees = ['赵一', '钱二', '孙三', '李四', '周五', '吴六', '郑七', '王八']


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    employee_no = db.Column(db.String(20), unique=True)
    isWin = db.Column(db.Boolean(), default=False)


@app.route('/')
def hello_world():
    return render_template('index.html', employees=employees)


@app.route('/lottery')
def lottery():
    winners = random.sample(employees, 3)
    return render_template('index.html', employees=employees, winners=winners)


@app.route('/create', methods=['POST'])
def create_employee():
    employee = Employee(name='example', employee_no='12345', isWin=False)
    db.session.add(employee)
    db.session.commit()
    return 'employee created'


@app.route('/read')
def read_employee():
    employees = Employee.query.all()
    return ', '.join(str(employee) for employee in employees)


@app.route('/update/<int:id>', methods=['POST'])
def update_employee(id):
    employee = Employee.query.get(id)
    if employee:
        employee.name = 'new_employeename'
        db.session.commit()
        return 'User updated'
    else:
        return 'User not found', 404


@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return 'User deleted'
    else:
        return 'User not found', 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
