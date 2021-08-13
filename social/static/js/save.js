const saveBtn = document.getElementById("save-button");
const contentId= saveBtn.value
const data = JSON.stringify({
    content_id : contentId
});

function signinAlert () {
    alert("Sign in first");
};


function saveHandler(event) {
    event.preventDefault();
    let csrftoken = getCookie('csrftoken');
    console.log("content_id : ", contentId)
    fetch('../../detail-save/', {
        method : "POST",
        body: data,
        headers : {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    })
    .then((res) => res.json())
    .then((res) => {
        let isSaved = res['is_saved']
        if (isSaved) {
            console.log("저장된 상태")
            saveBtn.innerText = "SAVED";
            saveBtn.classList.remove("button--orange");
            saveBtn.classList.add("saved");
        } else {
            console.log("저장 ㄴㄴ ")
            saveBtn.innerText = "SAVE";
            saveBtn.classList.add("button--orange");
            saveBtn.classList.remove("saved");
        }
    })
    .catch((err) => console.log(err));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function init(){
    saveBtn.addEventListener("click", saveHandler);
}

init();