console.log("Hello World");

var get_URL="http://127.0.0.1:5000" // Unused just in case

/**
 * Function that gets all tasks, visible or not
 */
function getTasks(){
    let xhr = new XMLHttpRequest
    xhr.open('GET', "/request/all_tasks", true)
    xhr.onload = function()
        {
            if (this.status ===200){
                console.log(JSON.parse(this.responseText))
            }
        }

    xhr.send()
}