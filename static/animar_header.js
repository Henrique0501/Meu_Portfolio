const nav = document.querySelector('header');

window.addEventListener('scroll', function() {
  const offset = window.pageYOffset;

  if(offset > 75)
    nav.classList.add('scroll')
  else
    nav.classList.remove('scroll')
});

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector('header').style.top = "0";
  } else {
    document.querySelector('header').style.top = "-200px";
  }
  prevScrollpos = currentScrollPos;
}