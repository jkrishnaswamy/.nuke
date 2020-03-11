import nuke
import nukescripts

def autocrop () :
    selectedNodes = nuke.selectedNodes()
    n=0
    for readNode in selectedNodes:
        if readNode.Class() == 'Read':
            readNode.setSelected(1)
            print readNode.Class()
            n=n+1
            print n            
            frst = readNode['first'].value()
            lst = readNode['last'].value()

        else :
            readNode.setSelected (0)
    if n ==0:
        nuke.message("Oops, you didn't selected at least one Read node!")
    else :
        nukescripts.autocrop(frst,lst)
        

        
