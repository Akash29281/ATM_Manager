from flask import(
Flask,
render_template,
request,
session,
redirect,
url_for)

from database.models.services.atm_service import pin_verify,deposit_money,withdraw_amount,show_transaction_history,get_transactions

from database.models.user import get_user_by_card

app = Flask(__name__)
app.secret_key = "atm_secret_key"

@app.route("/",methods = ["GET","POST"])
def login():

    if request.method == "POST":

        card_number = request.form["card_number"] # take from login form
        pin = request.form["pin"]  # take from login form

        if pin_verify(card_number, pin):
            session["card_number"] = card_number  # card_no = 1414 --> system storage (1414)
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
    return redirect (
        url_for("login")
    )


@app.route("/balance")
def balance():
    if "card_number" not in session:
        return redirect(url_for("login"))
    card_number = session["card_number"]

    user = get_user_by_card(card_number)

    return render_template(
        "balance.html",
        balance = user[4]
    )

@app.route("/deposit",methods = ["GET","POST"])
def deposit():

    if "card_number" not in session:
        return "card number is not stored in session"
    card_number = session["card_number"]

    if request.method == "POST":
        amount = float(request.form["deposit"])

        deposit_money(card_number,amount)
    user = get_user_by_card(card_number)
        
    return render_template(
        "deposit.html",
        amount = user[4]
    )

@app.route("/withdraw",methods = ["GET","POST"])
def withdraw():
    if "card_number" not in session:
        return redirect(url_for("login"))
    card_number = session["card_number"]

    if request.method == "POST":
        amount = int(request.form["amount"])
        withdraw_amount(card_number , amount)

    user = get_user_by_card(card_number)
    return render_template(
        "withdraw.html",
        amount = user[4]
    )
        
@app.route("/history")
def history():

    if "card_number" not in session:
        return redirect(url_for("login"))

    card_number = session["card_number"]

    transactions = show_transaction_history(card_number)
    print("transactions: ",transactions)

    return render_template(
        "history.html",
        transactions=transactions
        
    )




if __name__ == "__main__":
    app.run(debug=True)