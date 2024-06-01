function showUploadPopup() {
    openPopup("File uploaded successfully. Voice cloning in progress...");
}

function openPopup(message) {
    document.getElementById('popup-message').textContent = message;
    document.getElementById('popup').classList.add('open');
    document.getElementById('overlay').classList.add('open');
}

function closePopup() {
    document.getElementById('popup').classList.remove('open');
    document.getElementById('overlay').classList.remove('open');
}

function clearForm() {
    document.getElementById('file').value = '';
    document.getElementById('model').selectedIndex = 0;
    var audio = document.getElementById('processed-audio');
    if (audio) {
        audio.src = '';
    }
}
