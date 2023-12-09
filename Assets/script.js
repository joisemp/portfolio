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
            copyButton.innerHTML = '<img src="./Assets/copy-regular.svg" class="copy-icon" id="copyIcon" alt="">' + emailAddress;
          } else {
            copyButton.innerHTML = '<img src="./Assets/copy-regular.svg" class="copy-icon" id="copyIcon" alt="">Copy Email';
          }
          copyIcon.style.display = 'inline';
        }, 2000);
      })
      .catch(err => console.error('Error copying text: ', err));
  };
});
