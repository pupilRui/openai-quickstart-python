import os

import openai

from backend import cmd_based
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")


@app.route("/", methods=("GET", "POST"))
def index():
    question = ''
    if request.method == "POST":
        question = request.form["question"]
        return redirect(url_for("index", result=cmd_based.answer_question(question=question), question=question))

        # return redirect(url_for("index", result=cmd_based.answer_question(question=question)))

    result = request.args.get("result") or ""
    question = request.args.get("question") or "" 
    return render_template("customer.html", result=result, question=question)


def generate_prompt(question):
    return """Help answer this question:
question: {}""".format(
        question.capitalize()
    )
