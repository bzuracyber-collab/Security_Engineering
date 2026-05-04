import resend

resend_api_key = RESEND

def send_security_alert(threat_type, source_ip):
  html_content = f"""
  <strong> Security Alert: {threat_type}</strong>
  <p>A suspicious acitivity was detected from IP: {source_ip}</p>
  <p>Check the AWS CloudWatch dashboard for details.</p>
  """

  params = {
    "from": "security@danielbzura.com",
    "to": "[dannybzura@gmail.com]",
    "subject": f"Critical Alert: {threat_type}",
    "html": html_content
  }
  try:
    email = resend.Emails.send(params)
    print(f"Alert sent, ID: {email['id']}")
  except Exception as e:
    print(f"Failed to send alert: {e}")

if __name__ == "__main__":
  send_security_alert("Brute Force Attempt", "45.12.33.1")
