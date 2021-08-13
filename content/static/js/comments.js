const commentBtn = document.getElementById("detail__comments");
const keyExpressionBtn = document.getElementById("detail__keyexpression");
const keyExpressionBody = document.getElementsByClassName("detail__contents__description__body")[0];
const commentSection = document.getElementsByClassName("comment__section")[0];
const submitForm = document.getElementById("comment-form");
const submitBody = document.getElementById("comment-body");
const commentCnt = document.getElementById("comments_count");

const HIDE_CLASS = "display-hide"

console.log(commentBtn.value);

function commentHandler(event){
    keyExpressionBody.classList.add(HIDE_CLASS);
    commentSection.classList.remove(HIDE_CLASS);
}

function keyExpressionHandler(event) {
    keyExpressionBody.classList.remove(HIDE_CLASS);
    commentSection.classList.add(HIDE_CLASS);
}

function submitHandler(event) {
    event.preventDefault();
    const commentValue = submitBody.value;
    const commentData = JSON.stringify({
        content_id : commentBtn.value,
        comment_body : commentValue,
    })

    const csrftoken = getCookie('csrftoken');
    fetch("../detail-comment", {
        method : "POST",
        body : commentData,
        headers : {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    })
    .then((res) => res.json())
    .then((res) => {
        console.log(res);
        console.log(res.comment_writer);
        printComments(res);
        commentCnt.innerHTML = Number(commentCnt.innerHTML) + 1;
    })
    .catch((err) => console.log(err));

    submitBody.value = "";
}


function printComments(comments){
    let comment_iters = document.getElementById("comment_iters");
    let comment_self = document.createElement('div')
    comment_self.classList.add("comment__self");
    comment_self.innerHTML = `
    <div class = "comment__writer">
        ${comments.comment_writer}
    </div>
    <div class = "comment__body">
        ${comments.comment_body}
    </div>
    `
    comment_iters.append(comment_self);
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
    commentBtn.addEventListener("click", commentHandler);
    keyExpressionBtn.addEventListener("click", keyExpressionHandler);
    submitForm.addEventListener("submit", submitHandler);
}

init();