const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");
let keyword = null;
try {
    keyword = document.getElementById("just-for-keyword").innerText;
} catch (e) {
    console.log(e);
};
const filterProperty = {
    keyword : [],
    relation : [],
    tag : []
}

// 검색어가 있으면, 검색어대로 filter + 검색어 filterProperty에 추가
// 없으면 모든 모델 가져오고, filterProperty.keyword 초기화
function initialView(){
    fetch('/explore-filter',)
        .then((res) => res.json())
        .then((res) => {
            if (keyword)  {
                console.log("키워드는 :", keyword);
                console.log("됐음");
                filterProperty.keyword.push(keyword);
                let filtered_content = [];
                filtered_content = res.filter((value) => value.title.includes(keyword))
                console.log(filtered_content);
                printContent(filtered_content);
  
            } else {
                console.log("안됐음");
                filterProperty.keyword = [];
                printContent(res);
            }
        })
}



function fetchContent() {
    fetch('/explore-filter',)
        .then((res) => res.json())
        .then((res) => {
            console.log(res);
            let filtered_content = [];
            // relation tag에 해당하는 글
            for (let relationIter of filterProperty.relation){
                // console.log(relation);
                // filter() 가 Array로 return 하므로 다시 한번 for문으로 추가해줌,,
                let filteredArray = res.filter((value) => value.relation_select === relationIter);
                for (let arrayComponent of filteredArray) {
                    filtered_content.push(arrayComponent);
                }
            }
            // keyword search에 해당하는 글
            for (let keywordIter of filterProperty.keyword) {
                let filteredArray = res.filter((value) => value.title.includes(keywordIter))
                for (let arrayComponent of filteredArray) {
                    if (!filtered_content.includes(arrayComponent)){
                        filtered_content.push(arrayComponent);
                    }
                }
            }
            // 일반 상황 tag에 해당하는 글
            for (let tagIter of filterProperty.tag) {
            }

            return filtered_content

        })
        .then((res) => {
            console.log("체크된 컨텐츠", res)
            clearChildNode();
            printContent(res)
        })
}

// filter한 결과를 html에 print해주는
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
        contentBody.innerHTML = 
            `${value[i].expression} <span>is ${value[i].expression_descript_select}</span> of ${value[i].expression_descript}`

        contentBox.append(contentTitle, contentRelation, contentBody);
        
        mainSection.appendChild(contentBox);
    }
}

// tag 바뀔 때마다 앞부분 지워주기 
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

// checklist에 eventlistner 추가
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
    initialView();
    checkEventRelation();
}


init();