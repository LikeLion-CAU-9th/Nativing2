const followBtn = document.getElementById("follow-button");
const uploaderId = followBtn.value
const uploaderData = JSON.stringify({
    uploaderId : uploaderId
});


function followHandler(event) {
    event.preventDefault();
    let csrftoken = getCookie('csrftoken');
    fetch('../social-follow/', {
        method: "POST",
        body : uploaderData,
        headers : {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    })
    .then((res) => res.json())
    .then((res) => {
        let is_following = res['is_following']
        if (is_following) {
            followBtn.innerText = "FOLLOWING";
            followBtn.classList.add("following");
        } else {
            followBtn.innerText = "FOLLOW";
            followBtn.classList.remove("following");
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


function init () {
    followBtn.addEventListener("click", followHandler);
}

init();