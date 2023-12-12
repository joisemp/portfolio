document.addEventListener('DOMContentLoaded', function () {
  window.copyEmail = function () {
    const copyButton = document.getElementById('copyButton');
    const copyIcon = document.getElementById('copyIcon');
    const windowWidth = window.innerWidth;
    const emailAddress = 'joise1124@gmail.com';

    navigator.clipboard.writeText(emailAddress)
      .then(() => {
        copyButton.innerText = 'Email copied!';
        setTimeout(() => {
          if (windowWidth > 900) {
            copyButton.innerHTML = '<i class="fa-regular fa-copy copy-icon pe-md-3 pe-2"></i>' + emailAddress;
          } else {
            copyButton.innerHTML = '<i class="fa-regular fa-copy copy-icon pe-md-3 pe-2"></i>Copy Email';
          }
          copyIcon.style.display = 'inline';
        }, 2000);
      })
      .catch(err => console.error('Error copying text: ', err));
  };
});
