const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");
const keyword = document.getElementById("just-for-keyword").innerText;
const filterProperty = {
    keyword : [],
    relation : [],
    tag : []
}

if (keyword){
    filterProperty.keyword.push(keyword);
    console.log("키워드는 : ", keyword );
} else {
    filterProperty.keyword = [];
}

function fetchContent() {
    fetch('/explore-filter',).
    then((res) => res.json()).
    then((res) => {
        let filtered_content = [];
        for (let relation of filterProperty.relation){
            filtered_content.push(res.filter((value) => value.relation_select === relation));
        }
        console.log(filtered_content);
    })
}


function toggleTags(value) {
    const keywordSort = document.getElementsByClassName(value)
    console.log("키워드로 솎은 값: ",keywordSort);
    console.log("태그 값은 :", value)

    for (var i = 0; i < keywordSort.length ;i ++){
        (function (x) {
            const classes = keywordSort[i].classList;
            classes.toggle("display");
        })(i);
    }
}

function checkEventRelation() {
    for (var i = 0; i < relationshipTag.length ; i ++){
        // IIFE (Immediate Invoked Function Expression 이용)
        (function (x) {
            relationshipTag[x].addEventListener("click", (event) =>{
                if (event.target.checked) {
                    filterProperty.relation.push(event.target.value);
                }
                else {
                    filterProperty.relation = filterProperty.relation.filter((value) => {
                        return value != event.target.value;
                    })
                }
                fetchContent();

                console.log(filterProperty.relation);
            })
        })(i);
    }
}

function checkEventTag() {
}

function lengthCheck(){
    
}


function init(){
    checkEventRelation();
    
}


init();