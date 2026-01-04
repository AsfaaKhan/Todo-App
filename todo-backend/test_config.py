import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Check if .env file exists
env_file_path = os.path.join(os.getcwd(), '.env')
print(f".env file exists: {os.path.exists(env_file_path)}")

if os.path.exists(env_file_path):
    print("Contents of .env file:")
    with open(env_file_path, 'r') as f:
        print(f.read())

print("\nTesting configuration...")
from app.config import get_database_url, settings

print(f"DATABASE_URL from get_database_url(): {get_database_url()}")
print(f"DATABASE_URL from settings: {settings.database_url}")
print(f"Environment DATABASE_URL: {os.getenv('DATABASE_URL', 'Not set')}")

# Test creating the engine
from app.database import create_engine
try:
    engine = create_engine()
    print(f"Engine created with URL: {engine.url}")
    print("Engine creation successful!")
except Exception as e:
    print(f"Error creating engine: {e}")