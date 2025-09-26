from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint('books', 'books', url_prefix = '/books', description = 'Opeartion on books')

books = []

@blp.route('/')
class BooksList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_book):
        new_book['id'] = len(books) + 1
        books.append(new_book)
        return new_book

@blp.route('/<int:book_id>')
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = 'Book not found')
        return book

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def put(self, new_book, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = 'Book not found')
        book.update(new_book)
        return book

    @blp.response(200)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id ), None)
        if book is None:
            abort(404, message = 'Book not found')
        books = [book for book in books if book['id'] != book_id]
        return ''



