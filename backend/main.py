from flask import Flask, request, jsonify
import base64
import os
import boto3
import json
from dotenv import load_dotenv

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

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_document():
    document_file = request.files['document']
    document_content = document_file.read()
    document_content_base64 = base64.b64encode(document_content).decode('utf-8')

    prompt = f"""
    Human: Summarize the legal document.

    Instructions:
    - Provide a summary of the document.
    - Identify key points, arguments, and conclusions.

    Document Content (Base64 Encoded):
    {document_content_base64}

    Assistant:
    """

    response = process_prompt(prompt)
    return jsonify({'summary': response})

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

if __name__ == "__main__":
    app.run(debug=True)
