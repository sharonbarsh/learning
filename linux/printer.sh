#!/bin/bash


if [[ $# -gt 1 ]]; then
    echo "only one argument! "
    exit 1
elif [[ $# == 0 ]]; then
    echo "Hi no arguments"
    exit 1
elif [[ $1 == "--hello" ]]; then
    echo "Hello this is printer"
    exit 1
elif [[ $1 == "--bye" ]]; then
    echo "Bye-Bye from printer"
    exit 1
elif [[ $1 == "--help" || $1 == "-h" ]]; then
    echo " --hello,           will print: Hello this is printer"
    echo " --bye,             will print: Bye-Bye from printer"
    echo " -h, --help         will show all the options"
else 
    echo "invailid option"
fi 