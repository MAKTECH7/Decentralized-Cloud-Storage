from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.services.account import Account
from config import APPWRITE_ENDPOINT, APPWRITE_PROJECT_ID, APPWRITE_API_KEY

# Initialize the Appwrite client
client = Client()
client.set_endpoint(APPWRITE_ENDPOINT)  # Your Appwrite server URL
client.set_project(APPWRITE_PROJECT_ID)  # Your project ID
client.set_key(APPWRITE_API_KEY)  # Your API key

# Initialize services
storage = Storage(client)
account = Account(client)

def signup(email, password):
    """Sign up a new user."""
    try:
        user = account.create(email=email, password=password, name=email.split('@')[0])
        return user
    except Exception as e:
        print(f"Signup failed: {e}")

def login(email, password):
    """Log in an existing user."""
    try:
        session = account.create_session(email=email, password=password)
        return session
    except Exception as e:
        print(f"Login failed: {e}")

def upload_chunk(chunk_path):
    """Upload a file chunk to Appwrite."""
    try:
        with open(chunk_path, 'rb') as file:
            result = storage.create_file(file=file, read=['*'], write=['*'])
            return result
    except Exception as e:
        print(f"Upload failed: {e}")

def download_chunk(file_id):
    """Download a file chunk from Appwrite using its ID."""
    try:
        result = storage.get_file(file_id)
        return result
    except Exception as e:
        print(f"Download failed: {e}")
