import os
import pandas as pd
from celery import Celery
from dotenv import load_dotenv


# Celery configuration
load_dotenv('.env')
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


# Celery periodic tasks
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs) -> None:
    # Example of periodic task (will be executed every 10 seconds)
    sender.add_periodic_task(10, periodic_task.s(), name='Periodic task example')


@celery.task(name="Periodic Task (every 10 seconds)")
def periodic_task() -> None:
    print("Example of periodic task executed!")


@celery.task(name="File Processing Task")
def file_handler_task(file: str):
    df = pd.read_excel(file)
    print(f"{df.head()}")
    print(f"file processed {file}")
    os.remove(file)
