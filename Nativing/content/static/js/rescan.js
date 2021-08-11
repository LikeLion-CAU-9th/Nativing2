const reScanForm = document.getElementById("re-scan-form");
const reScan = document.getElementById("re-scan");
const reScanDiv = document.getElementById("re-scan-keywords");

let reScanList = [];

function setLocalStorageRescan(){
    localStorage.setItem("reScanList", reScanList);
}

function printKeywords(word) {
    const keywordBox = document.createElement("div");
    const keywordSelf = document.createElement("span");
    const keywordDel = document.createElement("div");
    
    keywordBox.classList.add("keyword-box");
    keywordSelf.classList.add("keyword-self");
    keywordDel.classList.add("keyword-del");

    keywordDel.value = word;
    keywordDel.addEventListener("click", delEvent);

    keywordSelf.innerText = word;
    keywordDel.innerText = "❌";

    keywordBox.append(keywordSelf, keywordDel);
    reScanDiv.appendChild(keywordBox);
}

function delEvent(event) {
    const delWord = event.target.value;
    const delButton = event.target;
    const keywordBox = delButton.parentNode;

    reScanDiv.removeChild(keywordBox);

    reScanList = reScanList.filter((value) => {
        return value !== delWord;
    })

    setLocalStorageRescan();
    fetchContent();
    console.log(reScanList);
}


function rescanEvent(event){
    event.preventDefault();
    if (!reScanList.includes(reScan.value)){
        reScanList.push(reScan.value);
        printKeywords(reScan.value);
        console.log(reScanList);

    } else{
        alert("이미 검색한 검색어입니다.")
    }
    reScan.value = "";

    setLocalStorageRescan();
    fetchContent();
}

function init(){
    reScanForm.addEventListener('submit', rescanEvent);
}

init();