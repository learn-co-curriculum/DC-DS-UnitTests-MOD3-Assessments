tests :
	jupyter nbconvert --to script mod3_assessment.ipynb
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py
	python3 -m pytest --disable-pytest-warnings -v
    
section1:
	jupyter nbconvert --to script mod3_assessment.ipynb
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py    
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py    
	python3 -m pytest --disable-pytest-warnings -v -m section1
    
section2:
	jupyter nbconvert --to script mod3_assessment.ipynb
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py    
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py    
	python3 -m pytest --disable-pytest-warnings -v -m section2
    
section3:
	jupyter nbconvert --to script mod3_assessment.ipynb
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py    
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py    
	python3 -m pytest --disable-pytest-warnings -v -m section3
    
section4:
	jupyter nbconvert --to script mod3_assessment.ipynb
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py    
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py    
	python3 -m pytest --disable-pytest-warnings -v -m section4
    
answers:
	jupyter nbconvert --to script ans-mod3_assessment.ipynb
	cp "ans-mod3_assessment.py" "mod3_assessment.py"
	rm "ans-mod3_assessment.py"
	sed -i '' '/get_ipython/s/^/# /' mod3_assessment.py
	sed -i '' '/'plt.show'/s/^/# /' mod3_assessment.py
	python3 -m pytest --disable-pytest-warnings -v