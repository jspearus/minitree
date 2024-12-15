

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
    console.log(IPaddr)
    const response = await fetch('http://' + IPaddr + ':' + PORTvar + '/themes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });
}
