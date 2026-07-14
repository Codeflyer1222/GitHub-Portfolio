"use strict"

/*
   New Perspectives on HTML5 and CSS3, 8th Edition
   Tutorial 9
   Coding Challenge 2

   Countdown Clock
   Author: Samuel Brown
   Date:   11/22/2024


*/
var secsLeft = 10; 
setInterval("countdown()", 1000);
function countdown() {
   var secsString = addLeadingZero(secsLeft);
   document.getElementById("seconds").textContent = secsString;
   checkCountdown();
   secsLeft -= 1;
}

function stopCountdown() {
   document.getElementById("Alert").textContent = "Time's Up";
   clearInterval(clock);
}


/* ------------------------------------------------- */


/* The checkCountdown() function tests whether there is any time left to make the
   ticket order. If the time left is 0, the stopClock() function is run;
   otherwise nothing happens and the program continues to run. */
   
function checkCountdown() {
   if (secsLeft === 0) stopCountdown();
}


/* The addLeadingZero() function adds a leading zero to values which are less than 10 */

function addLeadingZero(num) {
   var numStr = (num < 10) ? ("0" + num) : "" + num;
   return numStr;
}
