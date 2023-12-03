const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Function to set the theme
function setTheme(theme) {
  body.classList.toggle('dark-mode', theme === 'dark');
  const isDarkMode = body.classList.contains('dark-mode');
  themeToggle.innerHTML = isDarkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';

  // Save the theme preference in localStorage
  localStorage.setItem('theme', theme);
}

// Add click event listener to toggle theme
themeToggle.addEventListener('click', function() {
  const isDarkMode = body.classList.contains('dark-mode');
  setTheme(isDarkMode ? 'light' : 'dark');
});

// Page initialization
document.addEventListener('DOMContentLoaded', function () {
  const storedTheme = localStorage.getItem('theme');

  if (storedTheme !== null) {
    setTheme(storedTheme);
    console.log('Stored theme:', storedTheme);
  } else {
    console.log('Thene not found in localStorage');
  }
});
