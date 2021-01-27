# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.0
#  Last Updated: May 6th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform
import nukescripts

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\jkrishnaswamy\.nuke'
MacOSX_Dir = '/Users/jkrishnaswamy/.nuke'
Linux_Dir = '/home/jkrishnaswamy/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None


# ///////////////////////////////////////////////////////
# Create a custom toolbar / menu
# ///////////////////////////////////////////////////////

menubar = nuke.menu("Nodes")
m = menubar.addMenu("jkrishTools")  # Rename me to whatever you want
m.addCommand('EdgeScatter', "nuke.tcl('EdgeScatter.gizmo')")
m.addCommand('AdditiveKeyer', "nuke.tcl('AdditiveKeyer.gizmo')")
m.addCommand('AdditiveKeyer2', "nuke.tcl('AdditiveKeyer2.gizmo')")
m.addCommand('AdvancedGrain', "nuke.tcl('AdvancedGrain.gizmo')")
m.addCommand('AP_Fractal_blur', "nuke.tcl('AP_Fractal_blur.gizmo')")
m.addCommand('AutoFlare2', "nuke.tcl('AutoFlare2.gizmo')")
m.addCommand('backdropTools', "nuke.tcl('backdropTools.gizmo')")
m.addCommand('Caustics', "nuke.tcl('Caustics.gizmo')")
m.addCommand('Chromatic_Aberration', "nuke.tcl('Chromatic_Aberration.gizmo')")
m.addCommand('colorPickerID', "nuke.tcl('colorPickerID.gizmo')")
m.addCommand('DeadFrame', "nuke.tcl('DeadFrame.gizmo')")
m.addCommand('DeepCropSoft', "nuke.tcl('DeepCropSoft.gizmo')")
m.addCommand('DeFlicker', "nuke.tcl('DeFlicker.gizmo')")
m.addCommand('delightful', "nuke.tcl('delightful.gizmo')")
m.addCommand('DespillMadness', "nuke.tcl('DespillMadness.gizmo')")
m.addCommand('EdgeExtend2', "nuke.tcl('EdgeExtend2.gizmo')")
m.addCommand('expoglow', "nuke.tcl('expoglow.gizmo')")
m.addCommand('ExpressionWaveGenerator', "nuke.tcl('ExpressionWaveGenerator.gizmo')")
m.addCommand('FlareFactory', "nuke.tcl('FlareFactory.gizmo')")
m.addCommand('HeatWave', "nuke.tcl('HeatWave.gizmo')")
m.addCommand('IBKCleanPlate', "nuke.tcl('IBKCleanPlate.gizmo')")
m.addCommand('Image2Geo_v2', "nuke.tcl('Image2Geo_v2.gizmo')")
m.addCommand('L_Grain_v05', "nuke.tcl('L_Grain_v05.gizmo')")
m.addCommand('Looper', "nuke.tcl('Looper.gizmo')")
m.addCommand('Multimatte', "nuke.tcl('Multimatte.gizmo')")
m.addCommand('normalmap', "nuke.tcl('normalmap.gizmo')")
m.addCommand('nReflection', "nuke.tcl('nReflection.gizmo')")
m.addCommand('NukeCollect', "nuke.tcl('NukeCollect.gizmo')")
m.addCommand('P_Matte', "nuke.tcl('P_Matte.gizmo')")
m.addCommand('P_Noise3D', "nuke.tcl('P_Noise3D.gizmo')")
m.addCommand('Pixelate', "nuke.tcl('Pixelate.gizmo')")
m.addCommand('RippleDistortion', "nuke.tcl('RippleDistortion.gizmo')")
m.addCommand('T_HeatDistortion', "nuke.tcl('T_HeatDistortion.gizmo')")
m.addCommand('V_EdgeMatte', "nuke.tcl('V_EdgeMatte.gizmo')")
m.addCommand('X_Tesla', "nuke.tcl('X_Tesla.gizmo')")

m.addCommand('rotateMatrix', "nuke.tcl('rotateMatrix.gizmo')")
m.addCommand('deHaze', "nuke.tcl('deHaze.gizmo')")
m.addCommand('NaNKiller', "nuke.tcl('NaNKiller.gizmo')")
m.addCommand('DeadFrames_v2', "nuke.tcl('DeadFrames_v2.gizmo')")
m.addCommand('commonkeyer', "nuke.tcl('commonkeyer.gizmo')")
m.addCommand('deeptoPworld', "nuke.tcl('deeptoPworld.gizmo')")
m.addCommand('pproject', "nuke.tcl('pproject.gizmo')")
m.addCommand('edgeMaster_v06', "nuke.tcl('edgeMaster_v06.gizmo')")





nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")

###nuke.menu('Nuke').addCommand('Edit/Redo', 'nuke.redo()', 'Ctrl+Y')
nuke.menu('Nuke').addCommand('Shuffle', 'nuke.createNode("Shuffle")', 'H')
