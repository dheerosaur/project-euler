#!/usr/bin/env bash

number=`printf %03d $1`

git add data/$number python/$number.py javascript/$number.js

if [ -f ruby/$number.rb ]; then
    git add ruby/$number.rb
fi

git commit -m "Add solution to $number"
