import json
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.post("/login")
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if username == "admin" and password == "admin":
        return Response(json.dumps({"token": environ["FLAG"]}, indent=2), mimetype="application/json", status=HTTPStatus.OK)
    else:
        return Response(json.dumps({"error": "Unauthorized"}, indent=2), mimetype="application/json", status=HTTPStatus.UNAUTHORIZED)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
