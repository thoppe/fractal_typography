all:
	python build_recursion.py
clean:
	find . -name "*~" | xargs -I {} rm -vf {}
	find . -name "*.log" | xargs -I {} rm -vf {}
	find . -name "*.aux" | xargs -I {} rm -vf {}	
