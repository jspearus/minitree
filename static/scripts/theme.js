
// Theme creator code
const colorInput = document.getElementById('color');
const colorDisplay = document.getElementById('colorDisplay');

// Update the color display when the color input changes
colorInput.addEventListener('input', function () {
    colorDisplay.style.backgroundColor = colorInput.value;
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