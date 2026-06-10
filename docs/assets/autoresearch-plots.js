document.addEventListener("DOMContentLoaded", () => {
  const plots = document.querySelectorAll(".autoresearch-vega-plot");

  plots.forEach(async (plot) => {
    const dataUrl = plot.dataset.json;
    if (!dataUrl) {
      plot.textContent = "Missing data-json attribute.";
      return;
    }

    try {
      const response = await fetch(dataUrl);
      if (!response.ok) {
        throw new Error(`Unable to load ${dataUrl}: ${response.status}`);
      }
      const values = await response.json();
      const title = plot.dataset.title || "BTC score-search trials";

      const spec = {
        $schema: "https://vega.github.io/schema/vega-lite/v5.json",
        title,
        width: "container",
        height: 390,
        data: { values },
        mark: {
          type: "point",
          filled: true,
          opacity: 0.86,
          stroke: "#1f2937",
          strokeWidth: 0.6
        },
        encoding: {
          x: {
            field: "gpu_hours",
            type: "quantitative",
            title: "Approx. compute budget"
          },
          y: {
            field: "net_return",
            type: "quantitative",
            title: "Net return",
            axis: { format: ".0%" }
          },
          color: {
            field: "status",
            type: "nominal",
            title: "Status"
          },
          size: {
            field: "success_rate",
            type: "quantitative",
            title: "Fold success proxy",
            scale: { range: [80, 520] }
          },
          href: {
            field: "run_page",
            type: "nominal"
          },
          tooltip: [
            { field: "trial_id", type: "nominal", title: "Trial" },
            { field: "status", type: "nominal", title: "Status" },
            { field: "hypothesis", type: "nominal", title: "Hypothesis" },
            { field: "config_snippet", type: "nominal", title: "Config" },
            { field: "raw_text_snippet", type: "nominal", title: "Trace/report snippet" },
            { field: "metric_delta", type: "nominal", title: "Metric delta" },
            { field: "gpu_hours", type: "quantitative", title: "GPU hours", format: ".2f" },
            { field: "net_return", type: "quantitative", title: "Net return", format: ".1%" },
            { field: "sharpe", type: "quantitative", title: "Sharpe", format: ".2f" },
            { field: "max_drawdown", type: "quantitative", title: "Max drawdown", format: ".1%" },
            { field: "score", type: "quantitative", title: "Score", format: ".2f" },
            { field: "success_rate", type: "quantitative", title: "Fold success proxy", format: ".0%" }
          ]
        },
        config: {
          view: { stroke: "transparent" },
          axis: { labelColor: "#374151", titleColor: "#1f2937" },
          legend: { labelColor: "#374151", titleColor: "#1f2937" }
        }
      };

      await vegaEmbed(plot, spec, { actions: false, renderer: "canvas" });
    } catch (error) {
      plot.textContent = `Plot failed to load: ${error.message}`;
    }
  });
});

// To add another plot, add a div with class "autoresearch-vega-plot" and
// point data-json at a static JSON file with the same field names.
