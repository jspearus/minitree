console.log("Hello World! I Don't Give a Bug");
async function sendData(cmd) {
    const data = { cmd: cmd };

    const response = await fetch('http://192.168.1.177:8080/ctrl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result['status']);
}