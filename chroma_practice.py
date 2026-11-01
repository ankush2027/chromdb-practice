import chromadb
client=chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection(
    name="ai_learning"
)
collection.add(
    ids=["1", "2", "3", "4"],
    documents=[
        "Machine learning allows computers to learn patterns from data.",
        "Deep learning uses neural networks with multiple layers.",
        "Python is a popular programming language for AI development.",
        "Vector databases store embeddings and support similarity search."
    ]
)
print("Documents inserted successfully!")
print("Total documents:", collection.count())

data = collection.get(
    include=["documents", "embeddings"]
)

print("\nStored documents:")
print(data["documents"])

print("\nFirst document embedding:")
print(data["embeddings"][0])

print("\nEmbedding dimensions:")
print(len(data["embeddings"][0]))