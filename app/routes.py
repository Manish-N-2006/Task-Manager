from flask import request, jsonify
from app.models import tasks
from app import db

def register_routes(app):

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")

        if not title:
            return jsonify({
                "error" : "Title is required"
            }), 400

        new_task = tasks(
            title=title, description=description
        )

        db.session.add(new_task)
        db.session.commit()

        return jsonify({
            "message" : "Task created Successfully",
            "task" : new_task.to_dict()
        }),201