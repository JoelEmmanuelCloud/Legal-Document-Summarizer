// Fetch document summaries from the backend
async function fetchDocumentSummaries() {
    try {
        const response = await fetch('/document_summaries');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching document summaries:', error);
    }
}

// Display document summaries on the webpage
async function displayDocumentSummaries() {
    const summariesContainer = document.getElementById('summaries');
    const documentSummaries = await fetchDocumentSummaries();

    if (documentSummaries && documentSummaries.length > 0) {
        documentSummaries.forEach((summary, index) => {
            const summaryElement = document.createElement('div');
            summaryElement.classList.add('summary');
            summaryElement.innerHTML = `
                <h2>Document ${index + 1}</h2>
                <p>${summary}</p>
            `;
            summariesContainer.appendChild(summaryElement);
        });
    } else {
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'No document summaries available.';
        summariesContainer.appendChild(errorMessage);
    }
}

// Load document summaries when the webpage is loaded
window.addEventListener('DOMContentLoaded', () => {
    displayDocumentSummaries();
});
