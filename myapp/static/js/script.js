document.addEventListener('DOMContentLoaded', function() {
  const body = document.body;
  const themeToggle = document.getElementById('themeToggle');

  function themeSwitch() {
    body.classList.toggle('dark-mode');

    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
      table.classList.toggle('table-dark');
    });

    const isDarkMode = body.classList.contains('dark-mode');
    themeToggle.innerHTML = isDarkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
  }

  // Add event listener for themeToggle button
  themeToggle.addEventListener('click', themeSwitch);
});
