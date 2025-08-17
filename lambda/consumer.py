import json, os, time, boto3
DDB_TABLE = os.environ["DDB_TABLE"]
table = boto3.resource("dynamodb").Table(DDB_TABLE)

def handler(event, context):
    failures = []
    for rec in event.get("Records", []):
        try:
            body = json.loads(rec["body"])
            order_id = body["id"]; ts = int(body.get("ts", time.time()))
            table.put_item(Item={"id": order_id, "created_at": ts})
        except Exception:
            failures.append({"itemIdentifier": rec["messageId"]})
    return {"batchItemFailures": failures}
