# Section 2
import pytest
import pandas
from utils import flatten
from mod3_assessment import (
    data,
    mean,
    median,
    mode,
    zscore,
    std,
    conf,
    ztest_results
)

# Question a1:
# Compute the descriptive statistics of check totals.
@pytest.mark.section2
def test_data_is_dataframe():
    assert isinstance(data, pandas.DataFrame), "Your data variable is not of time DataFrame"
    
@pytest.mark.section2
def test_total_check_mean():
    assert mean == 22.020173558206388, "Mean is not correctly calculated"
    
@pytest.mark.section2
def test_total_check_median():
    assert median == 22.019760811774503, "Median is not corectly calculated"

@pytest.mark.section2
def test_total_check_mode():
    assert flatten(mode.shape) == 60, "Mode was not calculated correctly."

# Question b2:
# Calculate the 95% confidence interval around the mean check total and interpret it correctly
@pytest.mark.section2
def test_zscore():
    assert zscore == 1.96, "You're using the wrong Zscore"
    
@pytest.mark.section2
def test_std():
    assert round(std, 2) == 2.78, "Standard Deviation was not calculated correctly."

@pytest.mark.section2   
def test_conf():
    assert conf == (16.58064003673802, 27.459707079674754), "confidence interval is not correctly calculated."

# Question b3:
# Using a z-test and an  𝛼=0.05 , is my 23 dollar check significantly greater than the mean in our sample? How do you know this?
@pytest.mark.section2
def test_zscore_results():
    assert ztest_results == (-15.785195542782047, 3.934281954785885e-56), "Your ztest was calculated incorrectly"