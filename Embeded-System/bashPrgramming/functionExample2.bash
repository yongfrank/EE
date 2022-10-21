#!/bin/bash

function my_info() {
    lscpu >> $1
    uname -a >> $1
    free -h >> $1
}

# The first time to call function
my_info output.file

# Call the function second time
my_info another_output.file

