# -*- coding: iso-8859-1 -*-
import sys
import nuke



import frameHoldSet
nuke.addOnUserCreate(frameHoldSet.frameHoldSet, nodeClass="FrameHold") 


import scaleNodes
 
menuBar = nuke.menu("Nuke")
menuBar.addCommand('Edit/Node/Scale/up', 'scaleNodes.scaleNodes( 1.1 )', '=')
menuBar.addCommand('Edit/Node/Scale/down', 'scaleNodes.scaleNodes( 0.9 )', '-')

import alignNodes
menuBar = nuke.menu("Nuke")
menuBar.addCommand('Edit/Node/Align/horizontally', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="x" )', '[')
menuBar.addCommand('Edit/Node/Align/vertically', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="y" )', ']')


import labelAutobackdrop

menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('others/Backdrop', 'labelAutobackdrop.autoBackdrop()', 'Ctrl+m')

import trackRoto

menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/TrackToRoto', 'trackRoto.trackRoto()')

import autocrop

menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/autocrop', 'autocrop.autocrop()')

import tagAndBag_writeSetup

menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/tagAndBag_writeSetup', 'tagAndBag_writeSetup.tagAndBag_writeSetup()')

import CornerPinMocha
menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/CornerPinMocha', 'CornerPinMocha.CornerPinMocha()')


import projection_overscan
menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/projection_overscan', 'projection_overscan.projection_overscan()')

import pasteToSelected
menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand('py/pasteMuti', 'pasteToSelected.pasteToSelected()','Ctrl+Alt+v')



import link_hub

#menubar = nuke.menu("Nuke")
#m = menubar.addMenu("_hub")
menubar = nuke.toolbar('Nodes')
m = menubar.addMenu("tools")
m.addCommand("py/link", "link_hub.linkTools()","Ctrl+l")

#QuickCreate
import h_viewerShortcuts


# set default parameter for knob of node #


nuke.knobDefault('Shuffl
    [pasted text truncated for security]
