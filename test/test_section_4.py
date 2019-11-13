# Section 4
import pytest
from mod3_assessment import (
    ans6,
    ans7,
    ans8,
    ans9_prior,
    ans9_posterior,
    ans9_likelihood
)

@pytest.mark.section4
def test_ans6():
    assert ans6 == 0.2, "Not correct"
    
@pytest.mark.section4
def test_ans7():
    assert round(ans7, 2) == 0.04, "Not correct"
    
@pytest.mark.section4    
def test_ans8(pet):
    assert pet in ans8.lower(), "Not correct"

@pytest.mark.section4
def test_ans9_prior(nine1):
    assert ans9_prior == nine1, "Not correct"

@pytest.mark.section4
def test_ans9_posterior(nine2):
    assert ans9_posterior == nine2, "Not correct" 

@pytest.mark.section4
def test_ans9_likelihood(nine3):
    assert ans9_likelihood == nine3, "Not correct"