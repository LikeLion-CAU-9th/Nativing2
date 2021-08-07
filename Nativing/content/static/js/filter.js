
// 새로고침시 남아있던 localStorage clear
localStorage.clear();

const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");

try {
    let keyword = document.getElementById("just-for-keyword").innerText;
    localStorage.setItem("keyword", keyword);
} catch (e) {
    console.log(e);
};


// 검색어가 있으면, 검색어대로 filter + 검색어 filterProperty에 추가
// 없으면 모든 모델 가져오고, filterProperty.keyword 초기화
function initialView(){
    fetch('/explore-filter',)
        .then((res) => res.json())
        .then((res) => {
            let keyword = localStorage.getItem("keyword");
            if (keyword)  {
                console.log("키워드는 :", keyword);
                console.log("됐음");

                let filtered_content = res;
                filtered_content = filtered_content.filter((value) => value.title.includes(keyword))
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
            // console.log(res);
            let filtered_content = res;
            // relation tag에 해당하는 글
            // for (let relationIter of filterProperty.relation){
            //     // console.log(relation);
            //     // filter() 가 Array로 return 하므로 다시 한번 for문으로 추가해줌,,
            //     let filteredArray = res.filter((value) => value.relation_select === relationIter);
            //     for (let arrayComponent of filteredArray) {
            //         filtered_content.push(arrayComponent);
            //     }
            // }
            let tempKeyword = localStorage.getItem("keyword");
            let tempRescan = localStorage.getItem("reScanList");
            const tempRelation = localStorage.getItem("relation");
            let tempHashtag = localStorage.getItem('hashtag');
            

            if (tempKeyword) {
                filtered_content = filtered_content.filter((value) => value.title.includes(tempKeyword));
            }
            if (tempRelation) {
                filtered_content = filtered_content.filter((value) => value.relation_select.includes(tempRelation));
            }
            if (tempRescan) {
                tempRescan = tempRescan.split(",");
                for (var i = 0; i < tempRescan.length; i ++){
                    filtered_content = filtered_content.filter((value) => value.title.includes(tempRescan[i]));
                }
            }
            if (tempHashtag) {
                tempHashtag = tempHashtag.split(",");
                for (var i = 0; i < tempHashtag.length ; i ++) {
                    filtered_content = filtered_content.filter((value) => value.tag.includes(tempHashtag[i]));
                }
            }

            // keyword search에 해당하는 글
            // for (let keywordIter of filterProperty.keyword) {
            //     let filteredArray = res.filter((value) => value.title.includes(keywordIter))
            //     for (let arrayComponent of filteredArray) {
            //         if (!filtered_content.includes(arrayComponent)){
            //             filtered_content.push(arrayComponent);
            //         }
            //     }
            // }
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
        let linkDetail = document.createElement('a');
        let contentBox = document.createElement('div');
        let contentTitle = document.createElement('div');    
        let contentRelation = document.createElement('div');    
        let contentBody = document.createElement('div');
        
        linkDetail.href = `/explore/${value[i].id}`;
        contentBox.classList.add('content-box');
        contentTitle.classList.add('content-title');
        contentRelation.classList.add('content-relation');
        contentBody.classList.add('content-body');

        contentTitle.innerHTML = value[i].title;
        contentRelation.innerHTML = value[i].relation_select;
        contentBody.innerHTML = 
            `${value[i].expression} <span>is ${value[i].expression_descript_select}</span> of ${value[i].expression_descript}`

        contentBox.append(contentTitle, contentRelation, contentBody);
        linkDetail.append(contentBox);
        
        mainSection.appendChild(linkDetail);
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

function init(){
    initialView();
}


init();