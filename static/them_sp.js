document.querySelectorAll('.dropdown-menu').forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        const btn = document.querySelector('.btn-secondary');
        btn.textContent = e.target.textContent;
    });
});
document.getElementById('formFileLg').addEventListener('change', function(e) {
    var file = e.target.files[0];
    var imageType = /image.*/;

    if (!file.type.match(imageType)) {
        alert('File is not an image.');
        return;
    }

    var reader = new FileReader();
    reader.onload = function(e) {
        var img = document.getElementById('picture');
        img.src = reader.result;
    }
    reader.readAsDataURL(file);
});