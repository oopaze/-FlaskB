from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String,unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    followers = db.relationship('User', secondary='followers',
                              backref=db.backref('users', lazy='dynamic'))


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User')

    def __init__(self,content,user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id

Follow = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)


