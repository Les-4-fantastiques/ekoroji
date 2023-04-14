// function to toggle the task done status
function toggleDone(taskId) {
    // send a PUT request to the server to update the task done status
    fetch(`/tasks/${taskId}/done`, { method: 'PUT' })
      .then(response => response.json())
      .then(data => {
        // update the task item on the page with the new status
        const taskItem = document.getElementById(`task-${taskId}`);
        taskItem.classList.toggle('done', data.done);
      })
      .catch(error => console.error(error));
  }
  
  // function to handle the task search
  function handleSearch(event) {
    const query = event.target.value.trim();
    const taskList = document.querySelector('.task-list');
    // send a GET request to the server to get the matching tasks
    fetch(`/tasks?q=${query}`)
      .then(response => response.text())
      .then(html => {
        // replace the task list with the search results
        taskList.innerHTML = html;
      })
      .catch(error => console.error(error));
  }
  
  // add event listeners to the search input and all task done buttons
  document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', handleSearch);
    const doneButtons = document.querySelectorAll('.done-button');
    doneButtons.forEach(button => {
      button.addEventListener('click', event => {
        const taskId = event.target.dataset.taskId;
        toggleDone(taskId);
      });
    });
  });
  