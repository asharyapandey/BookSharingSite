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
    afterAcceptClick(event);
    return false;
}


function rejectClick(event) {
    const request = new XMLHttpRequest();
    request.open('POST', window.location.href);
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    const data = new FormData();
    data.append('is_accepted', 'False');
    data.append('request_id', event.value);
    request.send(data);
    afterRejectClick(event);
    return false;
}
function afterAcceptClick(event) {
    let id = `#requestStatus${event.value}` 
    const requestStatus = document.querySelector(id);
    const btnAccept = document.querySelector(`#btnAccept${event.value}`);
    const btnReject = document.querySelector(`#btnReject${event.value}`);
    requestStatus.innerHTML = '<span class="text-muted">Request Status : </span> Accepted ';
    btnAccept.setAttribute('class', 'd-none');
    btnReject.setAttribute('class', 'd-none');
}
function afterRejectClick(event) {
    let id = `#requestStatus${event.value}` 
    const requestStatus = document.querySelector(id);
    const btnAccept = document.querySelector(`#btnAccept${event.value}` );
    const btnReject = document.querySelector(`#btnReject${event.value}` );
    requestStatus.innerHTML = '<span class="text-danger">Request Status : </span> Rejected ';
    btnReject.setAttribute('class', 'd-none');
}

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


