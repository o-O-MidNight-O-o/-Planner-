


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UsersModel(db.Model):
    """
    Defines the users model
    """

    __tablename__ = "users"

    username = db.Column("username", db.String, primary_key=True)
    password = db.Column("password", db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<Item {self.username}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"username": self.username, "password": self.password}