alert("There is nothing suspicious about this website")

var full_name = prompt("What is your full name?")
var age = prompt("What is your age?")
var height = prompt("What is your height in centirmeters (cm)")
var pet = prompt("What is your pets name?")
// prompt 1 conditions 
var full_name = full_name.split(" ")
var first_name = full_name[0]
var last_name = full_name[1]

// prompt 4 conditions
var last_chars = pet.charAt(pet.length-1)

if (first_name[0] === last_name[0] && age >=20 && age <=30 && height >=170 && last_chars=="y") {
    console.log("Welcome comrade. Your next mission is in the Titirangi markets that are on the last sunday of every month")
}
else {
    console.log("Hello " + first_name +". It was nice to meet you")
}