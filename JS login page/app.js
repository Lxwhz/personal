// Dummy users database
const users = {
    'admin': 'password',
    'user': 'userpass'
};

function login(event) {
    event.preventDefault();

    // Get username and password
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Validate credentials
    if (users[username] && users[username] === password) {
        // Hide login page and show dashboard
        document.getElementById('login-page').style.display = 'none';
        document.getElementById('dashboard-page').style.display = 'block';
        document.getElementById('welcome-username').textContent = username;
    } else {
        // Show error message
        document.getElementById('login-error').style.display = 'block';
    }
}

function logout() {
    // Hide dashboard and show login page
    document.getElementById('dashboard-page').style.display = 'none';
    document.getElementById('login-page').style.display = 'block';
    document.getElementById('login-error').style.display = 'none';

    // Clear form fields
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
}