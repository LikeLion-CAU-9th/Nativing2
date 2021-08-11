// 새로고침시 남아있던 localStorage clear
localStorage.clear();

const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");
const loadMoreBtn = document.getElementById("load-more-content");
var loadCount = 1;

// loadmore 할때 몇개 씩 보여줄지
const LOADMORE_NUM = 3;

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
                printKeyword(keyword);
                printContent(filtered_content, loadCount);
                printCount(filtered_content);
  
            } else {
                console.log("안됐음");
                printContent(res, loadCount);
                printCount(res);
            }
        })
}


function fetchContent(isLoadMore = false) {
    fetch('/explore-filter',)
        .then((res) => res.json())
        .then((res) => {
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
                console.log(tempKeyword);
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
            printCount(res);
            if (isLoadMore) printContent(res, loadCount);
            else {
                loadCount = 1;
                printContent(res, loadCount);
            }
        })
}


function printKeyword(value) {
    const keywordPlace = document.getElementById("keyword-text");
    keywordPlace.innerText = `Keyword : ${value}`;
}


function printCount(result) {
    const keywordCount = document.getElementById("keyword-count");
    const countSelf = result.length;

    if (countSelf === 0) {
        keywordCount.innerHTML = "Nothing matches your condition. Try again."
    } else if (countSelf === 1) {
        keywordCount.innerHTML = `<span>${countSelf}</span> content meets your condition.`
    } else {
        keywordCount.innerHTML = `<span>${countSelf}</span> contents meet your condition.`
    }
}


// filtered content 개수 vs Load more count로 불러오는 개수 중 작은 것 return
//  + 모두 불러오면 loadmore 버튼 안보이도록
function HowMuchToLoadMore(contentNum, loadCnt) {
    const biggerInt = (loadCnt * LOADMORE_NUM > contentNum) ? contentNum : loadCnt * LOADMORE_NUM;
    if (biggerInt === contentNum) {
        loadMoreBtn.classList.add("do-not-show");
    } else {
        loadMoreBtn.classList.remove("do-not-show");
    }
    return biggerInt
}


// filter한 결과를 html에 print해주는
function printContent(value, count) {
    let mainSection = document.querySelector('.main-sections');

    const biggerInt = HowMuchToLoadMore(value.length, count);

    for (var i = 0; i < biggerInt; i ++){
        let linkDetail = document.createElement('a');
        let contentBox = document.createElement('div');
        let contentTitle = document.createElement('div');    
        let contentRelation = document.createElement('div');    
        let contentBody = document.createElement('div');
        let contentTag = document.createElement('div');
        
        linkDetail.href = `/explore/${value[i].id}`;
        contentBox.classList.add('content-box');
        contentTitle.classList.add('content-title');
        contentRelation.classList.add('content-relation');
        contentBody.classList.add('content-body');
        contentTag.classList.add('content-tag');

        contentTitle.innerHTML = value[i].title;
        contentRelation.innerHTML = value[i].relation_select;
        contentBody.innerHTML = 
            `${value[i].expression} <span>is ${value[i].expression_descript_select}</span> of ${value[i].expression_descript}`
        contentTag.innerHTML = value[i].tag;

        contentBox.append(contentTitle, contentRelation, contentBody, contentTag);
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


function loadMoreHandler(event){
    loadCount += 1;
    console.log(loadCount);
    fetchContent(isLoadMore = true);
}


function init(){
    // loadmore 세주기
    loadMoreBtn.addEventListener("click", loadMoreHandler)
    initialView();
}


init();