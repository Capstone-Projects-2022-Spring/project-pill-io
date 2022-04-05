import db from __init__
var morningMed = document.getElementById("morningMed");
var noonMed = document.getElementById("noonMed");
var nightMed = document.getElementById("nightMed");
var qry = sql.query("select * from medication");
// {
//   {
//     current_user.medication_name;
//     current_user.medication_time;
//   }
// }
// var nodeMove = document.createElement("LI");
// nodeMove.innerHTML = "<p>CONTENTS</p>";
// morningMed.appendChild(nodeMove);

const sql = 'SELECT * FROM medication'
db.all(sql,[],(err,rows)=>{
    rows.forEach((row)=>{console.log(row)})
})

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
