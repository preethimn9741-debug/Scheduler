function loadJobs() {
    fetch("/jobs")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to load jobs");
            }
            return response.json();
        })
        .then(data => {
            const jobList = document.getElementById("jobs");
            jobList.innerHTML = "";

            if (data.length === 0) {
                jobList.innerHTML = "<li>No jobs found</li>";
                return;
            }

            data.forEach(job => {
                const li = document.createElement("li");

                li.innerHTML = `
                    <strong>${job.name}</strong><br>
                    <span class="interval">Runs every ${job.interval} seconds</span>
                `;

                jobList.appendChild(li);
            });
        })
        .catch(error => {
            alert("Error loading jobs");
            console.error(error);
        });
}
