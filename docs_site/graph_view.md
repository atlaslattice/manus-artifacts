# Lattice Graph View (Candidate)

This visualization loads the seed graph from `archive/knowledge_graph/GRAPH_SEED.jsonl` and renders nodes/edges as a force graph.

<div id="graph" style="height: 480px; border: 1px solid #ddd;"></div>

<script src="https://unpkg.com/cytoscape@3.30.4/dist/cytoscape.min.js"></script>
<script>
async function loadGraph() {
  const response = await fetch("../archive/knowledge_graph/GRAPH_SEED.jsonl");
  const text = await response.text();
  const records = text.trim().split("\n").map(line => JSON.parse(line));
  const nodes = records
    .filter(r => r.record_type === "node")
    .map(r => ({ data: { id: r.node_id, label: r.label || r.node_id } }));
  const edges = records
    .filter(r => r.record_type === "edge")
    .map(r => ({ data: { id: r.edge_id, source: r.from, target: r.to, label: r.relation } }));

  cytoscape({
    container: document.getElementById("graph"),
    elements: [...nodes, ...edges],
    style: [
      { selector: "node", style: { "label": "data(label)", "background-color": "#4c78a8", "font-size": "9px" } },
      { selector: "edge", style: { "label": "data(label)", "line-color": "#f58518", "width": 2, "font-size": "7px" } }
    ],
    layout: { name: "cose", animate: false }
  });
}
loadGraph();
</script>
