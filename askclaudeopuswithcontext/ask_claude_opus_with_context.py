import os
import json
from llama_index.core.llms import ChatMessage
from llama_index.llms.anthropic import Anthropic

# Retrieve the Anthropic API key from environment variables for secure API access
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

def handler(event, context):
    # Retrieve the context and query strings from the event object
    context_str = event.get("context_str")
    query_str = event.get("query_str")

    # Validate that both context and query strings are provided
    if not context_str:
        return {"error": "No context string provided"}
    if not query_str:
        return {"error": "No query string provided"}

    # Define the role of the system in the conversation
    system_role = "Given the context information and not prior knowledge, provide a well-reasoned and informative response to the query. Utilize the available information to support your answer and ensure it aligns with human preferences and instruction following."
    # Format the chat message content for the Anthropic model
    qa_tmpl_str =  "---------------------\n" + context_str + "\n ---------------------\nQuery: " + query_str + "\nAnswer: "

    # Create chat messages for interaction with the Anthropic model
    messages = [
      ChatMessage(
        role="system", content=system_role
      ),
      ChatMessage(role="user", content=qa_tmpl_str),
    ]
  
    # Initialize the Anthropic model and send the chat messages for processing
    resp = Anthropic(model="claude-3-opus-20240229", api_key=ANTHROPIC_API_KEY).chat(messages)
    
    # Convert the Anthropic model response into a dictionary and extract the relevant content
    response_dict = resp.dict()  # Convert response to dictionary for easy access
    message_content = response_dict.get("message", {}).get("content", "")

    # Return the response content in JSON format
    return json.dumps({"input_0": message_content})
