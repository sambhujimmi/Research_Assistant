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

// "More" button functionality for loading additional papers dynamically
document.addEventListener("DOMContentLoaded", () => {
  const query = document.getElementById("query")?.value || "";
  const sortDropdown = document.getElementById("sort");
  const loadMoreButton = document.getElementById("load-more");

  // Load saved sort preference from localStorage
  if (localStorage.getItem("sortPreference")) {
    sortDropdown.value = localStorage.getItem("sortPreference");
  }

  // Save sort selection to localStorage when changed
  sortDropdown.addEventListener("change", function () {
    localStorage.setItem("sortPreference", this.value);
  });

  // Handle "More" button click
  if (loadMoreButton) {
    loadMoreButton.addEventListener("click", function () {
      let start = parseInt(this.getAttribute("data-start"));
      let sort = sortDropdown.value; // Get selected sort value

      fetch("/load_more", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query, start: start, sort: sort }),
      })
        .then((response) => response.json())
        .then((newPapers) => {
          if (newPapers.length === 0) {
            this.style.display = "none"; // Hide button if no more papers
            return;
          }

          const paperContainer = document.querySelector(".results");
          newPapers.forEach((paper) => {
            const paperDiv = document.createElement("div");
            paperDiv.classList.add("paper");
            paperDiv.innerHTML = `
                      <h3>
                          <a href="${paper.link}" target="_blank">${
              paper.title
            }</a>
                      </h3>
                      <div class="paper-info">
                          <span>
                              <i class="fas fa-users"></i>
                              ${paper.authors.join(", ")}
                          </span>
                          <span>
                              <i class="fas fa-calendar"></i>
                              ${paper.published.substring(0, 4)}
                          </span>
                      </div>
                      <button class="summarize-btn" data-abstract="${
                        paper.summary
                      }" data-fetched="false">
                          <i class="fas fa-chevron-down"></i> View Summary
                      </button>
                      <div class="summary"></div>
                  `;

            paperContainer.appendChild(paperDiv);

            // Attach summary toggle event to the new button
            const summarizeButton = paperDiv.querySelector(".summarize-btn");
            summarizeButton.addEventListener("click", function () {
              const summaryElement = this.nextElementSibling;
              const isFetched = this.getAttribute("data-fetched") === "true";
              const isVisible = summaryElement.style.display === "block";

              if (!isFetched) {
                this.innerHTML =
                  '<i class="fas fa-spinner fa-spin"></i> Loading...';
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
                    this.innerHTML =
                      '<i class="fas fa-chevron-up"></i> Hide Summary';
                  })
                  .catch((error) => {
                    console.error("Error:", error);
                    this.innerHTML =
                      '<i class="fas fa-chevron-down"></i> View Summary';
                  });
              } else {
                summaryElement.style.display = isVisible ? "none" : "block";
                const icon = isVisible ? "down" : "up";
                this.innerHTML = `<i class="fas fa-chevron-${icon}"></i> ${
                  isVisible ? "View" : "Hide"
                } Summary`;
              }
            });
          });

          this.setAttribute("data-start", start + newPapers.length);
        })
        .catch((error) => {
          console.error("Error fetching more papers:", error);
        });
    });
  }
});
