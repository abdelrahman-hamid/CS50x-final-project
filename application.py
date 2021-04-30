# Implements the web pages of a company website, including email confirmation

import os
import re

from flask import Flask, redirect, render_template, request
from flask_mail import Mail,  Message

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configurate flask mail (https://pythonhosted.org/Flask-Mail/)
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html", page="")


@app.route("/AboutUs")
def about():
    return render_template("about.html")


@app.route("/Services")
def services():
    return render_template("services.html")

# Confirms the contact form enquiry via email
@app.route("/ContactUs", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        # Get the submitted contact form values
        email = request.form.get("email")
        name = request.form.get("name")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Assign message subject, sender, and recipients
        msg = Message(
            "Your recent enquiry on fatoutaconsultancy.com",
            sender=("Faouta Consultancy", "abdelrahmanhamid98@gmail.com"),
            recipients=[email]
        )

        # Email message body in text format
        msg.body = ("Dear "+name+",\n\n"
                    "Thank you for contacting Fatouta Consultancy. We aim to"
                    "get back to you within 2 working days.\n\n"
                    "Here are details of your enquiry:\n"
                    "<Subject> "+subject+"\n"
                    "<Message> "+message+"\n\n"
                    "Best regards\n"
                    "Abdelrahman Hamid, General Manager")

        # Send the message
        mail.send(msg)

    # Display the contact.html page regardless of the request method
    return render_template("contact.html")