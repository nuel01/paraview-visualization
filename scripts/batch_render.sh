#!/usr/bin/env bash
set -e
# Run pvpython to render images headless
# Ensure pvpython is on PATH (ParaView installation)
if ! command -v pvpython &> /dev/null; then
  echo "pvpython not found. Please install ParaView and ensure pvpython is on PATH."
  exit 2
fi

# Generate sample data if missing
if [ ! -f data/sample.vtk ]; then
  python3 scripts/generate_sample_vtk.py
fi

pvpython scripts/render_pipeline.py
