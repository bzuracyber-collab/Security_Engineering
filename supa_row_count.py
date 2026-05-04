import os
from supabase import create_client

# Set up credentials
url = "URL"
key = "service-role-key"

# Init the client
supabase = create_client(url, key)

# Query
response = supabase.table('profiles').select("*", count='exact').execute()

# Handling Data
row_count = response.count

print(f"Connection Successful!")
print(f"Total entries found in table: {row_count}")
