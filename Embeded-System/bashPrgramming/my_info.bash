#!/bin/bash

function my_info() {
    lscpu >> $1
    uname -a >> $1
    free -h >> $1
}

