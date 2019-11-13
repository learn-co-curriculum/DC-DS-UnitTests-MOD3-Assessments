import pytest

@pytest.fixture
def C3():
    return ['binomial', 'Binomial', 'binomial distribution', 'Binomial Distribution']

@pytest.fixture
def B2():
    return 1.96

@pytest.fixture
def eight():
    return ["Pet Store", "pet store"]

@pytest.fixture
def nine1():
    return "P(Store)"

@pytest.fixture
def nine2():
    return "P(Store | Large)"


@pytest.fixture
def nine3():
    return "P(Large | Store)"

