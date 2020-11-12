const alpacaPic = document.querySelector('#alpaca-pic')
const animalPics = document.querySelector('.animal-pics')

alpacaPic.addEventListener('click', function (event) {
  console.log(event.target)
  console.log('You clicked the alpaca!')
})

animalPics.addEventListener('click', function (event) {
  console.log(event.target)
  event.target.classList.add('highlight')
})

const buttons = document.querySelector('.number-buttons')
const display = document.querySelector('#display-number')

buttons.addEventListener('click', function (event) {
  console.log(event.target)
  display.innerHTML = `<p id="output">Hi! The number you clicked is ${event.target.innerText}.</p>`
})

document.querySelector('.clear-button').addEventListener('click', function () {
  document.querySelector('#output').innerHTML = ''
})
