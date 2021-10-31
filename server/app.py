


import json
import db
from flask import jsonify, request

app = db.connection.conn()

@app.route("/plans", methods=["GET"])
def handle_plans():
    if request.method == "GET":
        plans = db.connection.conn().cursor().fetchall()
        return jsonify([plans.serialize for plan in plans])
    else:
        return {"message": "failure"}


@app.route("/plans/<plan_name>", methods=["GET"])
def handle_plan(plan_name):
    if request.method == "GET":
        try:
            plan =db.connection.conn().cursor().fetchone().filter_by(name=plan_name).first_or_404()
            return jsonify(plan.serialize)
        except:
            return jsonify({"error": f"plan {plan_name} not found"})
    else:
        return {"message": "Request method not implemented"}


@app.route("/plans/add", methods=["POST"])
def add_plan():
    if request.method == "POST":
        plan =db.connectionpsy.conn().cursor().execute("INSERT INTO plans (plan_name,plan_time)\
          VALUES ('hiking','tomorrow morning')" );
        return jsonify(plan.serialize)
    else:
        return {"message": "Request method not implemented"}


if __name__ == "__main__":
    app.run(debug=True)