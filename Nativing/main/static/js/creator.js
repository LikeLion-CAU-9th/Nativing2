const createDiv = document.createElement("div")

function createElementWithClass(tag, className, innerText, locationToAppend) {
    const element = document.createElement(tag)
    element.classList.add(className)
    element.innerHTML = innerText
    locationToAppend.appendChild(element)
    return element
}


const contentList = document.getElementsByClassName("content")
for (i = 0; i < contentList.length; i++) {
    content = contentList[i]
    content.innerHTML = '<div class="content__expression"> "나 목욜 약속 있어" </div> <div class="content__title"> 친구와 약속잡기 </div> <ul class="content__tags"> <li class="tag">Friend</li> <li class="tag">Game</li> </ul> <div class="content__author"> <div class="content__author__left"> <img src="../static/img/tarakyu.png" class="content__author__left__image"> </div> <div class="content__author__right"> <div class="content__author__right__name"> 따라큐 </div> <div class="content__author__right__detail"> <span class="nativing-orange">3.4k</span> followers <span class="skyblue"> Male</span> 26 </div> </div> </div>'
}