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

def test_clip():
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1,2,3,0,1]
    assert clip([],0) == []
    assert clip(ls,2) == [3,3]
    assert clip(ls,1) == [2,2,2]
    ls = [0,1,2,3,4,5,6,3,4,5,3,4,0,1,2,3,0,1,2]
    assert clip(ls,3) == [4,0]

def test_max_pic():
    assert max_pic([]) == []
    ls = [0,1,2,3]
    assert max_pic(ls) == ls
    ls = [0,0,0]
    assert max_pic(ls) == [0]
    ls = [0,0,1,1,2,3,3,3,4,4,4]
    assert max_pic(ls) == [3,4]

def test_janwin():
    ls = ["g","c","p"]
    for i in range(100):
        j = janwin([])
        assert len(j) == 1
        assert j in ls
    assert janwin(["g"]) == "g"
    ls = ["g","c","p"]
    for i in range(100):
        j = janwin(ls)
        assert len(j) == 1
        assert j in ls
    assert janwin(["g","c"]) == "g"
    assert janwin(["p","c"]) == "c"
    assert janwin(["g","p"]) == "p"

#jprint("g","c",["me"])
#jprint("g","c",["me","cp","draw","me","cp","draw","me","cp","draw","me","cp","me","me","me","me",])