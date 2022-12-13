// menangkap semua element a
document.querySelectorAll("#opts a").forEach((a) =>
     //jika di klik akan menjalankan fungsi computerChoice
     a.addEventListener("click",(element)=>{
        computerChoice(element);
     })


);
function computerChoice(element) {
    //tangkap pilihan user
    let pilihanUser = element.target.innerText;

    // Menangkap element result dengan queryselector untuk menampung
    // Nilai hasil game
    let pilihanComputer = document.querySelector("#result");

    // membuat array pilihan untuk komputer
    let choiches = ["Rock", "Paper","Scissors"];

    // pilihan random untuk komputer
    pilihanComputer.innerHTML =
     choiches[Math.round(Math.random()* choiches.length)];
     pilihanComputer= pilihanComputer.innerHTML;

     // jika pilihan komputer sama dengan pilihan user(Draw)
     if (pilihanUser == pilihanComputer) {
        alert("DRAW");
     }

     // jika pilihan user menang
     if (pilihanUser == "Rock" && pilihanComputer == "Scissors"){
        alert("YOU WIN");
     }else if(pilihanUser == "Paper" && pilihanComputer == "Rock"){
        alert("YOU WIN");
     }else if(pilihanUser == "Scissors" && pilihanComputer == "Paper"){
        alert("YOU WIN");
     }
     // jika pilihan computer yang menang
     if (pilihanUser == "Rock" && pilihanComputer == "Paper"){
        alert("COMPUTER WIN YOU LOSE");
     }else if(pilihanUser == "Paper" && pilihanComputer == "Scissors"){
        alert("COMPUTER WIN YOU LOSE");
     }else if(pilihanUser == "Scissors" && pilihanComputer == "Rock"){
        alert("COMPUTER WIN YOU LOSE");
     }
}