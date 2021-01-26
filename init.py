# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.
 
## init.py
## loaded by nuke before menu.py
 
nuke.pluginAddPath('./gizmo')
nuke.pluginAddPath('./pixelfudger')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./python')


### adds new LUT ###
nuke.ViewerProcess.register("NAME AS IT APPEARS IN THE LIST", nuke.createNode, ("Vectorfield","vfield_file PATH TO YOUR/LUT.cube colorspaceIn AlexaV3LogC"))

