async function isCorrect(pass) {
    const response = await fetch(`/admin/correct/${encodeURIComponent(pass)}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'no-cors'
    });
    return response.json();
}

async function sumbit(){
    let pass = document.getElementById("pass").value;
    let correct = await isCorrect(pass);
    if (correct == true){
        console.log("CORRECT!");
    } else {
        console.log("NOT CORRECT!");
    }
}