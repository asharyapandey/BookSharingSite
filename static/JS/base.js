const errorText = document.querySelector('#error-alert');
const registerForm = document.querySelector('.register-form');
const loginForm = document.querySelector('.login-form');
let validated = false;
const username = document.querySelector('#inputUsername');
const email = document.querySelector('#inputEmail');
const password = document.querySelector('#inputPassword');
const confirmPassword = document.querySelector('#confirmPassword');


password.addEventListener('keyup', () => {
    if (password.value.length < 8){
        errorText.innerText = "Password Should be 8 Characters long.";
    } else {
        validated = true;
        errorText.innerText = "";
    }
});
confirmPassword.addEventListener('keyup', () => {
    if (confirmPassword.value != password.value) {
        errorText.innerText = "Passwords Don't Match.";
    } else {
        validated = true;
        errorText.innerText = "";
    }
});

registerForm.onsubmit = () => {
    if (validated) {
        const request = new XMLHttpRequest();
        request.open('POST', '/users/register/');
        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));//setting the csrf token for validation

        request.onload = () => {
            const returnData = JSON.parse(request.responseText);
            if (returnData['success']) {
                errorText.removeAttribute('class', 'text-danger');
                errorText.innerText = returnData['data'];
                setTimeout(() => {
                    location.reload();
                }, 3000);
                
            } else {
                errorText.setAttribute('class', 'text-danger');
                errorText.innerText = returnData['data']; 
            } 
        }
    
        const data = new FormData();
        data.append('username', username.value);
        data.append('email', email.value);
        data.append('password', password.value);

        request.send(data);
        return false;
    }
}   

loginForm.onsubmit = () => {
    const username = document.querySelector('#username');
    const password = document.querySelector('#password');
    const errorTextLogin = document.querySelector('#error-alert-login');

    const request = new XMLHttpRequest();
    request.open('POST', '/users/login/');
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));//setting the csrf token for validation

    request.onload = () => {
        const returnData = JSON.parse(request.responseText);
        if (returnData['success']) {
            errorTextLogin.removeAttribute('class', 'text-danger');
            errorTextLogin.innerText = returnData['data'];
            setTimeout(() => {
                location.reload();
            }, 3000);
        } else {
            errorTextLogin.setAttribute('class', 'text-danger');
            errorTextLogin.innerText = returnData['data']; 
        } 
    }

    const data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);

    request.send(data);
    return false;
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

document.querySelector('.signup-toggle').addEventListener('click', () => {
    $('#modalLogin').modal('hide');
    $('#modalSignup').modal('show');
})

