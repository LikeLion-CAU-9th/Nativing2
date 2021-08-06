const teenager = document.getElementById('teenager');
const twentyfour = document.getElementById('twentyfour');
const twentynine = document.getElementById('twentynine');
const overthirty = document.getElementById('overthirty');

teenager.value = 19;
twentyfour.value = [[20, 24]];
twentynine.value = [[25, 29]];
overthirty.value = [[30, 99]];

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
    console.log(isArray.length);
}

function init() {
    addAgeEvent();
}

init();