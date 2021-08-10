// const genderButtonList = document.querySelectorAll('.form-box__gender-button');
// const genderInput = document.querySelector('#gender-input')

// genderButtonList.forEach(function(genderButton) {
//     genderButton.addEventListener("click", function(event) {
//         event.preventDefault()
//         const targetButton = genderButton
//         const anotherButton = targetButton.id == 'male' ? document.querySelector('#female') : document.querySelector('#male')
//         handleClickeEvent(targetButton, anotherButton)
//     });
// });

// function handleClickeEvent(targetButton, anotherButton) {
//     if (!targetButton.classList.contains('form-box__gender-button--selected') && anotherButton.classList.contains('form-box__gender-button--selected')) {
//         changeButtonColor(anotherButton)
//         setGender(anotherButton)
//     }
//     changeButtonColor(targetButton)
//     setGender(targetButton)
// }

// function changeButtonColor(button) {
//     button.classList.toggle('form-box__gender-button--selected');
// }

// function setGender(button) {
//     if (genderInput.value !== button.id ) {
//         genderInput.value = button.id
//     } else {genderInput.value = ""}
// }
