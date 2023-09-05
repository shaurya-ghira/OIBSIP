let tasks = [];

function addTask() {
  const taskInput = document.getElementById("taskInput");
  const taskText = taskInput.value.trim();

//   if (taskText === "") {
//     alert("Please enter a valid task.");    
//     return;
//   }

  tasks.push(taskText);
  taskInput.value="";
  renderTasks();
}


function deleteTask(index) {   tasks.splice(index, 1);
  renderTasks();
}


function renderTasks() {
  const taskList = document.getElementById("taskList");
  taskList.innerHTML = "";

  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <span>${task}</span>
      <button onclick="deleteTask(${index})">Delete</button>
    `;
    taskList.appendChild(li);
  });
}


renderTasks();