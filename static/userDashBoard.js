// import db from __init__
/*var morningMed = document.getElementById("morningMed");
var noonMed = document.getElementById("noonMed");
var nightMed = document.getElementById("nightMed");
var qry = sql.query("select * from medication");*/
var table = document.getElementById("medlist");
var deleteBtn = document.getElementByID('delete');

document.onload = function () {
    var rowLength = table.rows.length;
    if (i < rowLength) {
        // clones delete button in order to give it a different name (+i), so that we know which entry to delete later
        var clone = deleteBtn.cloneNode(true);
        clone.querySelector("#delete > .control > input").name += i;

        // tandi use this to go through the table and get the name value of any specified row
        //gets rows of table
        var rowLength = table.rows.length;
        //loops through rows
        for (i = 0; i < rowLength; i++) {
            //gets cells of current row
            var oCells = table.rows.item(i).cells;
            //gets amount of cells of current row
            var cellLength = oCells.length;
            //loops through each cell in current row
            var name = oCells.item(2) // name value of selected row
        }
        i++;
        table.appendChild(clone);

    }
}


// {
//   {
//     current_user.medication_name;
//     current_user.medication_time;
//   }
// }
// var nodeMove = document.createElement("LI");
// nodeMove.innerHTML = "<p>CONTENTS</p>";
// morningMed.appendChild(nodeMove);

/*
const sql = 'SELECT * FROM medication'
db.all(sql,[],(err,rows)=>{
    rows.forEach((row)=>{console.log(row)});
*/


//gets table

















/*

var request = new XMLHttpRequest();
    request.open('POST', '/', true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.onreadystatechange = function () {
        var data = 1;
    }

        var oTable = document.getElementById('medlist');
        var deleteBtn = document.getElementByID('');

        //gets rows of table
        var rowLength = oTable.rows.length;

        //loops through rows
        for (i = 0; i < rowLength; i++) {

            //gets cells of current row
            var oCells = oTable.rows.item(i).cells;

            //gets amount of cells of current row
            var cellLength = oCells.length;

            //loops through each cell in current row
            var name = oCells.item(2)

            for (var j = 0; j < cellLength; j++) {

                // get your cell info here

                var cellVal = oCells.item(j).innerHTML;
                alert(cellVal);
            }
        }
        ;
        request.send('longitude=' + longitude);*/


// window.onload = function(){
//     var Morning = new Date();
//     Morning.setHours(6,0,0,0);

//     var Noon = new Date();
//     Noon.setHours(12,0,0,0);

//     var Night = new Date();
//     Night.setHours(18,0,0,0);

//     var today = new Date();
//     var time = today.getHours();
//     if(time > Morning && time < Noon){ 
//         alert("Morning");
//     }
//     else if(time > Noon && time < Night){
//         alert("Noon");
//     }
//     else if(time > Night && time < Morning){
//         alert("Night");
//     }
// }
