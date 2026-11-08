document.addEventListener('DOMContentLoaded', function () {
    var spinner = document.getElementById('spinner');

    if (spinner) {
        spinner.classList.remove('show');
        spinner.remove();
    }
});