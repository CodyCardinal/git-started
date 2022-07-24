import flask
from flask import Flask
import random

app = Flask(__name__)


jokes = [
    "Q: Relationship status? A: I'll leave the relations to the database.",
    "Q: What do you call an idle server? A: A waiter.",
    "Q: How many Prolog programmers does it take to change a lightbulb? A: Yes.",
    "Q: Why was the developer unhappy at their job? A: They wanted arrays."

]
@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return flask.render_template('joke.html', joke_text=joke)

