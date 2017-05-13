EMACS=emacs
CASK=cask
PACKAGE-NAME=yahtzee.el

all: build

checkdoc:
	$(EMACS) -Q -batch --eval "(checkdoc-file \"${PACKAGE-NAME}\")"

package-lint: cask
	${CASK} exec $(EMACS) -Q --batch -l "package-lint.el" \
	-f "package-lint-batch-and-exit" ${PACKAGE-NAME}

build: checkdoc package-lint
	${CASK} exec  $(EMACS) -Q --batch \
	--eval "(progn \
	           (setq byte-compile-error-on-warn t)  \
	           (batch-byte-compile))" ${PACKAGE-NAME}

cask:
	${CASK} install

test: build
	${CASK} exec ert-runner

clean :
	@rm -f *.elc
	@rm -rf .cask

.PHONY:	all checkdoc package-lint build cask clean test
