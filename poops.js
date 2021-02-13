var slideIndex = 0;
carousel();

function carousel() {
    var i;
    var x1 = document.getElementsByClassName("Text");
    for (i = 0; i < x1.length; i++) {
      x1[i].style.display = "none";
    }
    var x2 = document.getElementsByClassName("mySlides");
    for (i = 0; i < x2.length; i++) {
      x2[i].style.display = "none";
    }
    
    slideIndex++;
    if (slideIndex > x2.length) {slideIndex = 1}
    x1[slideIndex-1].style.display = "block";
    x2[slideIndex-1].style.display = "block";
    setTimeout(carousel,#Delay); // Change image every 100 ms
}
