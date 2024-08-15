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
