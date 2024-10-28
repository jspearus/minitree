


const freq = document.getElementById('freq');

const startDate = document.getElementById('start-block');
const stopDate = document.getElementById('stop-block');
const week = document.getElementById('week-block');

document.getElementById('freq').addEventListener('change', function () {
    let selectedValue = this.value;
    if (selectedValue == 'once') {
        week.style.display = 'none';
        startDate.style.display = 'block';
        stopDate.style.display = 'none';
    }
    else if (selectedValue == 'day') {
        week.style.display = 'none';
        startDate.style.display = 'none';
        stopDate.style.display = 'none';
    }
    else if (selectedValue == 'week') {
        week.style.display = 'block';
        startDate.style.display = 'none';
        stopDate.style.display = 'none';
    }
    else if (selectedValue == 'range') {
        week.style.display = 'block';
        startDate.style.display = 'block';
        stopDate.style.display = 'block';
    }
});

async function submitForm() {
    const form = document.getElementById('eventForm');
    event.preventDefault();
    const formData = new FormData(form);
    const formDataObj = {};
    console.log(formData)
    // Convert FormData to a JSON object
    formData.forEach((value, key) => {
        formDataObj[key] = value;
    });
    formDataObj['status'] = 'new';
    // todo add status key
    const jsonData = JSON.stringify(formDataObj);
    console.log(jsonData)
    const response = await fetch('http://' + IPaddr + ':' + PORTvar + '/events', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });
}