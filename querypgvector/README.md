# Triform.ai Template: Semantic Text Retrieval

## Overview
This Python template integrates text retrieval based on semantic similarity, leveraging Cohere's multilingual embeddings and storing results in a PostgreSQL database.

In addition to an Anthropic account you need a remote Postgres PGVector database instance. You can [create a Postgres PGVector database instance to Supabase](https://supabase.com/docs/guides/database/extensions/pgvector). Setting it up is easy and it's free.  

## How it Works
The module initializes with environment variables to securely connect to Cohere and a PostgreSQL database. It configures an embedding model, processes input text, and retrieves semantically similar texts from the database.

## Use Cases
- Creating semantic search engines for diverse datasets.
- Developing recommendation systems based on text content.
- Enhancing customer support with relevant automated responses.

## Customization
You can customize this template by:
- Changing the Cohere model or parameters for different languages or domains.
- Modifying database parameters to connect to different setups or schemas.
- Adjusting retrieval logic for various similarity metrics or result limits.

## Environment Setup
Set the following environment variables:
- `COHERE_API_KEY`: Your Cohere API key for embedding.
- `DATABASE_HOST`, `DATABASE_USER`, and `DATABASE_PASSWORD`: Your database connection details.