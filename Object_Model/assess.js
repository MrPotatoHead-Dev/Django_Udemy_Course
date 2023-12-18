var squares = document.querySelectorAll('td')
var restart = document.querySelector('#b')
console.log("connected!")
function clearBoard() {
    for (var i =0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}

restart.addEventListener('click', clearBoard)

var cellOne = document.querySelector('#one')

cellOne.addEventListener('click', function() {
    if (cellOne.textContent ==='') {
        cellOne.textContent = 'X'
    }
})