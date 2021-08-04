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
    fetch('/explore-filter',)
        .then((res) => res.json())
        .then((res) => {
            console.log(res);
            let filtered_content = [];
            for (let relation of filterProperty.relation){
                // console.log(relation);
                let filteredArray = res.filter((value) => value.relation_select === relation);
                for (arrayComponent of filteredArray) {
                    filtered_content.push(arrayComponent);
                }
            }
            console.log("체크된 컨텐츠", filtered_content)
            clearChildNode();
            printContent(filtered_content)
        })
}

function printContent(value) {
    let mainSection = document.querySelector('.main-sections');
    for (var i = 0; i < value.length; i ++){
        let contentBox = document.createElement('div');
        let contentTitle = document.createElement('div');    
        let contentRelation = document.createElement('div');    
        let contentBody = document.createElement('div');
        
        contentBox.classList.add('content-box');
        contentTitle.classList.add('content-title');
        contentRelation.classList.add('content-relation');
        contentBody.classList.add('content-body');

        contentTitle.innerHTML = value[i].title;
        contentRelation.innerHTML = value[i].relation_select;
        contentBody.innerHTML = i, "번째 글"

        contentBox.append(contentTitle, contentRelation, contentBody);
        
        mainSection.appendChild(contentBox);
    }
}

function clearChildNode() {
    var cell = document.querySelector('.main-sections');
    while (cell.hasChildNodes()){
        cell.removeChild( cell.firstChild );
    }
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
                // fetchContent();

                console.log("체크된 relation: ", filterProperty.relation);
                fetchContent();
            })
        })(i);
    }
}

function init(){
    checkEventRelation();
    // fetchContent();
}


init();