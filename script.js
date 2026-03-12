const API = "http://127.0.0.1:8000/info"


async function addInfo(){

let name = document.getElementById("name").value
let age = document.getElementById("age").value
let home = document.getElementById("home").value

let response = await fetch(API,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
name:name,
age:parseInt(age),
home:home
})
})

let data = await response.json()

document.getElementById("result").innerText = data

}



async function getInfo(){

let id = document.getElementById("id").value

let response = await fetch(API + "?id=" + id)

let data = await response.json()

document.getElementById("name").value = data.name
document.getElementById("age").value = data.age
document.getElementById("home").value = data.home

document.getElementById("result").innerText = JSON.stringify(data)

}



async function updateInfo(){

let id = document.getElementById("id").value
let name = document.getElementById("name").value
let age = document.getElementById("age").value
let home = document.getElementById("home").value

let response = await fetch(API + "?id=" + id,{
method:"PUT",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
name:name,
age:parseInt(age),
home:home
})
})

let data = await response.json()

document.getElementById("result").innerText = data

}



async function deleteInfo(){

let id = document.getElementById("id").value

let response = await fetch(API + "?id=" + id,{
method:"DELETE"
})

let data = await response.json()

document.getElementById("result").innerText = data

}