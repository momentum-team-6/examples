/* globals fetch, moment */

const url = 'http://localhost:3000/todos/'

const form = document.querySelector('#todo-form')
const todoList = document.querySelector('#todo-list')

// Right now this is running as soon as the page loads, which is ok but not great
// I will want to put this inside a function and/or an event listener when we revise this code tomorrow
fetch(url)
  .then(res => res.json())
  .then(data => {
    for (let todo of data) {
      console.log(todo.item)
      renderTodoItem(todo)
    }
  })

form.addEventListener('submit', function (event) {
  event.preventDefault()
  const todoText = document.querySelector('#todo-text').value
  createTodo(todoText)
})

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
      renderTodoItem(data)
    })
}

function renderTodoItem (todoObj) {
  const itemEl = document.createElement('li')
  itemEl.innerText = todoObj.item
  todoList.appendChild(itemEl)
}
