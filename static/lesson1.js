let currentPart = 1;

function next(){
    currentPart += 1;
    document.getElementById(`part${currentPart - 1}`).style.display = 'none';
    if (document.getElementById(`part${currentPart}`)){
        document.getElementById(`part${currentPart}`).style.display = 'block';
    } else {
        lessonOver();
    }
}

function succes2(){
    document.getElementById(`part${currentPart}`).style.display = 'none';
    document.getElementById("notSucces").style.display = 'none';
    document.getElementById("succes").style.display = 'block';
    document.getElementById("lessonOver").style.display = 'none';
    document.getElementById("lessonOverButton").style.display = 'none';
    setTimeout(succes, 1500);
}

function succes(){
    document.getElementById(`part${currentPart}`).style.display = 'none';
    document.getElementById("notSucces").style.display = 'none';
    document.getElementById("succes").style.display = 'none';
    document.getElementById("lessonOver").style.display = 'none';
    document.getElementById("lessonOverButton").style.display = 'none';
    next();
}

function notSucces(){
    document.getElementById("notSucces").style.display = 'block';
    document.getElementById("succes").style.display = 'none';
     document.getElementById("lessonOver").style.display = 'none';
    document.getElementById("lessonOverButton").style.display = 'none';
}

function lessonOver(){
    document.getElementById("notSucces").style.display = 'none';
    document.getElementById("succes").style.display = 'none';
    document.getElementById("lessonOver").style.display = 'block';
    document.getElementById("lessonOverButton").style.display = 'block';
}

function returnToHome(){
    document.location.href = "/";
}