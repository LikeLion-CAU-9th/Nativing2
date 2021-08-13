// 새로고침시 남아있던 localStorage clear
localStorage.clear();

const relationshipTag = document.getElementsByClassName("relationship-check")
const searchResults = document.getElementsByClassName("content-box");
const loadMoreBtn = document.getElementById("load-more-content");
var loadCount = 1;

// loadmore 할때 몇개 씩 보여줄지
const LOADMORE_NUM = 4;

try {
    let keyword = document.getElementById("just-for-keyword").innerText;
    localStorage.setItem("keyword", keyword);
} catch (e) {
    console.log(e);
};


// 검색어가 있으면, 검색어대로 filter + 검색어 filterProperty에 추가
// 없으면 모든 모델 가져오고, filterProperty.keyword 초기화
function initialView(){
    fetch('../explore-filter', {
        headers : {
            "Accept" : "application/json"
        }
        })
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
    fetch('../explore-filter',)
        .then((res) => res.json())
        .then((res) => {
            let filtered_content = res;

            let tempKeyword = localStorage.getItem("keyword");
            let tempRescan = localStorage.getItem("reScanList");
            const tempRelation = localStorage.getItem("relation");
            let tempHashtag = localStorage.getItem('hashtag');
            let tempGender = localStorage.getItem('gender');
            let tempAge = localStorage.getItem('age');

            if (tempKeyword) {
                filtered_content = filtered_content.filter((value) => value.title.includes(tempKeyword));
                console.log(tempKeyword);
            }
            if (tempGender) {
                filtered_content = filtered_content.filter((value) => (value.user_gender === tempGender))
            }
            if (tempRelation) {
                filtered_content = filtered_content.filter((value) => tempRelation.includes(value.relation_select));
            }
            if (tempRescan) {
                tempRescan = tempRescan.split(",");
                for (var i = 0; i < tempRescan.length; i ++){
                    filtered_content = filtered_content.filter((value) => value.title.includes(tempRescan[i]));
                }
            }
            if (tempAge) {
                console.log(tempAge, typeof(tempAge))
                tempAge = tempAge.split(",");
                console.log(tempAge, typeof(tempAge))
                filtered_content = filtered_content.filter((value) => tempAge.includes(String(value.user_age)));
            }
            if (tempHashtag) {
                tempHashtag = tempHashtag.split(",");
                for (var i = 0; i < tempHashtag.length ; i ++) {
                    filtered_content = filtered_content.filter((value) => value.tag.includes(tempHashtag[i]));
                }
            }

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
    keywordPlace.innerHTML = `Keyword: <span class="nativing-orange">${value}</span>`;
}


function printCount(result) {
    const keywordCount = document.getElementById("content-list__result");
    const countSelf = result.length;

    if (countSelf === 0) {
        keywordCount.innerHTML = "Nothing matches your condition. Try again."
    } else if (countSelf === 1) {
        keywordCount.innerHTML = `<span class="nativing-orange">${countSelf}</span> content meets your condition.`
    } else {
        keywordCount.innerHTML = `<span class="nativing-orange">${countSelf}</span> contents meet your condition.`
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
    let mainSection = document.querySelector('.content-list__content-box__grid');

    const biggerInt = HowMuchToLoadMore(value.length, count);

    for (var i = 0; i < biggerInt; i ++){
        const contentBox = document.createElement('a');
        contentBox.href = `../explore/${value[i].id}`;
        contentBox.className = "content-link"
        contentBox.innerHTML = `
        <div class="content">
            <div class="content__expression"> 
                "${value[i].title}" 
            </div> 
            <div class="content__title">
                ${value[i].expression} 
            </div> 
            <ul class="content__tags"> 
                <li class="tag tag--relation">${value[i].relation_select}</li>
            </ul> 
            <div class="content__author"> 
                <div class="content__author__left"> 
                    <img src="${value[i].user_image_url}" class="content__author__left__image"> 
                </div> 
                <div class="content__author__right"> 
                    <div class="content__author__right__name"> ${value[i].user_name} </div> 
                    <div class="content__author__right__detail"> 
                    </div> 
                </div> 
            </div>
        </div>
        `
        const tagList = contentBox.querySelector('ul')
        value[i].tag.forEach(tagName => {
            const tag = document.createElement('li');
            tag.classList.add('tag');
            tag.innerHTML = tagName
            tagList.appendChild(tag);
        });
        const authorDetail = contentBox.querySelector('.content__author__right__detail')
        genderSpan = document.createElement('span');
        if (value[i].user_gender === "male") {
            genderSpan.classList.add('skyblue')
            genderSpan.innerHTML = "male "   
        } else {
            genderSpan.classList.add('pink')
            genderSpan.innerHTML = "female "   
        }
        ageSpan = document.createElement('span');
        ageSpan.innerHTML = String(value[i].user_age)
        authorDetail.appendChild(genderSpan);
        authorDetail.appendChild(ageSpan);
        mainSection.appendChild(contentBox);
    }
}


// tag 바뀔 때마다 앞부분 지워주기 
function clearChildNode() {
    var cell = document.querySelector('.content-list__content-box__grid');
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