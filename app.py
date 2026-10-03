from flask import(
Flask,
render_template,
request,
session,
redirect,
url_for)

from database.models.services.atm_service import pin_verify

app = Flask(__name__)
app.secret_key = "atm_secret_key"

@app.route("/",methods = ["GET","POST"])
def login():

    if request.method == "POST":

        card_number = request.form["card_number"] # take from login form
        pin = request.form["pin"]  # take from login form

        if pin_verify(card_number, pin):
            session["card-number"] = card_number  # card_no = 1414 --> system storage (1414)
            print(session)
            return redirect(
                url_for("dashboard") # if card no is correct then redirect to dashboard
            )

        return "Invalid Card Number or Pin" # if card_no or pin not correct

    return render_template("login.html") 

@app.route("/dashboard")
def dashboard():
    if "card_number" not in session:

        return redirect(
            url_for("login")
        )
    card_number = session["card_number"]
    return render_template(
        "dashboard.html",
        card_number = card_number
    )
@app.route("/logout")
def logout():
    session.clear()

    return redirect(
        url_for("login")
    )

if __name__ == "__main__":
    app.run(debug=True)