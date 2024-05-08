import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    user = session.get("user_id")

    # Try storing all stocks the user owns into a list of dictionaries, grouping the same stocks together in the list (GROUP BY symbol)
    try:
        stocks = db.execute("SELECT symbol, name, price, SUM(shares) AS shares FROM portfolio WHERE user_id = ? GROUP BY symbol", user)
    except:
        return apology("you have no stocks")
    if not stocks:
        return render_template("buy.html")
        #return apology("you have no stocks")
    # Set variable for total $ user has in stocks
    stocks_total = 0

    # Iterate through stocks, calculating the total $ and adding it to a stocks total
    for stock in stocks:
        # Use lookup function to get current price of stock
        current = lookup(stock["symbol"])
        price = float(current["price"])
        # Replace the value for "price" for each stock with the current price provided by lookup
        stock["price"] = price
        shares = int(stock["shares"])
        # Calculate the total $ invested in each stock
        total = price * shares
        # Calculate the total $ invested
        stocks_total += total

    # Find the amount of cash the user has left
    cash1 = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]["cash"]
    cash = usd(cash1)

    # Add the cash + $ in stocks.
    grandtotal = stocks_total + cash1
    grandtotal = usd(grandtotal)

    # Render index.html, passing in all variables.
    return render_template("index.html", stocks=stocks, total=total, cash=cash, grandtotal=grandtotal)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST
    if request.method == "POST":

        # Store information in variables
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Ensure symbol was entered:
        if not symbol:
            return apology("please enter stock symbol")

        # Check if shares is an integer
        try:
            shares = int(shares)
        except:
            return apology("please enter an integer value for shares")

        # Check for valid number of shares
        if shares <= 0 or not shares:
            return apology("please enter a valid integer")

        # Look up stock quote
        stock = lookup(symbol)

        # Ensure stock exists
        if not stock:
            return apology("stock does not exist")

        # Save name and price from stock dictionary into distinct variables
        name = stock['name']
        price = stock['price']

        # Calculate cost of purchasing x shares of stock
        cost = price * shares

        # Get user id
        user = session["user_id"]

        # Check how much cash the user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]["cash"]

        # Check if user has enough money for stock
        if cash < cost:
            return apology("You do not have enough cash for this transaction")

        # Purchase stock and update database
        # Update transactions table
        db.execute("INSERT INTO transactions(user_id, transaction_type, name, symbol, shares, price, time) VALUES(?, ?, ?, ?, ?, ?, ?)", user, "buy", name, symbol, shares, price, datetime.datetime.now())

        # Update portfolio table
        exist = db.execute("SELECT symbol FROM portfolio WHERE user_id = ? AND symbol = ?", user, symbol)
        try:
            current_shares = int(db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", user, symbol)[0]["shares"])
        except:
            current_shares = 0
        new_shares = current_shares + shares

        if not exist:
            db.execute("INSERT INTO portfolio(user_id, name, symbol, shares, price) VALUES(?, ?, ?, ?, ?)", user, name, symbol, shares, price)
        else:
            db.execute("UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?", new_shares, user, symbol)

        # Update users table
        db.execute("UPDATE users SET cash = ? WHERE ID = ?", cash-cost, user)

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user = session.get("user_id")
    stocks = db.execute("SELECT symbol, transaction_type, SUM(shares) AS shares, price, time FROM transactions WHERE user_id = ? GROUP BY time", user)
    if not stocks:
        return apology("you have no stocks")

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # If the form was reached via GET
    if request.method == "POST":

        # Look up stock quote
        stock = lookup(request.form.get("symbol").upper())

        # Ensure stock exists
        if not stock:
            return apology("stock does not exist")

        # Save values from dictionary into distinct variables
        name = stock['name']
        price = usd(stock['price'])
        symbol = stock['symbol']

        # Pass values into html template
        return render_template("quoted.html", name=name, symbol=symbol, price=price)

    # If the page was reached via GET, display form to request a quote.
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Store user input in variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure no fields are left blank
        if not username:
            return apology("must enter username")
        elif not password:
            return apology("must enter password")
        elif not confirmation:
            return apology("must confirm password")

        # Check if user confirmed password
        if password != confirmation:
            return apology("password does not match, please try again.")

        # Hash password
        hashed = generate_password_hash(password)

        # Check if username already in database
        exist = db.execute("SELECT username FROM users WHERE username = ?", username)
        # Return error message if username taken
        if len(exist) >= 1:
            return apology("username is already taken")
        else:
            # Insert user into database
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed)

        # Find the user we just added in the database
        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Log user in
        session["user_id"] = user[0]["id"]

        #Redirect to home page
        return render_template("index.html")
        #return redirect("/")

    # If the form was reached via GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        user = session.get("user_id")

        # Create list of symbols
        symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ? AND shares > 0 GROUP BY symbol", user)
        if not symbols:
            return apology("you have no stocks")

        # Store information in variables
        users_symbol = request.form.get("symbol").upper()
        users_shares = request.form.get("shares")

        # Ensure symbol was entered:
        if not users_symbol:
            return apology("please enter stock symbol")

        # Ensure stock exists
        item = lookup(users_symbol)
        if not item:
            return apology("invalid symbol")

        # Ensure symbol is in transactions database
        #if users_symbol not in symbols:
            #return apology("you do not own any shares of this stock")

        # Check if shares is an integer
        try:
            users_shares = int(users_shares)
        except:
            return apology("please enter an integer value for shares")

        # Check for valid number of shares
        if users_shares <= 0 or not users_shares:
            return apology("please enter a valid integer")

        # Create dict for this stock
        this_stock = db.execute("SELECT symbol, price, SUM(shares) AS shares FROM portfolio WHERE user_id = ? AND symbol = ? GROUP BY symbol", user, users_symbol)[0]

        if not this_stock:
            return apology("You do not hav any shares of this stock")

        # Ensure user has enough shares of the stock to sell
        current_shares = this_stock["shares"]
        if users_shares > current_shares:
            return apology("you do not have enough shares of this stock")

        # Get current price for stocks to sell
        price = float(item["price"])
        name = item["name"]
        symbol = item["symbol"]
        shares = users_shares
        selling = price * users_shares
        new_shares = current_shares - shares

        # Check how much cash the user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user)[0]["cash"]
        new_cash = cash + selling

        # Sell stock and update database
        # Update transactions table
        db.execute("INSERT INTO transactions(user_id, transaction_type, name, symbol, shares, price, time) VALUES(?, ?, ?, ?, ?, ?, ?)", user, "sell", name, symbol, shares, price, datetime.datetime.now())

        # Update portfolio table
        if new_shares == 0:
            db.execute("DELETE FROM portfolio WHERE symbol = ?", symbol)
        else:
            db.execute("UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?", new_shares, user, symbol)

        # Update users table
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user)

        return redirect("/")

    # User reached route via GET
    else:
        user = session.get("user_id")
        # Try storing all symbols for stocks the user owns into a list of dictionaries, grouping the same stocks together in the list (GROUP BY symbol)
        try:
            symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user)
        except:
            return apology("you have no stocks")

        return render_template("sell.html", symbols=symbols)
