const likeBtn = document.getElementById("likes-button");
const contentLikeId = likeBtn.value
const likeData = JSON.stringify({
    content_like_id : contentLikeId
})

function likeHandler(event) {
    event.preventDefault();
    let csrftoken = getCookie('csrftoken');
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
    likeBtn.addEventListener("click", likeHandler);
}

init();