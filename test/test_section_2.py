# Section 2
import pytest
import pandas
from utils import flatten
from mod3_assessment import (
    data,
    mean,
    median,
    zscore,
    std,
    conf,
    ztest_results,
    significant
)

# Question a1:
# Compute the descriptive statistics of check totals.
# @pytest.mark.section2
# def test_data_is_dataframe():
#     assert isinstance(data, pandas.DataFrame), "Your data variable is not of time DataFrame"
    
@pytest.mark.section2
def test_desc_total_check():
    assert round(mean, 2) == 22.02, "Mean is not correctly calculated"
    assert round(median, 2) == 22.02, "Median is not corectly calculated"
    
    
# Question a2: What do the measures of central tendency (mean and median) indicate about the distribution of the check totals?
#       Brainstorm how to grade written answer. (Word Vectors??)


# Question b1: Create a histogram to visually depict the distribution of check totals.
#       Research how to test visualizations
    

# Question b2: Calculate the 95% confidence interval around the mean check total and interpret it correctly
@pytest.mark.section2   
def test_confidence_interval(B2):
    assert zscore == B2, "Your z-score is incorrect"
    assert round(std, 2) == 2.78, "Your standard deviation is incorrect."
    assert isinstance(conf, tuple), "Your conf variable needs to be a tuple"
    assert conf == (16.58064003673802, 27.459707079674754), "Your confidence interval is incorrect."

# Question b3:
# Using a z-test and an  𝛼=0.05 , is my 23 dollar check significantly greater than the mean in our sample? How do you know this?
@pytest.mark.section2
def test_zscore_results():
    assert ztest_results == (-15.785195542782047, 3.934281954785885e-56), "Your ztest was calculated incorrectly"
    assert significant, "Review the results of the z-test."
#       Brainstorm how to grade written answer. (Word Vectors??)
    
# Question b4: How does sampling and the Central Limit Theorem allow us to make inferences on the population mean
#       Brainstorm how to grade written answer. (Word Vectors??)