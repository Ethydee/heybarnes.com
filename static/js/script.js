function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

document.getElementById("demo").innerHTML = "Barnes";

function myFunction() {
    const x = document.getElementById("frm1");
    let text = "";
    for (i = 0; i < x.length ;i++) {
        text += x.elements[i].value + " ";
    }
    document.getElementById("demo").innerHTML = text;
}

function colors() {
    let cols = [];
    let text = "Epic Website";
    let randColor;
    for (let i = 0; i < text.length; i++) {
        randColor = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
        cols += `<span style="color: ${randColor}">${text[i]}</span>`
    }
    document.getElementById("Tonin").innerHTML = cols;
    return cols
}

function updateGrades() {
    document.getElementById("grades").innerHTML = "";
    const names = ["Ron", "Shane", "Mr. Walter", "Barnes", "Mr. Hudson", "Mrs. Owen"];
    const grades = {};
    let num;
    let letter;
    for (let name in names) {
        num = getRandomInt(60, 100);
        if (num >= 98 && num < 100) {
            letter = "A+";
        }
        if (num >= 90 && num < 98) {
            letter = "A";
        }
        if (num >= 80 && num < 90) {
            letter = "B";
        }
        if (num >= 70 && num < 80) {
            letter = "C";
        }
        if (num < 70) {
            letter = "F";
        }
        grades[names[name]] = getRandomInt(100);
        document.getElementById("grades").innerHTML +=
            `<li>${names[name]}: ${num}% ${letter}`;
    }
}

updateGrades()
colors()
