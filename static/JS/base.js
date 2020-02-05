const username = document.querySelector('#username');
const email = document.querySelector('#email');
const password = document.querySelector('#password');
const confirmPassword = document.querySelector('#confirmPassword');
const registerForm = document.querySelector('.register-form');
const errorText = document.querySelectorAll('.error');
let username_validate = false;
let password_validate = false;
let confirmPassword_validate = false;
username.addEventListener('keyup', () => {
    if (username.value.length < 5){
        errorText[0].innerText = "**Username Should be 5 Characters long.";
    } else if (password.value == '') {
        errorText[0].innerText = "";
    } else {
        username_validate = true;
        errorText[0].innerText = "";
    }
});
password.addEventListener('keyup', () => {
    if (password.value.length < 8){
        errorText[2].innerText = "**Password Should be 8 Characters long.";
    } else if (password.value == '') {
        errorText[2].innerText = "";
    } else {
        password_validate = true;
        errorText[2].innerText = "";
    }
});
confirmPassword.addEventListener('keyup', () => {
    if (confirmPassword.value != password.value) {
        errorText[3].innerText = "Passwords Don't Match.";
    } else if (confirmPassword.value == '') {
        errorText[3].innerText = "";
    } else {
        confirmPassword_validate = true;
        errorText[3].innerText = "";
    }
});

registerForm.addEventListener('submit', (e) => {
    if (username.value.length < 5 || password.value.length < 8 || confirmPassword.value != password.value) {
        e.preventDefault();
    }
})


function acceptClick(event) {
    const request = new XMLHttpRequest();
    request.open('POST', window.location.href);
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    const data = new FormData();
    data.append('is_accepted', 'True');
    data.append('request_id', event.value);
    request.send(data);
    return false;
}

function filterNonFictionClick() {
    const request = new XMLHttpRequest();
    request.open('POST', 'books/search/');
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    const data = new FormData();
    data.append('search', 'E');
    request.send(data);
    return false;
}

function rejectClick(event) {
    //alert("The URL of this page is: " + window.location.href);
    const request = new XMLHttpRequest();
    request.open('POST', window.location.href);
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    const data = new FormData();
    data.append('is_accepted', 'False');
    data.append('request_id', event.value);
    request.send(data);
    return false;
}

// wat.forEach(element => {
//     element.setAttribute('class', 'form-label-group')
// });
// registerForm.onsubmit = () => {
//     if (validated) {
//         const request = new XMLHttpRequest();
//         request.open('POST', '/users/register/');
//         request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));//setting the csrf token for validation

//         request.onload = () => {
//             const returnData = JSON.parse(request.responseText);
//             if (returnData['success']) {
//                 errorText.removeAttribute('class', 'text-danger');
//                 errorText.innerText = returnData['data'];
//                 setTimeout(() => {
//                     location.reload();
//                 }, 3000);
                
//             } else {
//                 errorText.setAttribute('class', 'text-danger');
//                 errorText.innerText = returnData['data']; 
//             } 
//         }
    
//         const data = new FormData();
//         data.append('username', username.value);
//         data.append('email', email.value);
//         data.append('password', password.value);

//         request.send(data);
//         return false;
//     }
// }   

// loginForm.onsubmit = () => {
//     const username = document.querySelector('#username');
//     const password = document.querySelector('#password');
//     const errorTextLogin = document.querySelector('#error-alert-login');

//     const request = new XMLHttpRequest();
//     request.open('POST', '/users/login/');
//     request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));//setting the csrf token for validation

//     request.onload = () => {
//         const returnData = JSON.parse(request.responseText);
//         if (returnData['success']) {
//             errorTextLogin.removeAttribute('class', 'text-danger');
//             errorTextLogin.innerText = returnData['data'];
//             setTimeout(() => {
//                 location.reload();
//             }, 3000);
//         } else {
//             errorTextLogin.setAttribute('class', 'text-danger');
//             errorTextLogin.innerText = returnData['data']; 
//         } 
//     }

//     const data = new FormData();
//     data.append('username', username.value);
//     data.append('password', password.value);

//     request.send(data);
//     return false;
// }

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


