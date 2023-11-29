const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Conditionally format rows
function condFormat() {
  var rows = document.querySelectorAll('table tr');
  rows.forEach(function(row) {
    if (row.cells[0].textContent === 'TBC') {
      row.classList.add('table-warning');
    }else if (row.cells[0].textContent === 'Go') {
      row.classList.add('table-success');
    }
  });
}

themeToggle.addEventListener('click', function () {
  // Toggle dark mode for the body
  body.classList.toggle('dark-mode');

  // Toggle dark mode for every table
  const tables = document.querySelectorAll('table');
  tables.forEach(table => {
    table.classList.toggle('table-dark');
  });

  // Update the theme toggle button icon
  const isDarkMode = body.classList.contains('dark-mode');
  themeToggle.innerHTML = isDarkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
});

document.addEventListener('DOMContentLoaded', condFormat);