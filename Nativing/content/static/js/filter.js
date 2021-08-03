const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");
const keyword = document.getElementById("just-for-keyword").innerText;
const filterProperty = {
    keyword : [],
    relation : [],
    tag : []
}

filterProperty.keyword.push('ne')
console.log(filterProperty);

if (keyword){
    console.log("키워드는 : ", keyword )
} else {
    console.log("키워드 없음")
}


// console.log(searchResults.value)
fetch('/explore-filter',).
    then((res) => res.json()).
    then((res) => {
        let filtered_content;
        filtered_content = res.filter(value => value.id === 1 || value.id === 2);
        console.log(filtered_content);
    })
// console.log(abc)

function addEvent(){
    console.log("sed")
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

function formin(x) {
    relationshipTag[x].addEventListener("click", (event) =>{
        if (event.target.checked) {
            filterProperty.relation.push(event.target.value);
        }
        else {
            filterProperty.relation = filterProperty.relation.filter((value) => {
                return value != event.target.value;
            })
        }
        console.log(filterProperty.relation);
        // toggleTags(value);  
    })
}

function lengthCheck(){
    
}


function init(){
    for (var i = 0; i < relationshipTag.length ; i ++){
        // console.log(relationshipTag[i].value);
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
                console.log(filterProperty.relation);
                // toggleTags(value);  
            })
        })(i);
    }
    console.log("aaa")
}
init();