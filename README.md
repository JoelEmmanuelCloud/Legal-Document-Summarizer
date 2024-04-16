# Legal Document Summarizer

This project aims to summarize legal documents using AWS Bedrock and provide a simple frontend for displaying the document summaries.

## Project Structure

The project is structured as follows:

- **backend/**: Contains the backend Python code responsible for summarizing legal documents and serving the summaries to the frontend.

- **frontend/**: Contains the frontend files including HTML, CSS, and JavaScript for displaying the document summaries.

- **video/**: Directory for storing the demonstration video of the project.

- **.env**: Environment variables file containing sensitive information such as AWS credentials. Ensure to create this file and populate it with the necessary credentials.

- **.gitignore**: Git ignore file specifying untracked files that Git should ignore, including `.env` and temporary files.

## Getting Started

To run the project:

1. Set up your AWS Bedrock credentials in the `.env` file.
2. Place your legal documents in the `backend/documents/` directory.
3. Navigate to the `frontend` directory and start a local server to serve the frontend files.
4. Start the backend server by running `main.py` in the `backend` directory.
5. Open your web browser and navigate to the local server URL to view the frontend.
6. Explore the document summaries!