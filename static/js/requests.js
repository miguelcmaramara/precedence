console.log("Hello World");

var get_URL="http://127.0.0.1:5000" // Unused just in case

/* 
//Depreciated function to get tasks as json rather than html. Kept as reference
function getTasks(){
    let xhr = new XMLHttpRequest;
    xhr.open('GET', "/request/all_tasks", true);
    xhr.onload = function() {
            if (this.status ===200){
                console.log(JSON.parse(this.responseText));
                return JSON.parse(this.responseText);
            }
        }

    xhr.send();
}
// */

function getTasks(){
    let xhr = new XMLHttpRequest;
    xhr.open('GET', "/request/all_tasks", true);
    xhr.onload = function() {
            if (this.status ===200){
                // remove child nodes
                // insert new nodes
                console.log(this);
                console.log(this.responseText);
                var taskList = document.getElementById("task-container");
                taskList.innerHTML = this.responseText;
                // taskList.appendChild(this.responseText);


            }
        }

    xhr.send();
}

getTasks();