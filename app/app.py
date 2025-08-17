import os
import psycopg2
import json
import boto3
from fastapi import FastAPI

app = FastAPI(title="aws-ha-app")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "password")
QUEUE_URL = os.getenv("QUEUE_URL")
AWS_REGION = os.getenv("AWS_REGION", "eu-central-1")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"service": "aws-ha-app", "message": "Hello from ALB → ASG (EC2)!"}

@app.get("/dbping")
def dbping():
    try:
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, connect_timeout=3)
        cur = conn.cursor(); cur.execute("SELECT 1;"); cur.fetchone()
        cur.close(); conn.close()
        return {"db": "reachable"}
    except Exception as e:
        return {"db": f"error: {type(e).__name__}"}

@app.post("/order")
def create_order():
    order = {"id": "ord_"+os.urandom(3).hex(), "ts": __import__("time").time()}
    if not QUEUE_URL:
        return {"status": "queued:NO_QUEUE_URL", "order": order}
    sqs = boto3.client("sqs", region_name=AWS_REGION)
    sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(order))
    return {"status": "queued", "order": order}
