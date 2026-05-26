#!/usr/bin/env pvpython
# Render pipeline using paraview.simple
from paraview.simple import *
import os

# Input file
data_file = os.path.join('data', 'sample.vtk')
reader = LegacyVTKReader(FileNames=[data_file])

# Contour (isosurface)
contour = Contour(Input=reader)
contour.ContourBy = ['POINTS', 'Temperature']
contour.Isosurfaces = [320.0]
contour.PointMergeMethod = 'Uniform Binning'

contourDisplay = Show(contour)
contourDisplay.Representation = 'Surface'
contourDisplay.ColorArrayName = ['POINTS', 'Temperature']
contourDisplay.LookupTable = GetColorTransferFunction('Temperature')

# Streamlines (use gradient of scalar as a vector proxy)
# Create a gradient field via Calculator
calc = Calculator(Input=reader)
calc.ResultArrayName = 'GradT'
calc.Function = 'gradient(Temperature)'
gradDisplay = Show(calc)
gradDisplay.Visibility = 0

stream = StreamTracer(Input=calc, SeedType='Point Source')
stream.SeedType.Center = [10,10,10]
stream.SeedType.Radius = 8
stream.SeedType.NumberOfPoints = 100
stream.Vectors = ['POINTS', 'GradT']
streamDisplay = Show(stream)
streamDisplay.ColorArrayName = ['POINTS', 'Temperature']
streamDisplay.LookupTable = GetColorTransferFunction('Temperature')
streamDisplay.Representation = 'Surface'

# Volume rendering (create a slice-to-volume via XMLImageDataReader if available)
# For legacy VTK structured points, use the reader directly for volume
volRep = Show(reader)
volRep.Representation = 'Volume'
volRep.ColorArrayName = ['POINTS', 'Temperature']
volRep.LookupTable = GetColorTransferFunction('Temperature')
volProp = GetDisplayProperties(reader)
volProp.SetScalarOpacity('Temperature', [0.0, 0.0, 300.0, 0.1, 350.0, 0.5, 400.0, 1.0])

# Camera and render settings
renderView = GetActiveViewOrCreate('RenderView')
renderView.Background = [1.0, 1.0, 1.0]
renderView.ViewSize = [1600, 900]
renderView.CameraPosition = [40, 40, 40]
renderView.CameraFocalPoint = [10, 10, 10]

# Color map adjustments
ctf = GetColorTransferFunction('Temperature')
ctf.RescaleTransferFunction(280.0, 380.0)

# Render and save screenshots
if not os.path.exists('assets'):
    os.makedirs('assets')

Render()
SaveScreenshot('assets/overview.png', renderView, ImageResolution=[1600,900])

# Focus on contour only
Hide(reader)
Show(contour)
Render()
SaveScreenshot('assets/contour.png', renderView, ImageResolution=[1600,900])

# Show streamlines
Hide(contour)
Show(stream)
Render()
SaveScreenshot('assets/streamlines.png', renderView, ImageResolution=[1600,900])

print("Render complete. Images saved to assets/")
