import chromadb
import uuid
from chromadb.config import Settings


#client = chromadb.HttpClient(host="localhost", port=8000)

client = chromadb.Client(Settings())


col = client.get_or_create_collection("chapters")

def save_version(chapter_id: str, text: str, metadata: dict):
    vid = str(uuid.uuid4())
    col.add(documents=[text], ids=[vid], metadatas=[{"chapter_id": chapter_id, **metadata}])
    return vid

def list_versions(chapter_id):
    return col.get(where={"chapter_id": chapter_id})

