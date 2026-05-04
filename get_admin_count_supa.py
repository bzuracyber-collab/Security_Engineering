from supabase import create_client

#Creds
url = "url"
key = "service-role-key"

def run_security_audit():
  client = create_client(url, key)
  # Query Admin Users
  results = client.table('profiles').select("email, role, last_login").eq("role", "admin").execute()
  admins = results.data

  print("Admin Privilege Audit")

  if not admins:
    print("No admin users found.")
  else:
    for user in adminsL
      email = user.get('email')
      login = user.get('last_login')
      print(f"Admin Account: {email} Last Login: {login}")

if __name__ == "__main__":
  run_security_audit()
