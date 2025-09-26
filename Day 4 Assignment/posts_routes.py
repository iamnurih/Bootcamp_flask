from flask import request, jsonify
from flask_smorest import Blueprint, abort
from models import Post

def create_post_blueprint(db):
    posts_blp = Blueprint("post", __name__, description = "posts api", url_prefix = "/posts")

    @posts_blp.route("/", methods = ["GET"])
    def get_posts():
        posts = Post.query.all()  # blog_db에서 posts로 변경
        post_list = []
        for post in posts:
            post_list.append({"id": post.id,
                              "title": post.title,
                              "content": post.content
                              }
                             )
        return jsonify({"posts": post_list})

    @posts_blp.route("/", methods = ["POST"])
    def post():
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            abort(400, message = "title and content are required")

        new_post = Post(title = title, content = content)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({
            "msg": "Post Created"
        }), 201

    @posts_blp.route("/<int:post_id>", methods = ["PUT"])
    def put(post_id):
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            abort(400, message = "title and content are required")

        modified_post = Post.query.filter_by(id=post_id).first()

        if not modified_post:
            abort(404, message = "post not found")

        modified_post.title = title
        modified_post.content = content
        db.session.commit()

        return jsonify({"msg": "Post Updated"}), 200

    @posts_blp.route("/<int:post_id>", methods = ["DELETE"])
    def delete_post(post_id):
        d_post = Post.query.filter_by(id=post_id).first()
        if not d_post:
            abort(404, message = "post not found")

        db.session.delete(d_post)
        db.session.commit()
        return jsonify({"msg": "Post Deleted"}), 200

    return posts_blp