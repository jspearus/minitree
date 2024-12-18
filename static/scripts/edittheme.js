

// async function submitForm() {
//     const form = document.getElementById('themeForm');
//     event.preventDefault();
//     const formData = new FormData(form);
//     const formDataObj = {};

//     // Convert FormData to a JSON object
//     formData.forEach((value, key) => {
//         formDataObj[key] = value;
//     });
//     const jsonData = JSON.stringify(formDataObj);
//     console.log(jsonData)
//     console.log(formDataObj.name)
//     try {
//         const response = await fetch('http://' + IPaddr + ':' + PORTvar + '/edittheme/' + formDataObj.name, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(jsonData)
//         });
//         console.error('test:', response);
//         const responseData = await response.json(); // Parse JSON response
//         console.error('Error:', responseData);
//         if (responseData.redirect) {
//             window.location.href = responseData.redirect; // Redirect to the provided URL
//         }
//     } catch (error) {
//         console.error('Error:', error);
//     }
// }


