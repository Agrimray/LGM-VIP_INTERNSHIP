let screen = document.getElementById('screen');
buttons = document.querySelectorAll('button');
let screenValue = '';
let x=0;
for (item of buttons) {
    item.addEventListener('click', (e) => {
        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        if (buttonText == 'X') {
            buttonText = '*';
            screenValue += buttonText;
            screen.value = screenValue;
        }
        else if (buttonText == 'C') {
            screenValue = "";
            screen.value = screenValue;
        }
        else if (buttonText == '=') {
            screen.value = eval(screenValue);
        }
        else if (buttonText == 'sin') {
            screenValue = Math.sin(screen.value * (Math.PI / 180));
            screen.value = screenValue;
        }
        else if (buttonText == 'cos') {
            screenValue = Math.cos(screen.value * (Math.PI / 180));
            screen.value = screenValue;
        }
        else if (buttonText == 'tan') {
            screenValue = Math.tan(screen.value * (Math.PI / 180));
            screen.value = screenValue;
        }
        else if (buttonText == 'sqrt') {
            screenValue = Math.sqrt(screen.value);
            screen.value = screenValue;
        }
        else {
            screenValue += buttonText;
            screen.value = screenValue;
        }

    })
}

