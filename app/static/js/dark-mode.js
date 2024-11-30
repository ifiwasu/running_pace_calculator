document.addEventListener('DOMContentLoaded', (event) => {
    const toggleButton = document.getElementById('dark-mode-toggle');
    const body = document.body;

    // Function to toggle dark mode classes
    const toggleDarkModeClasses = () => {
        const cards = document.querySelectorAll('.card');
        const formControls = document.querySelectorAll('.form-control');

        cards.forEach(card => {
            card.classList.toggle('bg-dark');
            card.classList.toggle('text-white');
        });

        formControls.forEach(control => {
            control.classList.toggle('bg-dark');
            control.classList.toggle('text-white');
        });
    };

    // Check localStorage for dark mode setting
    if (localStorage.getItem('dark-mode') === 'enabled') {
        body.classList.add('dark-mode');
        toggleDarkModeClasses();
    }

    toggleButton.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        toggleDarkModeClasses();
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('dark-mode', 'enabled');
        } else {
            localStorage.setItem('dark-mode', 'disabled');
        }
    });
});