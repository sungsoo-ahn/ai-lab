(function () {
  function renderVegaSpecs() {
    if (typeof vegaEmbed !== "function") {
      return;
    }

    document.querySelectorAll(".ai-lab-vega-spec").forEach(function (node) {
      var target = node.getAttribute("data-target");
      if (!target || node.dataset.rendered === "true") {
        return;
      }

      var element = document.getElementById(target);
      if (!element) {
        return;
      }

      try {
        var spec = JSON.parse(node.textContent || "{}");
        var fallback = element.innerHTML;
        vegaEmbed(element, spec, { actions: false, renderer: "svg" })
          .then(function () {
            node.dataset.rendered = "true";
            element.classList.add("ai-lab-vega-rendered");
          })
          .catch(function (error) {
            element.innerHTML = fallback;
            element.classList.add("ai-lab-vega-error");
            console.error("AI Lab Vega-Lite render failed", error);
          });
      } catch (error) {
        element.classList.add("ai-lab-vega-error");
        console.error("AI Lab Vega-Lite render failed", error);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderVegaSpecs);
  } else {
    renderVegaSpecs();
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(renderVegaSpecs);
  }

  window.addEventListener("load", renderVegaSpecs);
  window.addEventListener("resize", renderVegaSpecs);
  document.addEventListener("toggle", function (event) {
    if (event.target && event.target.matches && event.target.matches(".ai-lab-run-detail")) {
      renderVegaSpecs();
    }
  }, true);
})();
