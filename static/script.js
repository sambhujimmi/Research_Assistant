// Theme toggle functionality
const html = document.documentElement;
const themeToggle = document.querySelector(".theme-toggle");

// Check for saved theme preference or default to light
const savedTheme = localStorage.getItem("theme") || "light";
html.className = savedTheme;
updateThemeToggleIcon(savedTheme);

themeToggle.addEventListener("click", () => {
  const newTheme = html.className === "light" ? "dark" : "light";
  html.className = newTheme;
  localStorage.setItem("theme", newTheme);
  updateThemeToggleIcon(newTheme);
});

function updateThemeToggleIcon(theme) {
  const icon = themeToggle.querySelector("i");
  if (theme === "dark") {
    icon.className = "fas fa-moon";
  } else {
    icon.className = "fas fa-sun";
  }
}

// Summary toggle functionality
document.querySelectorAll(".summarize-btn").forEach((button) => {
  button.addEventListener("click", function () {
    const summaryElement = this.nextElementSibling;
    const isFetched = this.getAttribute("data-fetched") === "true";
    const isVisible = summaryElement.style.display === "block";

    if (!isFetched) {
      // First click - fetch the data
      this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
      const abstract = this.getAttribute("data-abstract");

      fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ abstract: abstract }),
      })
        .then((response) => response.json())
        .then((data) => {
          summaryElement.textContent =
            data.summary || "Error fetching summary.";
          summaryElement.style.display = "block";
          this.setAttribute("data-fetched", "true");
          this.innerHTML = '<i class="fas fa-chevron-up"></i> Hide Summary';
        })
        .catch((error) => {
          console.error("Error:", error);
          this.innerHTML = '<i class="fas fa-chevron-down"></i> View Summary';
        });
    } else {
      // Subsequent clicks - just toggle visibility
      summaryElement.style.display = isVisible ? "none" : "block";
      const icon = isVisible ? "down" : "up";
      this.innerHTML = `<i class="fas fa-chevron-${icon}"></i> ${
        isVisible ? "View" : "Hide"
      } Summary`;
    }
  });
});
