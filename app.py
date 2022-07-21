from flask import Flask, request
from tax_calculator import calculate_tax

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello</h1>"


@app.route("/jacob")
def jacob():
    return "<h1>Jacob was here!</h1>"


@app.route("/cats")
def cats():
    all_cats = get_cats()
    return {"cats": all_cats}


def get_cats():
    return ["Tabby", "Tuxedo", "Norwegian Forest"]


@app.route("/tax-calculator")
def get_taxes():
    if (
        request.args.get("income") is None
        or request.args.get("filingStatus") is None
        or request.args.get("year") is None
    ):
        print("Invalid Input: Missing Parameter", request.args.get("income"))
        missing_parameters = list()

        for x in ['income', 'filingStatus', 'year']:
            if request.args.get(x) is None:
                missing_parameters.append(x)

        return (
            f"Bad Request: Missing Parameter(s) {missing_parameters}",
            400,
        )

    try:
        int(request.args.get("income"))
    except ValueError:
        return "Bad Request: Invalid Parameter Type " \
             + "(Income should be an Integer)", 400

    try:
        int(request.args.get("year"))
    except ValueError:
        return "Bad Request: Invalid Parameter Type " \
             + "(Year should be an Integer)", 400

    if request.args.get("filingStatus") not in ["single", "joint"]:
        return "Bad Request: Invalid Parameter " \
               "(Filing Status should be one of [single, joint].", 400

    return {
        "taxes": calculate_tax(
            int(request.args.get("income")),
            request.args.get("filingStatus"),
            request.args.get("year"),
        )
    }
