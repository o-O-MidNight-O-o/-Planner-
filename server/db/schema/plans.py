





from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PlansModel(db.Model):
    """
    Defines the plans model
    """

    __tablename__ = "plans"

    plan_name = db.Column("plan_name", db.String, primary_key=True)
    plane_time = db.Column("plan_time", db.String)

    def __init__(self, plan_name, plan_time):
        self.plan_name = plan_name
        self.plan_time = plan_time

    def __repr__(self):
        return f"<Item {self.plan_name}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"plan_name": self.plan_name, "plan_time": self.plan_time}