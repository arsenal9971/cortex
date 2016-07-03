MANAGE_PY:=python manage.py

PROJECT_ROOT:=.
CRAWLER_ROOT:=worldbrain/cortex/crawler

PIP_REQUIREMENTS_DIR=$(PROJECT_ROOT)/requirements
PIP_REQUIREMENTS_BASE:=$(PIP_REQUIREMENTS_DIR)/base.txt
PIP_REQUIREMENTS_DEV:=$(PIP_REQUIREMENTS_DIR)/dev.txt
PIP_REQUIREMENTS_TRAVIS:=$(PIP_REQUIREMENTS_DIR)/travis.txt
PIP_REQUIREMENTS_PRODUCTION:=$(PIP_REQUIREMENTS_DIR)/prod.txt
PIP_REQUIREMENTS_ALL:=$(PIP_REQUIREMENTS_BASE) $(PIP_REQUIREMENTS_DEV) $(PIP_REQUIREMENTS_TRAVIS) $(PIP_REQUIREMENTS_PRODUCTION)

# rebuild the requirement files
requirements: $(PIP_REQUIREMENTS_ALL)
requirements_rebuild:
	$(RM) $(PIP_REQUIREMENTS_ALL)
	$(MAKE) requirements PIP_COMPILE_ARGS=--rebuild

# compile our requirements dependencies
$(PIP_REQUIREMENTS_DIR)/%.txt: PIP_COMPILE_ARGS?=
$(PIP_REQUIREMENTS_DIR)/%.txt: $(PIP_REQUIREMENTS_DIR)/%.in
	pip-compile --no-header $(PIP_COMPILE_ARGS) --output-file "$@.tmp" "$<" >/tmp/pip-compile.out.tmp || { \
	  ret=$$?; echo "pip-compile failed:" >&2; cat /tmp/pip-compile.out.tmp >&2; \
	  $(RM) "$@.tmp" /tmp/pip-compile.out.tmp; \
	  exit $$ret; }
	@sed -n '1,10 s/# Depends on/-r/; s/\.in/.txt/p' "$<" > "$@"
	@cat "$@.tmp" >> "$@"
	@$(RM) "$@.tmp" /tmp/pip-compile.out.tmp

.PHONY: requirements requirements_rebuild

# run the code style checker
check:
	pylama $(PROJECT_ROOT)/worldbrain

# run the tests
PYTEST_ARGS?=
PYTEST=py.test -c setup.cfg $(PYTEST_ARGS)
test:
	$(PYTEST) $(PROJECT_ROOT)/worldbrain

.PHONY: test

# install the system requirements
system_requirements:
	for pk in $$(cat system-requirements.txt); do sudo apt-get install -yq "$$pk"; done
