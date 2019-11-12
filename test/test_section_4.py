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
    assert ans7 == 0.043478260869565216, "Not correct"
    
@pytest.mark.section4    
def test_ans8():
    assert ans8 == "Pet Store" | "pet store", "Not correct"

@pytest.mark.section4
def test_ans9_prior():
    assert ans9_prior == "P(Store)", "Not correct"

@pytest.mark.section4
def test_ans9_posterior():
    assert ans9_posterior == "P(Store | Large)", "Not correct" 

@pytest.mark.section4
def test_ans9_likelihood():
    assert ans9_likelihood == "P(Large | Store)", "Not correct"