document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const cancelBtn = document.getElementById('cancel');
    const errorMsg = document.getElementById('error-message');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        errorMsg.textContent = '';
        const user = document.getElementById('user').value;
        const pass = document.getElementById('pass').value;
        try {
            const res = await fetch(`/api/login/?user=${encodeURIComponent(user)}&pass=${encodeURIComponent(pass)}`);
            const data = await res.json();
            if (res.ok && data.success) {
                window.location.href = '/bienvenido/';
            } else {
                errorMsg.textContent = data.error || 'Error de autenticación';
            }
        } catch (err) {
            errorMsg.textContent = 'Error de conexión';
        }
    });

    cancelBtn.addEventListener('click', function() {
        form.reset();
        errorMsg.textContent = '';
    });
});
