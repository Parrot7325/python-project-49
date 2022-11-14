install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user  --force-reinstall dist/*.whl


retry:
	poetry build
	python3 -m pip install --user  --force-reinstall dist/*.whl
	poetry publish --dry-run


token:
	cat ../githubtoken.txt


installation:
	poetry install
	poetry build
	python3 -m pip install --user  --force-reinstall dist/*.whl

push:
	echo Parrot7325
	cat ../githubtoken.txt
	git push
