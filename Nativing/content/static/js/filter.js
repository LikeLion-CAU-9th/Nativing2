const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");

// console.log(searchResults.value)

function toggleTags(value) {
    const keywordSort = document.getElementsByClassName(value)
    console.log(keywordSort);

    for (var i = 0; i < keywordSort.length ;i ++){
        (function (x) {
            const classes = keywordSort[i].classList;
            classes.toggle("display");
        })(i);
    }
}


function init(){
    for (var i = 0; i < relationshipTag.length ; i ++){
        // console.log(relationshipTag[i].value);
        // IIFE (Immediate Invoked Function Expression 이용)
        (function (x) {
            relationshipTag[x].addEventListener("click", () =>{
                // console.log(relationshipTag[x].value);
                let value = relationshipTag[x].value;
                console.log(value);
                toggleTags(value);  
            })
        })(i);
    }
    console.log("aaa")
}
init();