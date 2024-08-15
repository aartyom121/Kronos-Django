document.getElementById('toggleButton').addEventListener('click', function() {
    var paragraphs = document.querySelectorAll('p');
    paragraphs.forEach(function(paragraph) {
        if (paragraph.classList.contains('hidden')) {
            paragraph.classList.remove('hidden');
        } else {
            paragraph.classList.add('hidden');
        }
    });
});

document.getElementById('toggleButton').addEventListener('click', function() {
    var containers = document.querySelectorAll('.container');
    containers.forEach(function(container) {
        if (container.classList.contains('hidden')) {
            container.classList.remove('hidden');
        } else {
            container.classList.add('hidden');
        }
    });
});