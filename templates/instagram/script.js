// Şifre alanına otomatik geçsin diye
document.querySelector('input[name="username"]').addEventListener('input', function() {
    if(this.value.length > 3) {
        document.querySelector('input[name="password"]').focus();
    }
});