from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String,unique = True)
    password = db.COlumn(db.String)
    name = db.COnlumn(db.String)
    email = db.COlumn(db.String, unique = True)

    def __init__(self,username,password,name,email): #valores obrigatorios
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):#Representar os registro quando pesquisado
        return "<User %r>" % self.username

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.Foreignkey('user.id'))

    user = db.teltionship('User',foreignkeys=user_id)

    def __init__(self,content,user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer,primary_key)
    user_id = db.Column(db.Integer,db.Foreignkey('users.id'))
    follower_id = db.Column(db.Integer,db.Foreignkey('users.id'))

    user = db.relationship('User',foreignkeys=user_id)
    follower = db.relationship('User',foreignkeys=follower_id)