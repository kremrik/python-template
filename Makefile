SHELL := bash
MODULE := map_ops
LINE_LENGTH := 59
NO_COLOR := \e[39m
BLUE := \e[34m
GREEN := \e[32m

.PHONY: check
check : unit-tests type-check black-format lint success

.PHONY: unit-tests
unit-tests :
	@echo
	@echo -e '$(BLUE)unit-tests'
	@echo -e        '----------$(NO_COLOR)'
	@python3 -m pytest ./*/test*.py

.PHONY: type-check
type-check :
	@echo
	@echo -e '$(BLUE)type-check'
	@echo -e 		'----------$(NO_COLOR)'
	@mypy ./*/*.py

.PHONY: black-format
black-format :
	@echo
	@echo -e '$(BLUE)black-format'
	@echo -e 		'------------$(NO_COLOR)'
	@black ./*/*.py -l $(LINE_LENGTH)

.PHONY: flake8-lint
lint :
	@echo
	@echo -e '$(BLUE)flake8-lint'
	@echo -e 		'-----------$(NO_COLOR)'
	@flake8 ./*/*.py \
		--max-line-length $(LINE_LENGTH) \
		--ignore=F401,E731 \
		--count \
		|| exit 1

.PHONY: success
success :
	@echo
	@echo -e '$(GREEN)ALL CHECKS COMPLETED SUCCESSFULLY$(NO_COLOR)'

#----------------------------------------------------------

.PHONY: coverage
coverage: 
	@pytest --cov=$(MODULE) --cov-config=.coveragerc --cov-report html
	@python3 -m http.server 8000 --directory htmlcov/

.PHONY: set-hooks
set-hooks:
	@git config core.hooksPath .githooks
	@chmod +x .githooks/*
