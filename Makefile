.PHONY: all
all: sdist

.PHONY: sdist
sdist: drafter
	python setup.py sdist

.PHONY: wheel
wheel: drafter
	python setup.py bdist_wheel

.PHONY: drafter
drafter:
	git submodule update --init --recursive
	$(MAKE) -C drafter drafter

.PHONY: clean
clean:
	python setup.py clean
	rm -rf _drafter.c _drafter.so _drafter.o .tox .cache build dist
	$(MAKE) -C drafter distclean
