
function send(){
    let mes_text = document.getElementById("in").value
    document.getElementById("in").value = ""
    let cont = document.getElementById("massages")

    let new_mes = document.createElement("div")
    new_mes.setAttribute("id", "mes")

    let new_user = document.createElement("span")
    new_user.innerHTML = 'User 1'
    new_user.setAttribute("id", "user")

    let new_text = document.createElement("span")
    new_text.innerHTML = mes_text
    new_text.setAttribute("id", "text")

    new_mes.appendChild(new_user)
    new_mes.appendChild(new_text)
    cont.appendChild(new_mes)
}