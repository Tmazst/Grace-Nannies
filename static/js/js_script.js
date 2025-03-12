


////Fixed Sticky
//window.onscroll = function() {scrollFunction()};
//
//function scrollFunction() {
//  var scrollingElement = document.getElementById("nav-div");
//  // Distance from the top of the document to the top of the scrolling element
//  var elementOffset = scrollingElement.offsetTop;
//  // Viewport (window) top position
//  var windowTop = window.pageYOffset || document.documentElement.scrollTop;
//
//  if (windowTop > elementOffset) {
//    scrollingElement.style.position = "fixed";
//    scrollingElement.style.top = "0";
//  } else {
//    scrollingElement.style.position = "relative";
//  }
//}
function sideNavFunc1(event){
  // var popScrnLogo = document.getElementById("updates");
  // popScrnLogo.classList.toggle("show-popup");
  console.log("Side Nav");
  let sideNavBg = document.querySelector('#side-navig-bg');
  let sideNavCont = document.querySelector("#side-navig-cont");
  // document.querySelector("#commentField").value = "";
  sideNavBg.classList.toggle("show-popup");
  sideNavCont.classList.toggle("show-menu1");
  sideNavCont.classList.remove("gen-flex-col");
  };

function sideNavFunc(event){
  // var popScrnLogo = document.getElementById("updates");
  // popScrnLogo.classList.toggle("show-popup");
  console.log("Side Nav");
  let sideNavBg = document.querySelector('#side-navig-bg');
  let sideNavCont = document.querySelector("#side-navig-cont");
  // document.querySelector("#commentField").value = "";
  sideNavBg.classList.toggle("show-popup");
  sideNavCont.classList.toggle("show-menu");
  };

function closeSideNavFunc(){
  // var popScrnLogo = document.getElementById("updates");
  // popScrnLogo.classList.toggle("show-popup");
  console.log("Side Nav");
  let sideNavBg = document.querySelector('#side-navig-bg');
  let sideNavCont = document.querySelector("#side-navig-cont");
  // document.querySelector("#commentField").value = "";
  sideNavBg.classList.remove("show-popup");
  sideNavCont.classList.remove("show-menu");

  };


//Navigation Dropdown
const navSlide = () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav-links");
  const navLinks = document.querySelectorAll(".nav-links a");

