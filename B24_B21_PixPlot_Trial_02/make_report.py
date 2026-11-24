"""Turn PixPlot hotspot output into a readable image classification report.

Usage:
    python make_report.py <output_dir> <report_prefix> [report_title]

Example:
    python make_report.py output_c7 classification_c7 "B24_photo (7 clusters)"
"""

import csv
import json
import os
import sys

base = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base, sys.argv[1] if len(sys.argv) > 1 else "output")
prefix = sys.argv[2] if len(sys.argv) > 2 else "classification"
title = sys.argv[3] if len(sys.argv) > 3 else "B24_photo"

data = os.path.join(output_dir, "data")
with open(os.path.join(data, "manifest.json")) as f:
    plot_id = json.load(f)["plot_id"]

with open(os.path.join(data, "imagelists", f"imagelist-{plot_id}.json")) as f:
    images = json.load(f)["images"]

with open(os.path.join(data, "hotspots", f"hotspot-{plot_id}.json")) as f:
    hotspots = json.load(f)

assignment = {}
for hotspot in hotspots:
    for index in hotspot["images"]:
        assignment[images[index]] = (hotspot["label"], hotspot["img"])

csv_path = os.path.join(base, prefix + ".csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "cluster", "cluster_representative"])
    for image in images:
        cluster, representative = assignment.get(image, ("Unassigned", ""))
        writer.writerow([image, cluster, representative])

unassigned = [image for image in images if image not in assignment]
lines = [
    f"# {title} — PixPlot classification",
    "",
    f"- Images processed: {len(images)}",
    f"- Clusters found: {len(hotspots)}",
    f"- Assigned: {len(assignment)} | Unassigned: {len(images) - len(assignment)}",
    "- Method: Inception-v3 image features -> UMAP 2D layout -> k-means hotspots",
    "- Note: these are visual-similarity groupings, not semantic subject labels.",
    "",
    "## Cluster memberships",
    "",
]
for hotspot in hotspots:
    members = [images[i] for i in hotspot["images"]]
    lines += [f"### {hotspot['label']} (representative: {hotspot['img']})", "", ", ".join(members), ""]
if unassigned:
    lines += ["### Unassigned", "", ", ".join(unassigned), ""]

md_path = os.path.join(base, prefix + ".md")
with open(md_path, "w") as f:
    f.write("\n".join(lines))

print(f"Wrote {csv_path} and {md_path}")
for hotspot in hotspots:
    members = [images[i] for i in hotspot["images"]]
    print(f"{hotspot['label']} ({hotspot['img']}, {len(members)}): {', '.join(members)}")
print(f"Unassigned ({len(unassigned)}): {', '.join(unassigned) if unassigned else 'none'}")
