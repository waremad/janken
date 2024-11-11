from janken import *

def test_lscount():
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1]
    assert lscount([],[3]) == 0
    assert lscount(ls,[]) == 0
    assert lscount([],[]) == 0
    assert lscount(ls,[3]) == 3
    assert lscount(ls,[4]) == 3
    assert lscount(ls,[3,4]) == 3
    assert lscount(ls,[3,4,5]) == 2
    assert lscount(ls,[0,1]) == 2

def test_how_hand():
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1,2,3,0,1]
    assert how_hand(ls,2) == 3
    assert how_hand(ls,1) == 1
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1,2,3,0,1,2]
    assert how_hand(ls,3) == 4

def test_win():
    assert win("g") == "p"
    assert win("c") == "g"
    assert win("p") == "c"