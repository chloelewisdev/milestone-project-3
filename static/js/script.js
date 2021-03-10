//Only runs function when page is ready:
$(document).ready(function() {

//Add or remove active class on nav 
$(".nav-link").on("click", function() {
        $("a.nav-link").removeClass("active");
        $(this).addClass("active");
    });
});

//Scroll to top button - code from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, the button shows
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// Closes mobile dropdown menu after item clicked - source: https://stackoverflow.com/questions/42401606/how-to-hide-collapsible-bootstrap-4-navbar-on-click        
$('.navbar-nav>li>a').on('click', function() {
    $('.navbar-collapse').collapse('hide');
});

