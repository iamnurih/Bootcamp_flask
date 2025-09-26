from flask import Flask, render_template, request, jsonify, Blueprint
from .models import SessionLocal, Todo

todo_bp = Blueprint("todos", __name__)


# 1. 전체 목록 조회: GET
@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task": t.task} for t in todos])

# 2. 특정 항목 조회: GET
@todo_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
    if not todo:
        return jsonify({"error": "할 일이 없습니다"}), 404

    return jsonify({"id": todo.id, "task": todo.task})


    # 400 -> bad request: 코딩 잘못
    # 401 -> unauthorized: 사이트에 로그인 안했는데 뭔가 하려고해서.. 로그인, 회원가입.
    # 403 -> forbidden: 사이트에 이미 로그인 한 상태에서 권한이 없는거
    # 404 -> not found: 못찾음
    # 409 -> conflict: 회원가입을 이미 했는데, 또 하는 경우
    # 200 -> ok
    # 201 -> created: 내가 뭘 만들었다. 없는데 만들었다.
    # 204 -> no content: 뭔가 성공을 하긴 했는데 딱히 응답할거 없을때


# 3. 항목 추가: POST
@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json() # body -> json
    db = SessionLocal()
    new_todo = Todo(task=data["task"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    return jsonify ({"id": new_todo.id, "task": new_todo.task}), 201

# 4. 항목 수정: PUT, PATCH
@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todos(todo_id):
   data = request.get_json()
   db = SessionLocal()

   todo = db.query(Todo).get(todo_id)
   if not todo:
        db.close()
        return jsonify({"error": "할 일이 없습니다"}), 404

   todo.task = data["task"]
   db.commit()

   updated = {"id": todo.id, "task": todo.task}
   db.close()
   return jsonify (updated)


# 5. 항목 삭제: DELETE
@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error": "할 일이 없습니다"}), 404

    db.delete(todo)

    db.commit()
    db.close()
    return jsonify ({"deleted": "삭제 완료"})
