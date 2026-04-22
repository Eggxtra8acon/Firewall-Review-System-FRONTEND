// 1. Grab the elements from your HTML
const uploadForm = document.getElementById('uploadForm');
const statusBox = document.getElementById('status');
const statusMsg = document.getElementById('statusMessage');

// 2. Listen for when the "Analyze Rules" button is clicked
uploadForm.addEventListener('submit', async (e) => {
    // This stops the page from refreshing automatically
    e.preventDefault();
    
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];

    // Check if a file was actually selected
    if (!file) return;

    // 3. Create the "Digital Envelope" (FormData)
    // Your Python backend teammates will look for the key name 'file'
    const formData = new FormData();
    formData.append('file', file);

    // 4. Update the UI to show progress
    statusBox.className = "status-box"; // Reset any previous error/success colors
    statusMsg.innerText = "Processing your firewall rules...";
    statusBox.classList.remove('hidden');

    try {
        /* 5. THE HANDSHAKE (Fetch API)
           We send the data to the backend. 
           NOTE: 'http://127.0.0.1:5000/upload' is a placeholder. 
           Your teammates will give you their actual server URL later.
        */
        const response = await fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            statusBox.classList.add('success');
            statusMsg.innerText = "Rules analyzed successfully!";
            
            // This is where you'll see the results in the VS Code Console (F12)
            console.log("Data from Python:", data);
        } else {
            throw new Error("Backend server error");
        }
    } catch (error) {
        // If the Python server isn't running, it will land here
        statusBox.classList.add('error');
        statusMsg.innerText = "Could not connect to the backend server.";
        console.error("Connection Error:", error);
    }
});