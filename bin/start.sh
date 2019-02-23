#!/usr/bin/env bash

number=`printf %03d $1`

touch data/$number
cp python/{template,$number}.py
cp javascript/{template,$number}.js
