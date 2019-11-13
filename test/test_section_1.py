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
    assert ans1 == 0.28, "ans1 is calculated incorrectly"

# Question A2: P(A|B)
@pytest.mark.section1
def test_ans2():
    assert ans2 == 0.56, "ans2 is calculated incorrectly"
    
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
    assert ans5 == 0.06532117736042573, "ans5 is calculated incorrectly"
    
# Question C2a: Use the function probability_of_scoring to calculate the probability of drawing 𝑘 points out of 22 draws
@pytest.mark.section1
def test_ans5():
    assert isinstance(k_values, range), "the k_values variable should be a range"
    assert k_values[-1] == 21, "The k_values variable is the incorrect range."
    assert isinstance(probs, list), "The probs variable should be a list"
    assert probs == [0.003113481211226729, 0.020548975994096417, 0.06472927438140372, 0.12945854876280743, 0.18447843198700062, 0.1992367065459607, 0.16935120056406663, 0.1161265375296457, 0.06532117736042573, 0.03048321610153201, 0.011888454279597485, 0.0038907668551409957, 0.001069960885163774, 0.0002469140504224094, 4.761913829575039e-05, 7.619062127320063e-06, 1.0000019042107584e-06, 1.0588255456349209e-07, 8.823546213624342e-09, 5.57276602965748e-10, 2.5077447133458666e-11, 7.164984895273905e-13], "This list doesn't seem to have the correct values"

# Question C2b: Plot the results of 2a. to create the probability mass function.
# @pytest.mark.section1
#     Figure out how to test plots.

# Question C3: What type of distribution does the probability_of_scoring have?
@pytest.mark.section1
def test_dist_type(C3):
    assert dist_type in C3, "This doesn't seem like the correct distribution type."
    