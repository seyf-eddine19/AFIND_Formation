/*-----------------------------------*/
/*------------ MENU SHOW ------------*/
var toggleBtn = document.querySelector("#nav-toggle");
var myMenu = document.querySelector("#nav-menu");

toggleBtn.onclick = function(){
  toggleBtn.classList.toggle('bx-x');
  toggleBtn.classList.toggle('bx-menu');
  myMenu.classList.toggle('show');
}
/*-----------------------------------*/
function submitEnrollForm() {
    var form = document.getElementById("enrollForm");
    if (form.checkValidity()) {
        form.submit();
    } else {
        form.reportValidity();
    }
}