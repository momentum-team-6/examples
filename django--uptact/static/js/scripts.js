console.log(' js loaded')

let stars = document.querySelectorAll(".fa-star")
console.log(stars)

for (let star of stars) {
    star.addEventListener('click', e => {
    let contactPk = e.target.parentElement.parentElement.dataset.contactPk;
    let url = `contacts/${contactPk}/make-family`;
    star.classList.toggle('fas')
    star.classList.toggle('far')
    fetch(url, {
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
})
}

