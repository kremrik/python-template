SHELL := bash
LINE_LENGTH := 59
NO_COLOR := \e[39m
BLUE := \e[34m
GREEN := \e[32m

.PHONY: check
check : unit-tests format lint success

.PHONY: unit-tests
unit-tests :
	@echo
	@echo -e '$(BLUE)UNIT TESTS'
	@echo -e        '----------$(NO_COLOR)'
	@python3 -m pytest ./*/test*.py

.PHONY: type-check
type-check :
	@echo
	@echo -e '$(BLUE)TYPE-HINT CHECKS'
	@echo -e 		'----------------$(NO_COLOR)'
	@mypy ./*/*.py

.PHONY: format
format :
	@echo
	@echo -e '$(BLUE)FORMATTING WITH BLACK'
	@echo -e 		'---------------------$(NO_COLOR)'
	@black ./*/*.py -l $(LINE_LENGTH)

.PHONY: lint
lint :
	@echo
	@echo -e '$(BLUE)LINTING WITH FLAKE8'
	@echo -e 		'-------------------$(NO_COLOR)'
	@flake8 ./*/*.py \
		--max-line-length $(LINE_LENGTH) \
		--ignore=F401 \
		--count \
		|| exit 1

.PHONY: success
success :
	@echo
	@echo -e '$(GREEN)ALL CHECKS COMPLETED SUCCESSFULLY$(NO_COLOR)'


.PHONY: set-hooks
set-hooks:
	@git config core.hooksPath .githooks
	@chmod +x .githooks/*
