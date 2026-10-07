import os
from decimal import Decimal

from flask import Flask, flash, redirect, render_template, request, session, url_for

from database.models.services.atm_service import (
    deposit_money,
    pin_verify,
    transfer_money,
    withdraw_amount,
)
from database.models.transaction import get_transactions_with_date
from database.models.user import get_user_by_card, locked_account, update_pin

app = Flask(__name__)
app.secret_key = os.getenv("ATM_SECRET_KEY", "atm_secret_key_change_me")


def current_user():
    card_number = session.get("card_number")
    if not card_number:
        return None
    return get_user_by_card(card_number)


def masked_number(value, visible=4):
    text = str(value)
    if len(text) <= visible:
        return text
    return "•" * (len(text) - visible) + text[-visible:]


def user_context(user):
    return {
        "user": user,
        "customer_name": user[1],
        "account_number": user[2],
        "masked_account": masked_number(user[2]),
        "card_number": user[3],
        "masked_card": masked_number(user[3]),
        "balance": user[4],
        "is_locked": bool(user[5]),
    }


@app.route("/", methods=["GET", "POST"])
def login():
    if "card_number" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        card_number = request.form.get("card_number", "").replace(" ", "").strip()
        pin = request.form.get("pin", "").strip()
        user = get_user_by_card(card_number)

        if user is None:
            flash("Card number not found.", "error")
            return render_template("login.html")

        if user[5]:
            flash("This account is locked. Please contact an administrator.", "error")
            return render_template("login.html")

        if pin_verify(card_number, pin):
            session.clear()
            session["card_number"] = card_number
            session["failed_attempts"] = 0
            flash("Login successful. Welcome back!", "success")
            return redirect(url_for("dashboard"))

        attempts = session.get("failed_attempts", 0) + 1
        session["failed_attempts"] = attempts
        attempts_left = 3 - attempts

        if attempts >= 3:
            locked_account(user[0])
            session.clear()
            flash("Account locked after 3 incorrect PIN attempts.", "error")
        else:
            flash(f"Invalid PIN. {attempts_left} attempt(s) remaining.", "error")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    transactions = get_transactions_with_date(user[0])
    recent_transactions = transactions[:5]

    total_deposits = sum((Decimal(str(t[1])) for t in transactions if t[0] in ("Deposit", "Transfer In")), Decimal("0"))
    total_withdrawals = sum((Decimal(str(t[1])) for t in transactions if t[0] == "Withdraw"), Decimal("0"))
    total_transfers = sum((Decimal(str(t[1])) for t in transactions if t[0] == "Transfer Out"), Decimal("0"))

    return render_template(
        "dashboard.html",
        **user_context(user),
        recent_transactions=recent_transactions,
        total_deposits=total_deposits,
        total_withdrawals=total_withdrawals,
        total_transfers=total_transfers,
    )


@app.route("/balance")
def balance():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    recent_transactions = get_transactions_with_date(user[0], limit=3)
    return render_template(
        "balance.html",
        **user_context(user),
        recent_transactions=recent_transactions,
    )


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = request.form.get("deposit", "").strip()
        success, message = deposit_money(user[3], amount)
        flash(message, "success" if success else "error")
        return redirect(url_for("deposit"))

    user = current_user()
    recent_transactions = [
        t for t in get_transactions_with_date(user[0]) if t[0] == "Deposit"
    ][:3]
    return render_template(
        "deposit.html",
        **user_context(user),
        recent_transactions=recent_transactions,
    )


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = request.form.get("amount", "").strip()
        success, message = withdraw_amount(user[3], amount)
        flash(message, "success" if success else "error")
        return redirect(url_for("withdraw"))

    user = current_user()
    recent_transactions = [
        t for t in get_transactions_with_date(user[0]) if t[0] == "Withdraw"
    ][:3]
    return render_template(
        "withdraw.html",
        **user_context(user),
        recent_transactions=recent_transactions,
    )


@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        receiver_account = request.form.get("receiver_account", "").strip()
        amount = request.form.get("amount", "").strip()
        success, message = transfer_money(user[3], receiver_account, amount)
        flash(message, "success" if success else "error")
        return redirect(url_for("transfer"))

    user = current_user()
    recent_transfers = [
        t for t in get_transactions_with_date(user[0]) if t[0] in ("Transfer Out", "Transfer In")
    ][:4]
    return render_template(
        "transfer.html",
        **user_context(user),
        recent_transactions=recent_transfers,
    )


@app.route("/history")
def history():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    transactions = get_transactions_with_date(user[0])
    return render_template(
        "history.html",
        **user_context(user),
        transactions=transactions,
    )


@app.route("/change_pin", methods=["GET", "POST"])
def change_pin():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        old_pin = request.form.get("current_pin", "").strip()
        new_pin = request.form.get("new_pin", "").strip()
        confirm_pin = request.form.get("confirm_pin", "").strip()

        if new_pin != confirm_pin:
            flash("New PIN and confirmation PIN do not match.", "error")
        else:
            success, message = update_pin(user[3], old_pin, new_pin)
            flash(message, "success" if success else "error")
            if success:
                return redirect(url_for("change_pin"))

    return render_template("change_pin.html", **user_context(user))


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out securely.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
