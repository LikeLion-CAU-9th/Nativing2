const hashtag = document.getElementsByClassName("tag-iter");
const hashtagCheck = document.getElementsByClassName("tags-check");
const viewMoreBtn = document.getElementById("viewtags-btn");
const HIDE_TAG = "do-not-show";
let hashtagList = [];

function setLocalStorageHashtag(){
    localStorage.setItem('hashtag', hashtagList);
}

function hideTagsInit(){
    for (var i = 5; i < hashtag.length ; i ++ ){
        hashtag[i].classList.add(HIDE_TAG);
    }
}

function showTags() {
    for (var i = 5; i < hashtag.length ; i ++ ){
        hashtag[i].classList.remove(HIDE_TAG);
    }
}

function addEventViewMore(){
    viewMoreBtn.addEventListener("click", (event) => {
        showTags();
        viewMoreBtn.classList.add(HIDE_TAG);
    })
}
function viewMoreHandler(event){
    showTags();

}

function checkEventHashtag() {
    for (var i = 0; i < hashtagCheck.length ; i ++) {
        (function(x) {
            hashtagCheck[x].addEventListener("click", (event) => {
                if (event.target.checked) {
                    hashtagList.push(event.target.value);
                }
                else {
                    hashtagList = hashtagList.filter((value) => {
                        return value !== event.target.value;
                    })
                }
                setLocalStorageHashtag();
                console.log(hashtagList);
                fetchContent();
            })
        })(i);
    }
}

function init(){
    // viewMoreBtn.addEventListener("click", viewMoreHandler);
    addEventViewMore();
    checkEventHashtag();
    hideTagsInit();   
}

init();