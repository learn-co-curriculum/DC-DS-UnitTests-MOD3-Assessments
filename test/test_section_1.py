# Section 1
import pandas as pd 
import pytest
from mod3_assessment import (
    ans1,
    ans2,
    ans3,
    ans4,
    ans5,
    k_values,
    probs
)


# Question 1: P(A and B)
@pytest.mark.section1
def test_ans1():
    assert ans1 == 0.28, "ans1 is calculated incorrectly"

# Question 2: P(A|B)
@pytest.mark.section1
def test_ans2():
    assert ans2 == 0.56, "ans2 is calculated incorrectly"
    
# Question 3: What is the probability of drawing a king or a queen?
@pytest.mark.section1
def test_ans3():
    assert ans3 == 2/13, "ans3 is calculated incorrectly"
    
# Question 4: How many possible 5-card combinations can be formed with this deck of 52 cards?
@pytest.mark.section1
def test_ans4():
    assert ans4 == 2598960, "ans4 is calculated incorrectly"

# Question 5: what is the probability of winning 8 points out of 22 draws?
@pytest.mark.section1
def test_ans5():
    assert ans5 == 0.06532117736042573, "ans5 is calculated incorrectly"
    
# Question 6:
# @pytest.mark.section1
# def test_ans5():
#     assert probs == [probability_of_scoring_k(22, 3/13, i) for i in k_values], "Check this test"