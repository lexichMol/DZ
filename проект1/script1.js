function add(){
    
    let type = document.querySelector("#type").value;
    if(type == "двоечник"){
        let new_name = document.querySelector("#name").value;
        document.querySelector("#name").value = "";
        document.querySelector("#type").value = "";
        let item_list = document.querySelector("#items1")
        let new_item = document.createElement("div");
        new_item.setAttribute("class", "item")
    
        let item_text = document.createElement("p");
        item_text.setAttribute("class", "name");
        item_text.innerHTML = new_name;
    
        let item_btn = document.createElement("button");
        item_btn.setAttribute("class", "delete")
        item_btn.innerHTML = "удалить"
    
        new_item.appendChild(item_text)
        new_item.appendChild(item_btn)
        item_list.appendChild(new_item)

        item_btn.addEventListener("click", () => {
            let parent = item_btn.parentNode;
            parent.parentNode.removeChild(parent);
        });   
    }
    else if(type == "Отличник"){
        let new_name = document.querySelector("#name").value;
        document.querySelector("#name").value = "";
        document.querySelector("#type").value = "";
        let item_list = document.querySelector("#items2")
        let new_item = document.createElement("div");
        new_item.setAttribute("class", "item")
    
        let item_text = document.createElement("p");
        item_text.setAttribute("class", "name");
        item_text.innerHTML = new_name;
    
        let item_btn = document.createElement("button");
        item_btn.setAttribute("id", "delete")
        item_btn.setAttribute("class", "delete")
        item_btn.innerHTML = "удалить"
    
        new_item.appendChild(item_text)
        new_item.appendChild(item_btn)
        item_list.appendChild(new_item)

        item_btn.addEventListener("click", () => {
            let parent = item_btn.parentNode;
            parent.parentNode.removeChild(parent);
        });
    }
    
};

let list_two = document.getElementById("items1")
let list_five = document.getElementById("items2")

function change1(){
    list_five.appendChild(list_two.querySelector(".item"));
}  
function change2(){
    list_two.appendChild(list_five.querySelector(".item"));
}