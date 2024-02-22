from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    #app.run()
    user = User()
    db_sess = db_session.create_session()

    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Cowboy"
    user.name = "Stoyat"
    user.age = 8
    user.position = "Cowbay"
    user.speciality = "Poprigun"
    user.address = "Dikii_1Mars"
    user.email = "Cowboy_Stonat@mars.org"
    user.hashed_password = "cow"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Zxc"
    user.name = "Mid"
    user.age = 993
    user.position = "ghoul"
    user.speciality = "engineer"
    user.address = "module_Tokyo"
    user.email = "1000-7zxc@mars.org"
    user.hashed_password = "zxc"
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()