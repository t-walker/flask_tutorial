from thermos import app, db
from thermos.models import User
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="twalker", email="twalkerweb@gmail.com"))
    db.session.add(User(username="jswanby", email="jswanbyweb@gmail.com"))
    db.session.commit()
    print "Initalized the database."

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all of your data?"):
        db.drop_all()
        print "Dropped the database."

if __name__ == '__main__':
    manager.run()
