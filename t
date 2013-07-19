#!/usr/bin/env bash

TESTS="tests"
if [ $# -gt 0 ]; then
  TESTS=""
  for test in $*; do
  	TESTS=$TESTS" tests."$test
  done
fi

python -m unittest -v $TESTS