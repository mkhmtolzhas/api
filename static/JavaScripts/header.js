// // window.addEventListener('scroll', function() {
// //     var header = document.getElementById('site-header');
// //     var scrollPosition = window.scrollY;
  
// //     if (scrollPosition > 0) {
// //       header.classList.add('transparent');
// //     } else {
// //       header.classList.remove('transparent');
// //     }
// //   });


//   window.addEventListener('scroll', function() {
//     var section = document.querySelector('.home');
//     var windowHeight = window.innerHeight;
//     var scrollY = window.scrollY || window.pageYOffset;
  
//     // Проверяем, достигла ли прокрутка 100vh по оси Y
//     if (scrollY >= windowHeight) {
//       section.classList.add('transparent');
//     } else {
//       section.classList.remove('transparent');
//     }
//   });


window.addEventListener('scroll', function() {
  var header = document.getElementById('site-header');
  var homeSection = document.querySelector('.home');
  var windowHeight = window.innerHeight;
  var scrollY = window.scrollY || window.pageYOffset;

  // Проверяем, прокрутил ли пользователь за секцию .home
  if (scrollY > homeSection.clientHeight) {
    header.style.backgroundColor = '#303133';
  } else {
    header.style.backgroundColor = 'transparent';
  }
});
