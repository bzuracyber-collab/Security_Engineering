import boto3
import json
from datetime import datetime

# AWS Client Init
s3 = boto3.client('s3')
logs = boto3.client('logs')

def ship_security_logs(event_type, status, user_ip):
  # JSON  Payload
  payload = {
    "timestamp": datetime.now().isoformat(),
    "event": event_type,
    "status": status,
    "source_ip": user_ip
  }

  # Convert dictionary to JSON
  log_json = json.dumps(payload)

  # Ship to S3
  s3.put_object(
    Bucket='danielbzura_security_logs',
    Key=f"logs/{event_type}_{datetime.now().strftime('%H%M%S')}.json",
    Body=log_json
  )

  # Ship to CloudWatch
  logs.put_log_events(
    logGroupName='danielbzura_Security',
    logStreamName='AuthEvents',
    logEvents=[{'timestamp': int(datetime.now().timestamp() * 1000), 'message': log_json}]
  )
  print(f"Log shipped for {event_type}")

if __name__ = "__main__":
  ship_security_logs("login_attempt", "failed", "192.168.1.50")
