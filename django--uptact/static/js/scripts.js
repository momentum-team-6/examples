console.log('js loaded')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let star = document.querySelector(".fa-star")
let contactPk = star.parentElement.dataset.contactPk
let URL = `contacts/${contactPk}/make-family`
star.addEventListener('click', e => {
    fetch(URL, {
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        },
    })
    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {
        //Perform actions with the response data from the view
        console.log(data)
        star.classList.toggle('fas')
        star.classList.toggle('far')
    })
    
})