console.log("posts.js loaded");

/**
 * Completes the task within the database and then updates the file
 * @param {int} taskId 
 */
function taskFinished(taskId){
    if(typeof(taskId) !== "number")
        throw "taskId is not of type int"
    let xhr = new XMLHttpRequest;
    xhr.open('POST', "/post/task_complete",true);
    xhr.onload = function(){
        console.log(taskId);
        document.getElementById(taskId).remove();
        getTasks();
    }
    xhr.send(taskId.toString());


}