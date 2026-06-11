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
        vegaEmbed(element, spec, { actions: false, renderer: "svg" });
        node.dataset.rendered = "true";
      } catch (error) {
        element.textContent = "Chart failed to render.";
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
})();
