/**
 * Lab 3: Random Redirector
Create a page which randomly redirectly to another. 
Create an array of urls (as strings), and randomly pick one using Math.random(). 
Then redirect to the page using window.location.

Version 2
Using JavaScript's timing events show a 5-second countdown to the user.
 When the countdown is finished, redirect to a random page.
 */

const URLs = [
  "https://google.com",
  "https://bing.com",
  "https://startpage.com",
];

const randRedir = () => {
  window.location = URLs[Math.floor(Math.random() * URLs.length)];
};
// randRedir();
let countDown = 5;

const app = document.getElementById("app");
const setTime = time => (app.innerHTML = time);

setInterval(() => {
  --countDown;
  setTime(countDown);
  if (countDown < 1) randRedir();
}, 1000);
