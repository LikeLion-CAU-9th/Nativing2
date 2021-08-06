const relationshipCheck = document.getElementsByClassName("relationship-check")

let relation = [];

function setLocalStorageRel() {
    localStorage.setItem("relation", relation);
}

function checkEventRelation() {
    for (var i = 0; i < relationshipCheck.length ; i ++){
        // IIFE (Immediate Invoked Function Expression 이용)
        (function (x) {
            relationshipCheck[x].addEventListener("click", (event) =>{
                if (event.target.checked) {
                    relation.push(event.target.value);
                }
                else {
                    relation = relation.filter((value) => {
                        return value !== event.target.value;
                    })
                }
                
                setLocalStorageRel();
                console.log("체크된 relation: ", relation);
                fetchContent();
            })
        })(i);
    }
}


function init(){
    checkEventRelation();
}

init()