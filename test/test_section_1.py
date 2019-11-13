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
    probs,
    dist_type
)


# Question A1: P(A and B)
@pytest.mark.section1
def test_ans1():
    assert round(ans1, 2) == 0.28, "ans1 is calculated incorrectly"

# Question A2: P(A|B)
@pytest.mark.section1
def test_ans2():
    assert round(ans2, 2) == 0.56, "ans2 is calculated incorrectly"
    
# Question B1: What is the probability of drawing a king or a queen?
@pytest.mark.section1
def test_ans3():
    assert round(ans3, 3) == 0.154, "ans3 is calculated incorrectly"
    
# Question B2: How many possible 5-card combinations can be formed with this deck of 52 cards?
@pytest.mark.section1
def test_ans4():
    assert ans4 == 2598960, "ans4 is calculated incorrectly"

# Question C1: what is the probability of winning 8 points out of 22 draws?
@pytest.mark.section1
def test_ans5():
    assert round(ans5, 2) == 0.07, "ans5 is calculated incorrectly"
    
# Question C2a: Use the function probability_of_scoring to calculate the probability of drawing 𝑘 points out of 22 draws
@pytest.mark.section1
def test_ans5(C2):
    assert type(probs) == list or np.array, "The probs variable should be of type list or array"
    assert probs == C2, "This list doesn't seem to have the correct values"

# Question C2b: Plot the results of 2a. to create the probability mass function.
# @pytest.mark.section1
#     Figure out how to test plots.

# Question C3: What type of distribution does the probability_of_scoring have?
@pytest.mark.section1
def test_dist_type(C3):
    assert C3 in dist_type.lower(), "This doesn't seem like the correct distribution type."
    