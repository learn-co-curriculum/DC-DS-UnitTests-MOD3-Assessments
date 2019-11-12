tests :
	jupyter nbconvert --to script mod3_assessment.ipynb
	python3 -m pytest --disable-pytest-warnings -v
    
section1:
	jupyter nbconvert --to script mod3_assessment.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m section1
    
section2:
	jupyter nbconvert --to script mod3_assessment.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m section2
    
section3:
	jupyter nbconvert --to script mod3_assessment.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m section3
    
section4:
	jupyter nbconvert --to script mod3_assessment.ipynb
	python3 -m pytest --disable-pytest-warnings -v -m section4