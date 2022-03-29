//med form
var medAdd = document.getElementById("medAdd");
var i = 2;
medAdd.onclick = function () {
  if (i < 4) {
    var medForm = document.getElementById("medication_page");
    var medContainer = document.getElementById("med_container");
    var clone = medContainer.cloneNode(true);
    clone.querySelector("#medName > .control > input").id += i;
    clone.querySelector("#medType > .control > input").id += i;
    clone.querySelector("#medTime > .control > input").id += i;
    clone.querySelector(
      "#medDose > .control > label > #medication_doseMorning"
    ).id += i;
    clone.querySelector(
      "#medDose > .control > label > #medication_doseNoon"
    ).id += i;
    clone.querySelector(
      "#medDose > .control > label > #medication_doseNight"
    ).id += i;
    i++;
    medForm.appendChild(clone);
  }
};
