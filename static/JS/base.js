const errorText = document.querySelector('#error-alert');
const registerForm = document.querySelector('.register-form');
let validated = false;
    

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
        const username = document.querySelector('#inputUsername').value;
        const email = document.querySelector('#inputEmail').value;
        const password = document.querySelector('#inputPassword').value;
        const request = new XMLHttpRequest();
        request.open('POST', '/users/register/');
        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));//setting the csrf token for validation

        request.onload = () => {
            const returnData = JSON.parse(request.responseText);
            errorText.innerText = returnData['data'];
        }
        
        const data = new FormData();
        data.append('username', username);
        data.append('email', email);
        data.append('password', password);

        request.send(data);
        return false;
    }
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
