import os
from dotenv import load_dotenv
import boto3
import json

# Load environment variables from the .env file
load_dotenv()

# Configure the Bedrock client with loaded credentials
bedrock = boto3.client(
    'bedrock-runtime',
    'us-east-1',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

# Function to summarize a document
def summarize_document(document_path):
    # Read document content in binary mode
    with open(document_path, 'rb') as file:
        document_content = file.read()

    # prompt for summarizing the document
    prompt = """
    Human: Summarize the legal document.

    Instructions:
    - Provide a summary of the document.
    - Identify key points, arguments, and conclusions.

    Document Content:
    {}

    Assistant:
    """.format(document_content)

    # Call Bedrock API to summarize document
    return process_prompt(prompt)

# Function to process the prompt and obtain response
def process_prompt(prompt):
    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 1000,
        "temperature": 1,
        "top_k": 1,
        "top_p": 0.001,
        "stop_sequences": ["\n\nHuman:", "\n\nAssistant:"],
    })

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = response.get('body').read().decode('utf-8').strip()

    if response_body:
        completion = json.loads(response_body).get('completion')
        return completion
    else:
        return None

# Main function to summarize documents in each folder
def main():
    documents_dir = 'documents'
    for folder_name in os.listdir(documents_dir):
        folder_path = os.path.join(documents_dir, folder_name)
        if os.path.isdir(folder_path):
            print(f"Summarizing documents in {folder_name} folder:")
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    print(f"Summarizing document: {file_name}")
                    document_summary = summarize_document(file_path)
                    print("Summary:", document_summary)
                    print("------------------------------------------")

# Entry point of the script
if __name__ == "__main__":
    main()
