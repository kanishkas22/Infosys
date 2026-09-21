# ============================
# MODIFICATION 1
# Import everything together
# ============================

from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["POST"])
def register():

    # Get values from registration form
    fullname = request.form["full_name"]
    email = request.form["email"]
    password = request.form["password"]

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    INSERT INTO candidates(full_name,email,password)
    VALUES(%s,%s,%s)
    """

    values = (fullname, email, password)

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.close()

    # ==========================================
    # MODIFICATION 2
    # Instead of showing plain text,
    # redirect user to login page
    # ==========================================

    return redirect(url_for("home"))


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["POST"])
def login():

    candidate = request.form["candidate_id"]
    password = request.form["password"]

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    sql = """
    SELECT *
    FROM candidates
    WHERE email=%s
    AND password=%s
    """

    cursor.execute(sql, (candidate, password))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:

        # ==========================================
        # MODIFICATION 3
        # Redirect using FUNCTION NAME
        # NOT HTML FILE NAME
        # ==========================================

        return redirect(url_for("camera"))

    else:

        return "Invalid Credentials"


# ==========================================
# CAMERA CHECK
# ==========================================

@app.route("/camera-check")
def camera():

    return render_template("camera_check.html")


# ==========================================
# MICROPHONE CHECK
# ==========================================

@app.route("/mic-check")
def mic():

    return render_template("mic_check.html")


# ==========================================
# SELFIE CHECK
# ==========================================

@app.route("/selfie-check")
def selfie():

    return render_template("selfie_check.html")


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)