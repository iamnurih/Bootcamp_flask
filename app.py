from flask import Flask, render_template, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

item = []