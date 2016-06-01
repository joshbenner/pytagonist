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
	rm -f pytagonist.c pytagonist.so
	python setup.py clean
	$(MAKE) -C drafter clean
