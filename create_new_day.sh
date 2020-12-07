#!/usr/local/bin/bash
day=""

if [[ $# -eq 1 ]]; then
    day=$1
else
    printf "Day missing: create_new_day.sh XX\n"
    exit 1
fi

current_dir=$PWD"/"
day_dir="day"${day}
printf "$current_dir\n"
printf "$day_dir\n"

if [[ ! -d $current_dir$day_dir ]]; then
   mkdir "$current_dir$day_dir"
   cd "$current_dir$day_dir"
   touch input.txt
   touch inputtest.text
   touch solution.py
else
    printf "Already exists\n";
fi

