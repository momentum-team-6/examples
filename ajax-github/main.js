/* eslint-disable prefer-const, no-unused-vars */
/* globals fetch */

const url = 'https://api.github.com/orgs/momentum-team-6'
const container = document.querySelector('#github-data')

// fetch(url)
//   .then(function (response) {
//     return response.json()
//   })
//   .then(function (data) {
//     console.log(data)
//     container.innerHTML = `<h1>${data.name}</h1>`
//   })

fetch(url)
  .then(res => res.json())
  .then(data => {
    container.innerHTML = `<h1>${data.name}</h1>`
    return data.repos_url
  })
  .then(reposUrl => fetch(reposUrl))
  .then(res => res.json())
  .then(data => {
    const list = document.createElement('ul')
    container.appendChild(list)
    for (let repo of data) {
      const listItem = document.createElement('li')
      listItem.innerText = repo.name
      list.appendChild(listItem)
    }
  })
