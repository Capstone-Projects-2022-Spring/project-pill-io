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
