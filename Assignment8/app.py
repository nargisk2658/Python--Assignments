from flask import Flask, render_template, redirect, url_for
from config import Config
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("success", username=user.name))

        except Exception as e:
            db.session.rollback()
            return f"Error occurred: {str(e)}"

    return render_template("register.html", form=form)


@app.route("/success/<username>")
def success(username):
    return render_template("success.html", name=username)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
