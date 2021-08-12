const commentBtn = document.getElementById("detail__comments");
const keyExpressionBtn = document.getElementById("detail__keyexpression");
const keyExpressionBody = document.getElementsByClassName("detail__contents__description__body")[0];
const commentSection = document.getElementsByClassName("comment__section")[0];
const submitForm = document.getElementById("comment-form");
const submitBody = document.getElementById("comment-body");

const HIDE_CLASS = "display-hide"

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

    submitBody.value = "";
}


function init(){
    commentBtn.addEventListener("click", commentHandler);
    keyExpressionBtn.addEventListener("click", keyExpressionHandler);
    submitForm.addEventListener("submit", submitHandler);
}

init();