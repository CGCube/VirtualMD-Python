from flask import Blueprint, render_template

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route("/")
def index():
    return render_template("index.html")

@routes_blueprint.route("/lead")
def lead():
    return render_template("lead.html")

@routes_blueprint.route("/drums")
def drums():
    return render_template("drums.html")

@routes_blueprint.route("/guitar")
def guitar():
    return render_template("guitar.html")

@routes_blueprint.route("/keys")
def keys():
    return render_template("keys.html")

@routes_blueprint.route("/cajon")
def cajon():
    return render_template("cajon.html")

@routes_blueprint.route("/blue_1")
def blue_1():
    return render_template("blue1.html")

@routes_blueprint.route("/blue_2")
def blue_2():
    return render_template("blue2.html")

@routes_blueprint.route("/blue_3")
def blue_3():
    return render_template("blue3.html")

@routes_blueprint.route("/blue_4")
def blue_4():
    return render_template("blue4.html")

@routes_blueprint.route("/gold_1")
def gold_1():
    return render_template("gold1.html")

@routes_blueprint.route("/gold_2")
def gold_2():
    return render_template("gold2.html")

@routes_blueprint.route("/gold_3")
def gold_3():
    return render_template("gold3.html")

@routes_blueprint.route("/gold_4")
def gold_4():
    return render_template("gold4.html")

@routes_blueprint.route("/mixer")
def mixer():
    return render_template("mixer.html")