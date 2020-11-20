/* globals fetch, moment */

const url = 'http://localhost:3000/todos/'
const form = document.querySelector('#todo-form')
const todoList = document.querySelector('#todo-list')

/* Event listeners */

form.addEventListener('submit', function (event) {
  event.preventDefault()
  const todoText = document.querySelector('#todo-text').value
  createTodo(todoText)
})

todoList.addEventListener('click', function (event) {
  if (event.target.classList.contains('delete')) {
    deleteTodo(event.target)
  }
  if (event.target.classList.contains('edit')) {
    editTodo(event.target)
  }
  if (event.target.id === 'update-todo') {
    updateTodo(event.target)
  }
})

/* CRUD functions */

function listTodos () {
  // fetch(url)
  //   .then(res => res.json())
  //   .then(data => {
  //     for (let todo of data) {
  //       console.log(todo.item)
  //       renderTodoItem(todo)
  //     }
  //   })

  // same as above, without arrow functions
  fetch(url)
    .then(function (response) {
      return response.json()
    })
    .then(function (data) {
      // Now I have data I can work with
      console.log(data)
      for (let todo of data) {
        console.log(todo)
        renderTodoItem(todo)
      }
    })
}

function createTodo (todoText) {
  fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      item: todoText,
      created_at: moment().format()
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      renderTodoItem(data)
    })
}

function deleteTodo (element) {
  const todoId = element.parentElement.id
  fetch(`http://localhost:3000/todos/${todoId}`, {
    method: 'DELETE'
  })
    .then(function (res) {
      return res.json()
    })
    .then(function (data) {
      // remove the item from the DOM
    })
}

function updateTodo (element) {
  const todoId = element.parentElement.id
  const todoText = document.querySelector('#edit-text')
  fetch(`http://localhost:3000/todos/${todoId}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      item: todoText.value,
      updated_at: moment().format()
    })
  })
    .then(function (res) {
      return res.json()
    })
    .then(function (data) {
      console.log(data)
      // update the item in the DOM
      // clear & hide the input
    })
}

/* DOM manipulation */

function renderTodoItem (todoObj) {
  const itemEl = document.createElement('li')
  itemEl.id = todoObj.id
  itemEl.classList.add(
    'lh-copy',
    'pv3',
    'ba',
    'bl-0',
    'bt-0',
    'br-0',
    'b--dotted',
    'b--black-3'
  )
  itemEl.innerHTML = `${todoObj.item}<i class="ml2 dark-red fas fa-times delete"></i><i class="ml2 fas fa-edit edit"></i>`
  todoList.appendChild(itemEl)
  clearInputs()
}

function editTodo (element) {
  const todoId = element.parentElement.id
  showTextInput(element)
}

function showTextInput (element) {
  const todoListItem = element.parentElement
  const textField = document.createElement('input')
  textField.type = 'text'
  textField.id = 'edit-text'
  textField.classList.add('ml3')
  todoListItem.appendChild(textField)
  const saveButton = document.createElement('button')
  saveButton.innerText = 'Save changes'
  saveButton.id = 'update-todo'
  saveButton.classList.add(
    'f6',
    'link',
    'dim',
    'br-pill',
    'p1',
    'ml1',
    'mb2',
    'dib',
    'white',
    'bg-green'
  )
  todoListItem.appendChild(saveButton)
}

function clearInputs () {
  const inputs = document.querySelectorAll('input')
  for (let field of inputs) {
    field.value = ''
  }
}

// calling this to populate the page with existing todos on page load
listTodos()
