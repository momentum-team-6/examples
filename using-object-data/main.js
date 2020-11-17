/* DATA */
const menuItems = [
  {
    title: 'Noodles',
    imgUrl:
      'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60'
  },
  {
    title: 'Burgers',
    imgUrl:
      'https://images.unsplash.com/photo-1550950158-d0d960dff51b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80'
  },
  {
    title: 'Breakfast',
    imgUrl:
      'https://images.unsplash.com/photo-1459789034005-ba29c5783491?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1450&q=80'
  },
  {
    title: 'Dessert',
    imgUrl:
      'https://images.unsplash.com/photo-1514849302-984523450cf4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80'
  }
]

const menuItemsContainer = document.querySelector('.menu-items')

// This lets us loop over all the menuItems and insert them into the DOM using innerHTML
function renderMenu () {
  for (let menuItem of menuItems) {
    const menuItemCard = document.createElement('div')
    menuItemCard.classList.add('menu-item')

    menuItemsContainer.innerHTML += `<div class='menu-item'>
    <h3>${menuItem.title}</h3>
    <img src=${menuItem.imgUrl}>
</div>`
  }
}

window.addEventListener('load', () => renderMenu())

// All of what follows is a demo of creating DOM content using a single item I've
// selected from the array of objects above, without looping. This is not how you would
// want to do it, but it demonstrates how you want to take each item and do the same thing with it

// const menuItemCard = document.createElement('div')
// menuItemCard.classList.add('menu-item')

// menuItemsContainer.innerHTML = `<div class='menu-item'>
//     <h3>${menuItem.title}</h3>
//     <img src=${menuItem.imgUrl}>
// </div>`

// const menuItem2 = menuItems[1]
// const menuItem2Card = document.createElement('div')
// menuItem2Card.classList.add('menu-item')

// menuItemsContainer.innerHTML += `<div class='menu-item'>
//     <h3>${menuItem2.title}</h3>
//     <img src=${menuItem2.imgUrl}>
// </div>`

// const menuItem3 = menuItems[2]
// const menuItem3Card = document.createElement('div')
// menuItem3Card.classList.add('menu-item')

// menuItemsContainer.innerHTML += `<div class='menu-item'>
//     <h3>${menuItem3.title}</h3>
//     <img src=${menuItem3.imgUrl}>
// </div>`

// Here is an alternate way to insert content, creating individual elements and
// appending them to parent elements using appendChild()
function alternateRenderMenu () {
  for (let menuItem of menuItems) {
    const menuItemCard = document.createElement('div')
    menuItemCard.classList.add('menu-item')
    const menuItemTitle = document.createElement('h3')
    const text = document.createTextNode(menuItem.title)
    menuItemTitle.appendChild(text)
    menuItemCard.appendChild(menuItemTitle)
    const menuItemImg = document.createElement('img')
    menuItemImg.src = menuItem.imgUrl
    menuItemCard.appendChild(menuItemImg)
    menuItemsContainer.appendChild(menuItemCard)
  }
}
