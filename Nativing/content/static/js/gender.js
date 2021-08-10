const maleCheck = document.getElementById('male');
const femaleCheck = document.getElementById('female');

let gender = [];

function setLocalStorageGen(){
    localStorage.setItem("gender", gender);
}

function addGenderEvent() {
    maleCheck.addEventListener("click", (event) => {
        if (event.target.checked){
            if (femaleCheck.checked){
                femaleCheck.checked = false;
            }
            gender.push(event.target.value);
            gender = gender.filter((value) => {
                return value !== "female"
            })

        } else {
            gender = gender.filter((value) => {
                return value !== event.target.value;
            })
        }
        setLocalStorageGen();
        fetchContent();
        console.log(gender);
    })

    femaleCheck.addEventListener("click", (event) => {
        if (event.target.checked){
            if (maleCheck.checked){
                maleCheck.checked = false;
            }
            gender.push(event.target.value);
            gender = gender.filter((value) => {
                return value !== "male"
            })
        } else {
            gender = gender.filter((value) => {
                return value !== event.target.value;
            })
        }
        setLocalStorageGen();
        fetchContent();
        console.log(gender); 
    })
}


function init() {
    addGenderEvent();
}

init();