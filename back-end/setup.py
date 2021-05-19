from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


def register_blueprints(blueprints, app:Flask):
    for bp in blueprints:
        app.register_blueprint(bp)

def run_scheduler(tasks):
    scheduler = BackgroundScheduler()
    for task in tasks:
        scheduler.add_job(func=task, trigger='interval', seconds=5)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
