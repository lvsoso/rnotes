from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)

# 配置SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ne1zoP1GJ8T9XXF5@localhost:33099/demo'  # 使用SQLite数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 定义一个用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    __table_args__ = (UniqueConstraint('username', 'email', name='uix_username_email'),)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# 创建数据库和表
@app.before_first_request
def create_tables():
    db.create_all()

# 添加新用户
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print('User already exists')
        return 'User already exists', 409



# 获取所有用户
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])


# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)
