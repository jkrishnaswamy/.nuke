import nuke

def tagAndBag_writeSetup () :

	a=nuke.selectedNodes()
	for w in a:
	    w.knob('datatype').setValue(1)
	    w.knob('batch_size').setValue(5)
	    w.knob('cpu').setValue(4)
	    w.knob('ram').setValue(16)
