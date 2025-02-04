let apiUrl;

fetch('/config.json')
    .then(response => response.json())
    .then(config => {
        apiUrl = config.apiUrl;
    });

function fetchPrint() {
    const message = document.getElementById('printMessage').value;
    fetch(apiUrl + '/print', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
        .then(response => response.json())
        .then(data => {
            displayMessage('printResponse', 'Your Message: ' + data.print, 'success');
        });
}

function fetchAdd() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    fetch(`${apiUrl}/add?num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                displayMessage('addResponse', 'Error: ' + data.error, 'error');
            } else {
                displayMessage('addResponse', 'Sum: ' + data.result, 'success');
            }
        });
}

function fetchUser() {
    const userId = document.getElementById('userId').value;
    fetch(apiUrl + '/user/' + userId)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                displayMessage('userResponse', 'Error: ' + data.error, 'error');
            } else {
                displayMessage('userResponse', `Name: ${data.name}, Email: ${data.email}`, 'success');
            }
        });
}

function displayMessage(elementId, message, type) {
    const element = document.getElementById(elementId);
    element.className = `output show ${type}`;
    element.innerText = message;
}

function fetchConfig() {
    fetch(apiUrl + '/config')
        .then(response => response.json())
        .then(data => {
            let message = 'Config:\n';
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    message += `${key}: ${data[key]}\n`;
                }
            }
            displayMessage('configResponse', message, 'success');
        });
}