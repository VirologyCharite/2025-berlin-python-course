from seq import Sequence


def test_id():
    s = Sequence("id1", "ACTT")
    assert s.id == "id1"


def test_sequence():
    s = Sequence("id1", "ACTT")
    assert s.sequence == "ACTT"


def test_length_zero():
    s = Sequence("id1", "")
    assert len(s) == 0


def test_length():
    s = Sequence("id1", "ACTT")
    assert len(s) == 4


def test_gc_content_zero():
    s = Sequence("id1", "ATT")
    assert s.gc_content() == 0.0


def test_gc_content_one_quarter():
    s = Sequence("id1", "ATGT")
    assert s.gc_content() == 25.0


def test_gc_content_empty_sequence():
    s = Sequence("id1", "")
    assert s.gc_content() == 0.0


def test_find_missing():
    s = Sequence("id1", "ACCCT")
    assert s.find("GG") == -1


def test_find_not_missing():
    s = Sequence("id1", "ACCCT")
    assert s.find("CCC") == 1
