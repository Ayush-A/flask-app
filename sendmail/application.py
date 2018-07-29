from flask import Flask, render_template, request
import smtplib

app = Flask("__name__")

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        email_from = request.form.get("emailfrom")
        email_to = request.form.get("emailto")
        password = request.form.get("password")
        subject = request.form.get("subject")
        body = request.form.get("bodymail")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_from, password)
        server.sendmail(email_from, email_to, body)
        return render_template("success.html")