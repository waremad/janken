from janken import *

def test_lscount():
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1]
    lscount([],[3]) == 0
    lscount(ls,[]) == 0
    lscount([],[]) == 3
    lscount(ls,[3]) == 3
    lscount(ls,[4]) == 3
    lscount(ls,[3]) == 3

def test_how_hand():
    pass

