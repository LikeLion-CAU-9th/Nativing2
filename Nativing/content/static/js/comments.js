const commentBtn = document.getElementById("detail__comments");
const keyExpressionBtn = document.getElementById("detail__keyexpression");
const keyExpressionBody = document.getElementsByClassName("detail__contents__description__body")[0];
const commentSection = document.getElementsByClassName("comment__section")[0];
const submitForm = document.getElementById("comment-form");
const submitBody = document.getElementById("comment-body");
const commentCnt = document.getElementById("comments_count");
const commentSubmit = document.getElementById("commentSubmit");

const HIDE_CLASS = "display-hide"

console.log(commentBtn.value);

function commentHandler(event){
    keyExpressionBody.classList.add(HIDE_CLASS);
    commentSection.classList.remove(HIDE_CLASS);
    commentBtn.classList.remove('gray');
    keyExpressionBtn.classList.add('gray');
}

function keyExpressionHandler(event) {
    keyExpressionBody.classList.remove(HIDE_CLASS);
    commentSection.classList.add(HIDE_CLASS);
    commentBtn.classList.add('gray');
    keyExpressionBtn.classList.remove('gray');
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
    <div class = "comment__self__image">
    <img src="${userImageURL}" class="content__author__left__image">
</div>
<div class = "comment__body">
    <div class="comment__body__writer">${comments.comment_writer}</div>
    <div class="comment__body__text">${comments.comment_body}</div>
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

submitBody.addEventListener('input', updateValue);
function updateValue(e) {
    if (submitBody && submitBody.value) {
        commentSubmit.disabled = false;
        commentSubmit.classList.remove('disabled');
        commentSubmit.classList.add('button--orange');
    }
    else {
        commentSubmit.disabled = true
        commentSubmit.classList.add('disabled');
        commentSubmit.classList.remove('button--orange');
    }
}


function init(){
    commentBtn.addEventListener("click", commentHandler);
    keyExpressionBtn.addEventListener("click", keyExpressionHandler);
    submitForm.addEventListener("submit", submitHandler);
}

init();