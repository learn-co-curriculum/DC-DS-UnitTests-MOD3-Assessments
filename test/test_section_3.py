# Section 3
import pytest
from mod3_assessment import (
    queso_results
)

# Question 3: 
# Run a statistical test on the two samples to determine if you should reject or fail to reject the null hypothesis above.
@pytest.mark.section3
def test_queso_results():
    assert round(queso_results[0], 2) == -19.09, "Statistic value is incorrect."
    assert queso_results[1] == 9.311305589394212e-75, "pvalue is incorrect."