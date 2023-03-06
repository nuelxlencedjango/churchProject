    
let offbgpic = document.getElementById('offering');    
let navLinks = document.getElementById('toggleNav');
let displaySensor = false;

let openFunction = function(){
    
if(displaySensor ===false){
    navLinks.style.display ="block";
    offbgpic.style.transition =".5s easy-in-out";
    offbgpic.style.height ="0px";
    displaySensor =true;


}
else{
    navLinks.style.display ="none";
    offbgpic.style.transition =".5s easy-in-out";
    offbgpic.style.height ="500px";

    displaySensor =false;
}
   }