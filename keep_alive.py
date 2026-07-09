"""
keep_alive.py — Flask ping server for 24/7 uptime
Runs in a background thread so the bot stays alive on hosting platforms.
"""

from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return (
        "<h2>🚀 Shadow's Box Bot</h2>"
        "<p>Status: <strong style='color:green'>Online ✅</strong></p>"
    )

def _run():
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)

def keep_alive():
    t = Thread(target=_run, daemon=True)
    t.start()
