# Section 3
import pytest
from mod3_assessment import (
    queso_results,
    reject
)

# Question 1: Set up the null and alternative hypotheses for this test.
#       Brainstorm how to grade written answer. (Word Vectors??)

# Question 2: What does it mean to make Type I and Type II errors?
#       Brainstorm how to grade written answer. (Word Vectors??)

# Question 3: 
# Run a statistical test on the two samples to determine if you should reject or fail to reject the null hypothesis above.
@pytest.mark.section3
def test_queso_results():
    assert round(queso_results[0], 2) == -19.09, "T statistic value is incorrect."
    assert queso_results[1] == 9.311305589394212e-75, "pvalue is incorrect."
    
# Question 4: 
# According to the results of the statistical test above explain the decision you would make regarding your null hypothesis and why you made that decision.
@pytest.mark.section3
def test_hypothesis_interpretation():
    assert reject, "Review the results of your T-test's pvalue and reconsider your interpretation."
#       Brainstorm how to grade written answer. (Word Vectors??)

# Question 5: What are the conditions required to perform the test you chose?
# def test_conditions():
#     assert conditions, "check conditions"
#       Brainstorm how to grade written answer. (Word Vectors??)