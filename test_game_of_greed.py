import pytest

from game_of_greed import calculate_score

# non scoring roll should return 0
def test_zilch():
  expected = 0
  actual = calculate_score(0)
  assert actual == expected

# rolls with various number of 1s should return correct score
def test_ones():
    assert calculate_score(1, 1) == 100
    assert calculate_score( 1,2 ) == 200
    assert calculate_score( ['1']*3) == 1000
    assert calculate_score( ['1']*4) == 2000
    assert calculate_score( ['1']*5) == 3000
    assert calculate_score( ['1']*6) == 4000


# rolls with various number of 2s should return correct score
def test_twos():
    assert calculate_score( ['2']) == 0
    assert calculate_score( ['2']*2) == 0
    assert calculate_score( ['2']*3) == 200
    assert calculate_score( ['2']*4) == 400
    assert calculate_score( ['2']*5) == 600
    assert calculate_score( ['2']*6) == 800

# rolls with various number of 3s should return correct score
def test_threes():
    assert calculate_score( ['3']) == 0
    assert calculate_score( ['3']*2) == 0
    assert calculate_score( ['3']*3) == 300
    assert calculate_score( ['3']*4) == 600
    assert calculate_score( ['3']*5) == 900
    assert calculate_score( ['3']*6) == 1200

# rolls with various number of 4s should return correct score
def test_fours():
    assert calculate_score( ['4']) == 0
    assert calculate_score( ['4']*2) == 0
    assert calculate_score( ['4']*3) == 400
    assert calculate_score( ['4']*4) == 800
    assert calculate_score( ['4']*5) == 1200
    assert calculate_score( ['4']*6) == 1600

# rolls with various number of 5s should return correct score
def test_fives():
    assert calculate_score( ['5']) == 50
    assert calculate_score( ['5']*2) == 100
    assert calculate_score( ['5']*3) == 500
    assert calculate_score( ['5']*4) == 1000
    assert calculate_score( ['5']*5) == 1500
    assert calculate_score( ['5']*6) == 2000

# rolls with various number of 6s should return correct score
def test_sixes():
    assert calculate_score( ['6']) == 0
    assert calculate_score( ['6']*2) == 0
    assert calculate_score( ['6']*3) == 600
    assert calculate_score( ['6']*4) == 1200
    assert calculate_score( ['6']*5) == 1800
    assert calculate_score( ['6']*6) == 2400

# 1,2,3,4,5,6 should return correct score
def test_straight():
     straight = ['1', '2', '3', '4', '5', '6']
     assert calculate_score(straight) == 1500

# 3 pairs should return correct score
def test_three_pairs():
    three_pairs = []
    assert calculate_score(three_pairs) == 1500

# 2 sets of 3 should return correct score
def test_two_trios():
    pass

# 1s not used in set of 3 (or greater) should return correct score
def test_leftover_ones():
    pass

# 5s not used in set of 3 (or greater) should return correct score
def test_leftover_fives():
    pass