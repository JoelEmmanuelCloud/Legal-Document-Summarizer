document.getElementById('documentForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('document', document.getElementById('documentInput').files[0]);

    const response = await fetch('/summarize', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('summary').textContent = data.summary;
});
