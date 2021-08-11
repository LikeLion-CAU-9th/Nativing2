const teenager = document.getElementById('teenager');
const twentyfour = document.getElementById('twentyfour');
const twentynine = document.getElementById('twentynine');
const overthirty = document.getElementById('overthirty');

let teenArray = new Array()
let twentyfourArray = new Array()
let twentynineArray = new Array()
let overthirtyArray = new Array()
for (var i = 0; i < 70 ; i ++ ){
    if (i < 20){
        teenArray.push(i)
    }
    if (i < 5){
        twentyfourArray.push(i + 20)
        twentynineArray.push(i + 25)
    }
    overthirtyArray.push(i + 30)
}

teenager.value = teenArray;
twentyfour.value = twentyfourArray;
twentynine.value = twentynineArray;
overthirty.value = overthirtyArray;

console.log(teenager.value);

console.log("fwefw");
let age = [];

function setLocalStorageAge(){
    localStorage.setItem('age', age);
}

function addAgeEvent() {
    teenager.addEventListener("click", ageEventHandler);
    twentyfour.addEventListener("click", ageEventHandler);
    twentynine.addEventListener("click", ageEventHandler);
    overthirty.addEventListener("click", ageEventHandler);
}

function ageEventHandler(event) {
    const eventValue = event.target.value;
    if (event.target.checked) {
        age.push(eventValue);
    } else{
        age = age.filter((value) => {
            return value !== eventValue;
        })
    }
    setLocalStorageAge();
    const isArray = localStorage.getItem('age');
    console.log(isArray);
    fetchContent();
}

function init() {
    addAgeEvent();
}

init();