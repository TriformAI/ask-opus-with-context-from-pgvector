import os
import json
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.core import Settings

# Fetch Cohere API key from environment variables for secure API access
COHERE_API_KEY = os.environ['COHERE_API_KEY']
# Fetch Supabase database user and password from environment variables for secure database access
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

# Configure the embedding model used by the application
Settings.embed_model = CohereEmbedding(
    cohere_api_key=COHERE_API_KEY,
    model_name='embed-multilingual-v3.0',  # Specifies the Cohere model to be used for embeddings
    input_type='search_query'  # Indicates the type of input expected by the model
)

# Initialize the PGVectorStore to connect to a PostgreSQL database with specific parameters
vector_store = PGVectorStore.from_params(
    database='postgres',
    host=DATABASE_HOST,
    password=DATABASE_PASSWORD,
    port=5432,
    user=DATABASE_USER,
    table_name='text_storage_table',
    embed_dim=1024  # Set the embedding dimension to 1024 for Cohere models
)

def handler(event, context):
    # Retrieve text input from the event object, defaulting to None if not provided
    input = event.get('input_0')

    if not input:
        return {'error': "No query text provided"}  # Return an error if no input text is provided

    # Initialize a VectorStoreIndex using the configured PGVectorStore
    index = VectorStoreIndex.from_vector_store(vector_store)

    # Create a retriever from the index to find top 5 similar entries
    retriever = index.as_retriever(similarity_top_k=5)
    response = retriever.retrieve(input)  # Retrieve similar text based on the input

    context_str = ""
    # Concatenate the text of each retrieved entry, separated by double newlines
    for t in response:
      context_str += t.text + "\n\n"

    # Return the original query and the retrieved context as a JSON string
    return json.dumps({'context_str': context_str, 'query_str': input})
