from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "web"

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = TextAreaField(label='Message')  # Use TextAreaField for the message
    submit = SubmitField(label="Submit")

@app.route("/", methods=["GET", "POST"])
def home():
    cform = ContactForm()
    if cform.validate_on_submit():
        print(f"Name: {cform.name.data}, E-mail: {cform.email.data}, Message: {cform.message.data}")
        return redirect(url_for('home'))  # Redirect to avoid form resubmission
    return render_template("contact.html", form=cform)

if __name__ == '__main__':
    app.run(debug=True)
