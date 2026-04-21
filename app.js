const uploadForm = document.getElementById('uploadForm');
const statusBox = document.getElementById('status');
const statusMsg = document.getElementById('statusMessage');

uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];

    if (!file) return;

    // 1. Prepare the data for Python (Flask/FastAPI)
    const formData = new FormData();
    formData.append('file', file); // 'file' is the key the backend will look for

    // 2. Show 'Loading' state
    statusBox.className = "status-box"; // Reset classes
    statusMsg.innerText = "Sending to backend for analysis...";
    statusBox.classList.remove('hidden');

    try {
        // 3. The Fetch Request (Update URL when backend is ready)
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            statusBox.classList.add('success');
            statusMsg.innerText = "Analysis Complete! Check console for results.";
            console.log("Backend Response:", data);
        } else {
            throw new Error("Server error");
        }
    } catch (error) {
        statusBox.classList.add('error');
        statusMsg.innerText = "Upload failed. Is the backend server running?";
        console.error("Error:", error);
    }
});