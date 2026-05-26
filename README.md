# ParaView Visualization Showcase

**One-line:** Reproducible ParaView visualization pipeline demonstrating pvpython scripting, state files, automated headless rendering, and CI.

**Skills demonstrated**
- ParaView Python scripting (`paraview.simple`)
- ParaView state file (`.pvsm`)
- Volume rendering, contours, streamlines, glyphs
- Headless rendering with `pvpython`
- Reproducible outputs and GitHub Actions CI

## Quick start (local)
1. Install ParaView (download from https://www.paraview.org/download/).
2. Clone this repo:
   git clone https://github.com/YOUR_USERNAME/paraview-visualization-showcase.git
3. Generate sample data (optional):
   python3 scripts/generate_sample_vtk.py
4. Run the pipeline headless:
   bash scripts/batch_render.sh
5. Output images will appear in `assets/`.

## Files
- `scripts/render_pipeline.py` — main pvpython script that builds the pipeline and saves PNGs.
- `states/sample_scene.pvsm` — ParaView state for interactive exploration.
- `scripts/generate_sample_vtk.py` — creates `data/sample.vtk` if you want to regenerate sample data.
- `.github/workflows/ci.yml` — optional CI to run `pvpython` and upload artifacts.

## How to extend
- Replace `data/sample.vtk` with your dataset (VTK, VTI, VTU).
- Add animations by varying camera or isosurface values and saving frames.
- Add more color maps and custom transfer functions in `render_pipeline.py`.

## Notes
- This repo is intended as a portfolio piece. Include a short write-up in your GitHub profile README linking to rendered images and describing the visualization choices.