if( nav && burger && navLinks.length > 0){
  burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");

    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = "";
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${
          index / 7 + 0.5
        }s `;
      }
    });
    burger.classList.toggle("toggle");
  });
  //
};
}
navSlide();


function calculateDays() {
    var adJob = document.querySelectorAll("#deadline-div");
    var adDeadline = document.querySelectorAll("#deadline");
    var daysLeft = document.querySelectorAll("#days_left");


    var date = new Date();
    var today = date.getTime(); // Get today's date in milliseconds to compare with deadlines
    if( adJob.length > 1 ){
        for(var i = 0; i < adDeadline.length; i++) {
            // Get each ad's deadline
            var targetedAd = adDeadline[i];
            // Get the targeted ad's date tag and convert it to a Date object
            var deadline = new Date(targetedAd.innerText);
    //        console.log(deadline);

            // Calculate the days between today's date and the deadline
            var difference = Math.floor((deadline.getTime() - today) / (1000 * 60 * 60 * 24)); // Convert the time difference to days
    //        console.log("There are still plenty of time: ",difference);

            if (difference > 10) {
                adJob[i].classList.toggle("deadline-is-far");
                daysLeft[i].innerText = difference + " Days Left";
    //            console.log("There are still plenty of time");

            } else if (difference <= 10 && difference > 0) {
                adJob[i].classList.toggle("deadline-is-close");
                daysLeft[i].innerText = difference + " Days Left";
    //            console.log("We are getting closer to the deadline");

            } else if (difference <= 3 && difference >= 0) {
                adJob[i].classList.toggle("deadline-is-today");
                daysLeft[i].innerText = difference + " Days Left";
    //            console.log("Deadline is today");

            } else if (difference < 0) {
                adJob[i].classList.toggle("deadline-is-over");
                daysLeft[i].innerText = "Closed";
            }
        }
    };

}

calculateDays();




// Function to handle the scroll event
function handleScroll() {

//      console.log("Scroll Called1");
      // Get the navigation menu element
      const navigation = document.getElementById('nav-div-cont');

      // Store the last known scroll position
      let lastScrollTop = 0;

      // Get the height of the window
      const windowHeight = window.innerHeight;

      // Get the current scroll position
      const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

      // Determine the scroll direction
      const scrollDirection = currentScroll > lastScrollTop ? 'down' : 'up';


       if (window.innerWidth <= 768){
          // If the user is scrolling down and the navigation is not already at the bottom
          if (scrollDirection === 'down' && (windowHeight + currentScroll) >= document.body.offsetHeight-4000) {
            console.log("Scroll Called",currentScroll,scrollDirection);
            navigation.style.position = 'fixed';
            navigation.style.bottom = '0';
          } else {
            navigation.style.position = 'static';
          }

          // Update the known scroll position
          lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;

    }else{

      var scrollingElement = document.getElementById("nav-div");
      // Distance from the top of the document to the top of the scrolling element
      var elementOffset = scrollingElement.offsetTop;
      // Viewport (window) top position
      var windowTop = window.pageYOffset || document.documentElement.scrollTop;

      if (windowTop > elementOffset) {
        scrollingElement.style.position = "fixed";
        scrollingElement.style.top = "0";
      } else {
        scrollingElement.style.position = "relative";
      }


    }
}

// window.onscroll = function() {handleScroll()};
// Add the scroll event listener
//window.addEventListener('scroll', handleScroll);




// Get references to the login button and the 2FA checkbox
let loginButton = document.getElementById("login_btn");
let twoFactorAuthCheckbox = document.getElementById("2fa_check_box");

// Event listener for the login button click
//loginButton.addEventListener('click', function() {
//    console.log("Login Submitted"); // Corrected typo: Changed 'log' to 'console'
//    if (twoFactorAuthCheckbox.checked) {
//        startOTPTimer();
//    }
//});
//
//// Event listener for the 2FA checkbox change
//twoFactorAuthCheckbox.addEventListener('change', function() {
//    console.log("2 Factor Checked"); // Corrected typo: Changed 'log' to 'console'
//    if (this.checked && loginButton.clicked) {
//        startOTPTimer();
//    }
//});



var blogContent = document.getElementsByClassName("text-limit");

for(var i=0; i<blogContent.length; i++){
    if (blogContent[i].textContent.length > 100) {

            blogContent[i].textContent = blogContent[i].textContent.substring(0,100) + "[...]";
        }
    }






//function checkDate(){
//
//    var applyBtn = document.querySelector(".jb-viewed-card-body a");
//    var appDeadline = document.querySelector("#deadline");
//
//    var date = new Date();
//    var today = date.getTime(); // Get today's date in milliseconds to compare with deadlines
//
//    var deadline = new Date(appDeadline.innerText);
//
//    console.log("Clicked!!",deadline.getTime());
//
//    // Calculate the days between today's date and the deadline
//    var differenceDate = (deadline.getTime() - today) / (1000 * 60 * 60 * 24);
//
//    if (differenceDate < 0) {
//            applyBtn.style.visibility="hidden";
//            console.log("Clicked!!",difference);
//    }
//}

//Dashboard
const navSideSlide = () => {
  const dashboardBtn = document.querySelector("#dashboard-btn");
  const nav = document.querySelector(".sidebar-main");
  const navLinks = document.querySelectorAll(".sidebar-main a");

if( dashboardBtn && nav && navLinks.length > 0){
  dashboardBtn.addEventListener("click", () => {
    nav.classList.toggle("nav-active-drw");

    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = "";
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${
          index / 7 + 0.5
        }s `;
      }
    });
    dashboardBtn.classList.toggle("toggle");
  });
  //
};
}
navSideSlide();


