document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#datepicker", {
        inline: true,
        locale: "gr",  // Προαιρετικά για ελληνικά
        onChange: function (selectedDates, dateStr) {
            const taskList = document.getElementById("task-list");
            const selectedDayText = document.getElementById("selected-date");

            selectedDayText.textContent = dateStr;

            fetch(`/tasks/api/tasks-by-day/?date=${dateStr}`)
                .then(response => response.json())
                .then(data => {
                    taskList.innerHTML = '';
                    if (data.tasks.length === 0) {
                        taskList.innerHTML = '<p>Δεν υπάρχουν εργασίες για αυτή την ημέρα.</p>';
                    } else {
                        data.tasks.forEach(task => {
                            const taskDiv = document.createElement('div');
                            taskDiv.className = 'task';
                            taskDiv.innerHTML = `
                                <h4>${task.title}</h4>
                                <p>${task.description}</p>
                                <p>Ολοκληρωμένο: ${task.completed ? '✅' : '❌'}</p>
                            `;
                            taskList.appendChild(taskDiv);
                        });
                    }
                });
        }
    });
});
