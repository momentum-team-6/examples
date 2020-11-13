/* eslint-disable prefer-const */
let form = document.querySelector('#registration-form')
let formIsValid

form.addEventListener('submit', e => {
  e.preventDefault()
})

form.addEventListener('click', validate)

function validate (event) {
  removeValidMessage()
  formIsValid = true
  form.checkValidity()

  confirmPasswordMatch()
  // TODO: add more validation functions here

  // if everything is valid, we want to show a message at the bottom
  showValidMessage()
}

function confirmPasswordMatch () {
  // grab the password input
  let password = document.querySelector('#password-input')
  // grab the confirm password input
  let confirmPwd = document.querySelector('#confirm-password')

  // compare their values to see if they match
  if (password.value !== confirmPwd.value) {
    confirmPwd.setCustomValidity('HEY Your passwords must match')
    markFormAsInvalid()
  } else {
    confirmPwd.setCustomValidity('')
  }
}

function showValidMessage () {
  if (formIsValid) {
    const validMsgEl = document.createElement('h2')
    validMsgEl.id = 'valid-message'
    const validMsgText = document.createTextNode('This form is valid!')
    validMsgEl.appendChild(validMsgText)
    document.querySelector('main').appendChild(validMsgEl)
  }
}

function removeValidMessage () {
  let validMsg = document.querySelector('#valid-message')
  if (validMsg) {
    validMsg.remove()
  }
}

function markFormAsInvalid () {
  formIsValid = false
}
