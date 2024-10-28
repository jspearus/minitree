
const dataContainer = document.getElementById('dataContainer');
const IPaddr = dataContainer.getAttribute('ip_var');
const PORTvar = dataContainer.getAttribute('port_var');
console.log("mini tree online");
async function sendData(cmd) {

    const data = { cmd: cmd };

    const response = await fetch('hhttp://' + IPaddr + ':' + PORTvar + '/ctrl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result['status']);
}
async function getDropdownValue() {
    const dropdown = document.querySelector('#themeSelect');
    const selectedValue = dropdown.value;
    const data = { cmd: selectedValue };

    const response = await fetch('http://' + IPaddr + ':' + PORTvar + '/ctrl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result['status']);
}


