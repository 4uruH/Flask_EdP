from flask import Blueprint, render_template

homepage = Blueprint("homepage", __name__)


@homepage.route("/", endpoint="index")
def articles_list():
    return render_template("index.html")
