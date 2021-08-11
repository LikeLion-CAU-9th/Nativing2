const likeBtn = document.getElementById("likes-button");
const likeImg = document.getElementById("likes-img");
const likeCnt = document.getElementById('likes-count');
const contentLikeId = likeBtn.value
const likeData = JSON.stringify({
    content_like_id : contentLikeId
})

function likeHandler(event) {
    event.preventDefault();
    let csrftoken = getCookie('csrftoken');
    fetch("../../social-likes", {
        method : "POST",
        body : likeData,
        headers : {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    })
    .then((res) => res.json())
    .then((res) => {
        const isLiked = res['is_liked'];
        const likesCount = res['likes_count']
        if (isLiked) {
            likeImg.src = `../../static/img/redheart.png`
        } else {
            likeImg.src = `../../static/img/heart.png`
        }
        likeCnt.innerText = likesCount
    })
    .catch((err) => console.log(err));
}

console.log("씨발")

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