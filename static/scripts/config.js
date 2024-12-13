

async function submitForm() {
    const form = document.getElementById('configForm');
    event.preventDefault();
    const formData = new FormData(form);
    const formDataObj = {};
    console.log(formData)
    // Convert FormData to a JSON object
    formData.forEach((value, key) => {
        formDataObj[key] = value;
    });


    const jsonData = JSON.stringify(formDataObj);
    console.log(jsonData)
    const response = await fetch('http://' + IPaddr + ':' + PORTvar + '/config', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });
}
