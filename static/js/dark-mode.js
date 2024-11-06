document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('dark-mode-toggle');
    const body = document.body;

    toggleButton.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
        document.querySelectorAll('.card').forEach(element => {
            element.classList.toggle('bg-dark');
            element.classList.toggle('text-white');
        });
        document.querySelectorAll('.form-control').forEach(element => {
            element.classList.toggle('bg-dark');
            element.classList.toggle('text-white');
        });
    });
});