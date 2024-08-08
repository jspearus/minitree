
// Theme creator code
const colorInput1 = document.getElementById('color1');
const colorInput2 = document.getElementById('color2');
const colorInput3 = document.getElementById('color3');

const colorLabel1 = document.getElementById('label1')
const colorLabel2 = document.getElementById('label2')
const colorLabel3 = document.getElementById('label3')

const numLED = document.getElementById('numLEDS')


document.getElementById('pattern').addEventListener('change', function () {
    let selectedValue = this.value;
    if (selectedValue == 'solid') {
        numLED.style.display = 'none';
        colorInput1.style.display = 'block';
        colorLabel1.style.display = 'block';

        colorInput2.style.display = 'none';
        colorLabel2.style.display = 'none'

        colorInput3.style.display = 'none';
        colorLabel3.style.display = 'none'
    }
    else if (selectedValue == '2Color') {
        numLED.style.display = 'block';
        colorInput1.style.display = 'block';
        colorLabel1.style.display = 'block';

        colorInput2.style.display = 'block';
        colorLabel2.style.display = 'block';

        colorInput3.style.display = 'none';
        colorLabel3.style.display = 'none';
    }
    else if (selectedValue == '3Color') {
        numLED.style.display = 'block';
        colorInput1.style.display = 'block';
        colorLabel1.style.display = 'block';

        colorInput2.style.display = 'block';
        colorLabel2.style.display = 'block';

        colorInput3.style.display = 'block';
        colorLabel3.style.display = 'block'
    }
});
async function submitForm() {
    const form = document.getElementById('themeForm');
    event.preventDefault();
    const formData = new FormData(form);
    const formDataObj = {};

    // Convert FormData to a JSON object
    formData.forEach((value, key) => {
        formDataObj[key] = value;
    });
    const jsonData = JSON.stringify(formDataObj);
    console.log(jsonData)
    const response = await fetch('http://192.168.1.177:8080/themes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });
}