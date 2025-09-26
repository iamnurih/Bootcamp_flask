from flask import Flask, request, jsonify

app = Flask(__name__)

todos = {
    1: "flask 공부하기",
    2: "파이썬 공부하기",
}

# 1. 전체 목록 조회: GET
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


# 2. 특정 항목 조회: GET
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:
        return jsonify({"error": "할 일이 없습니다"}), 404 # not found
    
    # 400 -> bad request: 코딩 잘못
    # 401 -> unauthorized: 사이트에 로그인 안했는데 뭔가 하려고해서.. 로그인, 회원가입. 
    # 403 -> forbidden: 사이트에 이미 로그인 한 상태에서 권한이 없는거
    # 404 -> not found: 못찾음
    # 409 -> conflict: 회원가입을 이미 했는데, 또 하는 경우

    return jsonify({todo_id: task})


# 3. 항목 추가: POST
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json() # body -> json

    # todos.keys() -> max([1, 2]) -> 2 + 1 -> 3
    new_id = max(todos.keys()) + 1 if todos else 1
    # if todos:
    #     new_id = max(todos.keys()) + 1 
    # else:
    #     new_id = 1
    todos[new_id] = data["task"]
    return jsonify({new_id: todos[new_id]}), 201

    # 200 -> ok
    # 201 -> created: 내가 뭘 만들었다. 없는데 만들었다.
    # 204 -> no content: 뭔가 성공을 하긴 했는데 딱히 응답할거 없을때

# 4. 항목 수정: PUT, PATCH
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todos(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "할 일이 없습니다"}), 404
    data = request.get_json()
    todos[todo_id] = data["task"]
    return jsonify({todo_id: todos[todo_id]})


# 5. 항목 삭제: DELETE
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "할 일을 찾을 수 없습니다"}), 404
    deleted = todos.pop(todo_id)
    return jsonify({"deleted": "삭제 완료!"})


if __name__ == '__main__':
    app.run(debug=True)