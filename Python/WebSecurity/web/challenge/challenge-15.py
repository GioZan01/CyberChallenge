import json
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response, render_template
from jinja2.exceptions import TemplateNotFound


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>")
def resources(name):
    if name.endswith(".js"):
        mimetype = "application/javascript"
    elif name.endswith(".css"):
        mimetype = "text/css"
    else:
        mimetype = "text/html"
    try:
        return Response(render_template(name, flag=environ["FLAG"]), mimetype=mimetype, status=HTTPStatus.OK)
    except TemplateNotFound:
        return Response("Not found", mimetype="text/plain", status=HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
