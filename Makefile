#!make

SHELL:=bash

.PHONY: prereqs
prereqs:
	doas pkg_add -u python-3.6 py3-virtualenv-16 py3-pip
	pip3 install virtualenv
	virtualenv .venv
	source generative/bin/activate
	pip3 install -r requirements.pip3

.PHONY: run
run:
	python3 run.py

.PHONY: train
train:
	python3 -c 'raise NotImplementedError()'

.PHONY: evaluate
evaluate:
	python3 -c 'raise NotImplementedError()'

# Arguably this should be moved in Cloud-init
.PHONY: azure-bootstrap
azure-bootstrap:
	./scripts/azure/bootstrap.sh

.PHONY: azure-train
azure-train:
	./scripts/azure/train.sh

.PHONY: azure-deallocate
azure-deallocate:
	./scripts/azure/deallocate.sh

.PHONY: azure-shell
azure-shell:
	./scripts/azure/shell.sh

.PHONY: azure-status
azure-status:
	./scripts/azure/status.sh

.PHONY: clean
clean:
	$(shell find . -name '*~' -delete)
	$(shell find . -name '*\#*' -delete)
