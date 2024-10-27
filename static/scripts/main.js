
let IPIPaddr = "192.168.1.158";

console.log("mini tree online");
async function sendData(cmd) {
    const data = { cmd: cmd };

    const response = await fetch('http://${IPaddr}:8080/ctrl', {
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

    const response = await fetch('http://${IPaddr}:8080/ctrl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result['status']);
}


