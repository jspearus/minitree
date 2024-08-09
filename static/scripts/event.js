


const freq = document.getElementById('freq');

const date = document.getElementById('event-date');
const datelabel = document.getElementById('date-label');

const week = document.getElementById('weekday');
const weeklabel = document.getElementById('week-label');

document.getElementById('freq').addEventListener('change', function () {
    let selectedValue = this.value;
    if (selectedValue == 'once') {
        week.style.display = 'none';
        weeklabel.style.display = 'none';
        date.style.display = 'block';
        datelabel.style.display = 'block';
    }
    else if (selectedValue == 'day') {
        week.style.display = 'none';
        weeklabel.style.display = 'none';
        date.style.display = 'none';
        datelabel.style.display = 'none';
    }
    else if (selectedValue == 'week') {
        week.style.display = 'block';
        weeklabel.style.display = 'block';
        date.style.display = 'none';
        datelabel.style.display = 'none';
    }
});

async function submitForm() {
    const form = document.getElementById('eventForm');
    event.preventDefault();
    const formData = new FormData(form);
    const formDataObj = {};

    // Convert FormData to a JSON object
    formData.forEach((value, key) => {
        formDataObj[key] = value;
    });
    const jsonData = JSON.stringify(formDataObj);
    console.log(jsonData)
    const response = await fetch('http://192.168.1.177:8080/events', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    });
}