let table = document.getElementById("t1");
let namesCookie = getCookie("names");
let percentsCookie = getCookie("percents");
let lettersCookie = getCookie("letters");

namesCookie = namesCookie.split(",").slice(1);
percentsCookie = percentsCookie.split(",").slice(1);
lettersCookie = lettersCookie.split(",").slice(1);

for(let i = 0; i < namesCookie.length; i++) {
    let roe = table.insertRow();
    console.log(percentsCookie[i]);
    roe.insertCell().innerHTML = `${namesCookie[i]}`;
    roe.insertCell().innerHTML = `${percentsCookie[i]}%`;
    roe.insertCell().innerHTML = `${lettersCookie[i]}`;
}