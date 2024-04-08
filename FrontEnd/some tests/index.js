window.addEventListener('scroll', function() {
    var header = document.getElementById('site-header');
    var scrollPosition = window.scrollY;
  
    if (scrollPosition > 0) {
      header.classList.add('transparent');
    } else {
      header.classList.remove('transparent');
    }
  });
  