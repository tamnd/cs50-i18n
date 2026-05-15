// cs50.js — mark active nav links

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var currentPath = window.location.pathname;
    var links = document.querySelectorAll("aside nav a");
    links.forEach(function (link) {
      var href = link.getAttribute("href");
      if (href === currentPath || href === currentPath + "/") {
        link.classList.add("fw-bold");
        link.style.color = "#fff";
      }
    });

    var tooltipTriggers = document.querySelectorAll("[data-bs-toggle='tooltip']");
    tooltipTriggers.forEach(function (el) {
      new bootstrap.Tooltip(el);
    });
  });
})();
