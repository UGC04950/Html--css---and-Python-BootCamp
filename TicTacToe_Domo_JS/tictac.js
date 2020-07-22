// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}
restart.addEventListener('click',clearBoard);

// check square marker

function changerMarker(){
  if(this.textContent === ''){
    this.textContent = "X";
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
  }

 for (var i = 0; i < squares.length; i++) {
   squares[i].addEventListener('click',changerMarker)
 }
