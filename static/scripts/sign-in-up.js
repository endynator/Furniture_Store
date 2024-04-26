document.addEventListener("DOMContentLoaded", function () {
    const changeContentLinks = document.querySelectorAll("#changeContentLink");
    const changeformContainers = document.querySelectorAll(".content");

    changeContentLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            changeformContainers.forEach(container => {
                container.classList.toggle("hidden");
            });
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
  const inputBoxes = document.querySelectorAll('.signin .content .form .inputBox input');

  inputBoxes.forEach(function(input) {
      input.addEventListener('focus', function() {
          this.classList.add('animated');
      });

      input.addEventListener('blur', function() {
          if (this.value === '') {
              this.classList.remove('animated');
          }
      });

      if (input.value !== '') {
          input.classList.add('animated');
      }
  });
});
