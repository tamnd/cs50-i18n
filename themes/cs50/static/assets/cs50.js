// cs50.js — reveal body after fonts load, mark active nav links

(function () {
  "use strict";

  // Reveal body once PT Sans is loaded (prevents FOUC)
  function revealBody() {
    document.body.classList.remove("invisible");
    document.body.classList.add("visible");
  }

  if (document.fonts) {
    document.fonts.ready.then(revealBody);
    // Fallback: reveal after 2 seconds regardless
    setTimeout(revealBody, 2000);
  } else {
    setTimeout(revealBody, 300);
  }

  // Mark active nav link based on current URL
  document.addEventListener("DOMContentLoaded", function () {
    var currentPath = window.location.pathname;
    var links = document.querySelectorAll("aside nav a");
    links.forEach(function (link) {
      if (link.getAttribute("href") === currentPath ||
          link.getAttribute("href") === currentPath + "/") {
        link.classList.add("fw-bold");
        link.style.color = "#fff";
      }
    });

    // Initialize Bootstrap tooltips if any
    var tooltipTriggers = document.querySelectorAll("[data-bs-toggle='tooltip']");
    tooltipTriggers.forEach(function (el) {
      new bootstrap.Tooltip(el);
    });
  });
})();
