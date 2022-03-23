
//med form
var medAdd = document.getElementById("medAdd");
medAdd.onclick = function () {
  var medForm = document.getElementById("medication_page");

  var medContainer = document.getElementById("med_container");
  var clone = medContainer.cloneNode(true);
  medForm.appendChild(clone);
};
