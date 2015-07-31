### * Variables

PYTHON_MODULE=pypick
PYTHON_MODULE_EGG=$(PYTHON_MODULE).egg-info

### * Help

Help:
	@echo "Makefile for the $(PYTHON_MODULE) Python module                   "
	@echo "                                                                  "
	@echo "Type: \"make <target>\" where <target> is one of the following:   "
	@echo "                                                                  "
	@echo "  install          Install the module and command-line tools      "
	@echo "  uninstall        Uninstall the module                           "

### * Targets

### ** install
install:
	rm -fr $(PYTHON_MODULE_EGG)
	pip install --user .

### ** uninstall
uninstall:
	pip uninstall -y $(PYTHON_MODULE)
