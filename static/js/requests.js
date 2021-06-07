console.log("Requests.js loaded");

var get_URL="http://127.0.0.1:5000"; // Unused just in case


/**
 * TODO: update this task so that it can handle getting different types of tasks filtered
 * 
 * getTasks() gets the HTML for the task and then updates the taskList
 */
function getTasks(){
    let xhr = new XMLHttpRequest;
    xhr.open('GET', "/request/all_tasks", true);
    xhr.onload = function() {
            if (this.status ===200){
                // For testing
                // console.log(this);
                // console.log(this.responseText);
                updateTasks(this.responseText);
            }
        }

    xhr.send();
}

getTasks();

/**
 * Function takes in the string of text as argument a String and sets it as the
 * innerHTML for the taskList
 */
function updateTasks(taskListHTML){
    if(typeof(taskListHTML) !== "string")
        throw "taskListHTML is not of string type"
    document.getElementById("task-container").innerHTML = taskListHTML;
}