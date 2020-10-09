import json

from flask import Flask, make_response, current_app


class Router:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/hello_world", "helloWorld", self.helloWorld)

    def index(self):
        return make_response("Welcome to your Web Application", 200)

    def helloWorld(self):
        response = json.dumps({"payload": "hello world!!! This is a test. Hello Chadi."})

        return current_app.response_class(response, mimetype="application/json")
