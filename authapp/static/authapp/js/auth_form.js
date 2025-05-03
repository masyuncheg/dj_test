document.addEventListener('DOMContentLoaded', function () {
    async function getCSRFToken() {
    await fetch('', { method: 'GET', credentials: 'same-origin' });
    }

    getCSRFToken();

    const  auth = document.getElementById('auth_form');

    auth.addEventListener('submit', async function (e) {
    e.preventDefault();
    const data = new FormData(auth);
    const response = await fetch('', {
    method: 'POST',
    body: data,
    headers: {
    'X-CSRFToken': document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1] || ''
    }

    });

    const res = await response.json();
    document.getElementById('result').innerText = JSON.stringify(res);
    });
    });
    