empty:
	

clean:
	rm -rf dist

run:
	python3 src/kikan/main.py

watch:
	python3 monitor.py tests/test.py __pycache__,dist

publish:
	python3 -m build && python3 -m twine upload dist/*
