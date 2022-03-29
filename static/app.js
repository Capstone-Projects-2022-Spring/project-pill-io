//med form
var medAdd = document.getElementById("medAdd");
var i = 2;
medAdd.onclick = function () {
  if (i < 4) {
    var medForm = document.getElementById("medication_page");
    var medContainer = document.getElementById("med_container");
    var clone = medContainer.cloneNode(true);
    clone.querySelector("#medName > .control > input").name += i;
    clone.querySelector("#medType > .control > input").name += i;
    clone.querySelector("#medDose > .control > input").name += i;
    clone.querySelector(
      "#medTime > .control > label > #medication_timeMorning"
    ).name += i;
    clone.querySelector(
      "#medTime > .control > label > #medication_timeNoon"
    ).name += i;
    clone.querySelector(
      "#medTime > .control > label > #medication_timeNight"
    ).name += i;
    i++;
    medForm.appendChild(clone);
  }
};
