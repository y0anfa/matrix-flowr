const dropdowns = Array.from(document.querySelectorAll('.dropdown'));

dropdowns.forEach((dropdown) => {
    const dropdownTrigger = dropdown.querySelector('.dropdown-trigger button');

    dropdownTrigger.addEventListener('click', () => {
        dropdown.classList.toggle('is-active');
    });
});

document.addEventListener('click', function (event) {
    // Fermer les dropdowns ouverts lors d'un clic en dehors d'un dropdown
    if (!event.target.closest('.dropdown')) {
        dropdowns.forEach(function (dropdown) {
            dropdown.classList.remove('is-active');
        });
    }
});

dropdowns.forEach(function (dropdown) {
    const dropdownTrigger = dropdown.querySelector('.dropdown-trigger button');

    dropdownTrigger.addEventListener('click', function () {
        // Fermer les autres dropdowns ouverts
        dropdowns.forEach(function (otherDropdown) {
            if (otherDropdown !== dropdown) {
                otherDropdown.classList.remove('is-active');
            }
        });

        dropdown.classList.toggle('is-active');
    });
});