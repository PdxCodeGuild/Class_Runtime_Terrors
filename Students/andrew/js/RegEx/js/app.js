// accept username, display on alert
//accept password, check if password 1 and 2 match
//reject invalid characters
//signup page complete if all criteria matches



submit.addEventListener('click', () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const passwordCheck = document.getElementById('password2').value;
    const submit = document.getElementById('submit');
    const clearForm = document.getElementById('clear');


    usernameLength(username, password, passwordCheck);


});

function usernameLength(username, pw1, pw2) {
    const usernameRegex = /^[a-z]+[a-z0-9]*$/i;
    let result = usernameRegex.test(username);
    console.log("test " + result);

    if (username.length === undefined) {
        alert('no username');
    }
    if (result === false) {
        alert("Username must begain with alphabetic character, a-z or A-Z only and no special characters, !@#$%^&*()")
    }
    console.log(username.length)
    if (username.length < 6) {
        alert('username too short');
    }
    else if (username.length > 12) {
        alert('Username is too long.');
    } else {
        console.log('Username is OK!');
        passwordLength(pw1, pw2);
    }
}

function passwordLength(password, password2) {
    if (password !== password2) {
        alert('Passwords do not match!');
    } else {
        if (password.length === undefined) {
            alert("Please enter a password");
            console.log('no password')
        }
        console.log(password.length)
        if (password.length < 8) {
            alert("Password is too short. Must be at least 8 characters.");
            console.log('password too short');
        }
        else if (password.length > 16) {
            alert("Password is too long. Must be no more than 16 characters.");
            console.log('password is too long.');
        } else {
            console.log('password is OK!')
            specialCharacters(password);
        }
    }

}

function specialCharacters(password) {
    const regexPw = /^[a-z1-9!@#$%^&*()]*$/i;
    let result = regexPw.test(password);

    console.log(result);

    if (result === true) {
        alert("rediercting to next page");

    } else {
        console.log("Error");
    }

}

