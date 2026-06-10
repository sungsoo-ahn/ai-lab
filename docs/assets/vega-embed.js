(function () {
  function embedAiLabPlots() {
    if (typeof vegaEmbed !== "function") {
      return;
    }
    document.querySelectorAll("[data-vega-spec]").forEach(function (element) {
      if (element.dataset.vegaRendered === "true") {
        return;
      }
      element.dataset.vegaRendered = "true";
      vegaEmbed(element, element.dataset.vegaSpec, {
        actions: false,
        renderer: "svg",
      }).catch(function (error) {
        element.textContent = "Plot failed to render: " + error;
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", embedAiLabPlots);
  } else {
    embedAiLabPlots();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(embedAiLabPlots);
  }
})();
