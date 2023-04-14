// const text = "Code Culture is a company dedicated to teaching a variety of different programming skills aimed to make you a master at front end, back end, and machine learning. Our goal is to provide you with the knowledge and tools you need to become a successful developer, whether you're just starting out or looking to improve your skills. With our expert instructors, hands-on projects, and comprehensive curriculum, you'll gain the experience and confidence you need to take your programming skills to the next level. Welcome to Code Culture!";
// const dynamicTxt = document.querySelector('.dynamic-txt');
// const cursor = document.querySelector('.blinking-cursor');

// function typeText() {
//   let i = 0;
//   const intervalId = setInterval(() => {
//     if (text[i] === ' ') {
//       dynamicTxt.innerHTML += '<span>&nbsp;</span><span>&nbsp;</span>';
//     } else {
//       dynamicTxt.innerHTML += `<span>${text[i]}</span>`;
//     }
//     let spanWidths = 0;
//     for (let j = 0; j <= i; j++) {
//       spanWidths += dynamicTxt.children[j].offsetWidth;
//     }
//     cursor.style.left = `${dynamicTxt.offsetLeft + spanWidths}px`;
//     i++;
//     if (i >= text.length) {
//       clearInterval(intervalId);
//     }
//   }, 50);
// }

// setTimeout(typeText, 3000);

const dynamicTxt = document.querySelector(".dynamic-txt");
const text = ["Code Culture is a company dedicated to teaching a variety of different programming skills aimed to make you a master at front end, back end, and machine learning. Our goal is to provide you with the knowledge and tools you need to become a successful developer, whether you're just starting out or looking to improve your skills. With our expert instructors, hands-on projects, and comprehensive curriculum, you'll gain the experience and confidence you need to take your programming skills to the next level. Welcome to Code Culture!"];
let wordIndex = 0;
let txtIndex = 0;
let isDeleting = false;
let delay = 150;

function typeWords() {
  const currentWordIndex = wordIndex % text.length;
  const currentWord = text[currentWordIndex];

  if (!isDeleting) {
    dynamicTxt.textContent = currentWord.substring(0, txtIndex);
    txtIndex++;

    if (txtIndex > currentWord.length) {
      isDeleting = true;
      delay = 2000;
    }
  } else {
    dynamicTxt.textContent = currentWord.substring(0, txtIndex);
    txtIndex--;

    if (txtIndex === 0) {
      isDeleting = false;
      wordIndex++;
      delay = 500;
    }
  }

  setTimeout(typeWords, delay);
}

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(typeWords, delay);
});