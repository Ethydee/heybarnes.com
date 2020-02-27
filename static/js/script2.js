function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*86400000));
    const expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    const name = cname + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function updateTable() {
    let form = document.getElementById("frm1");
    let table = document.getElementById("t1");
    let name = form.elements[0].value;
    let percent = parseInt(form.elements[1].value);
    let letter;
    if (isNaN(percent)) {
        console.log("Not Number");
        alert("Error: Percent not number.");
    }
    else {
        if (percent >= 98 && percent <= 100) {
            letter = "A+";
        }
        if (percent >= 90 && percent < 98) {
            letter = "A";
        }
        if (percent >= 80 && percent < 90) {
            letter = "B";
        }
        if (percent >= 70 && percent < 80) {
            letter = "C";
        }
        if (percent < 70) {
            letter = "F";
        }
        if (percent > 100) {alert("Error: Percent over 100.");}
        else if (percent < 0 ) {alert("Error: Percent is negative.");}
        else {
            let newrow = table.insertRow();
            let cell = newrow.insertCell();
            let cell1 = newrow.insertCell();
            let cell2 = newrow.insertCell();
            let namesCookie = getCookie("names");
            let percentsCookie = getCookie("percents");
            let lettersCookie = getCookie("letters");

            setCookie("names", namesCookie + "," + name, 365);
            setCookie("percents", percentsCookie + "," + percent, 365);
            setCookie("letters", lettersCookie + "," + letter, 365);

            cell.innerHTML = `${name}`;
            cell1.innerHTML = `${percent}%`;
            cell2.innerHTML = letter;
        }
    }
}
