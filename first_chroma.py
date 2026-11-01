import chromadb
client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(
    name="ai_notes"
)

print("ChromaDB connected successfully!")
print("Collection:", collection.name)