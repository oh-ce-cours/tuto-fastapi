from fastapi import FastAPI  # on importe fastapi
import datetime

ma_super_application = FastAPI()  # on créé une application


@ma_super_application.get("/date")
def compute_date():
    return {"date": datetime.date.today()}


@ma_super_application.get("/time")
def compute_time():
    return {"date": datetime.datetime.now()}


@ma_super_application.get("/datetime")
def compute_datetime():
    return {"date": datetime.datetime.now()}
