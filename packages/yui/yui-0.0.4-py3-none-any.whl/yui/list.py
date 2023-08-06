#!/usr/bin/env python
import os, sys, glob, yaml, subprocess, datetime
from yui import tsklib
from pathlib import Path

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
        Usage:
            """+tsklib.cmd+""" list heap   - list task from heap / global backlog
            """+tsklib.cmd+""" list cur    - list task picked for current day
            """)
        exit(1);
        pass;

    location = argv[0]

    def mb_strlen( s ):
        return len(str(s)) #.encode('utf-16-le'))
        pass

    red="\033[1;31m";
    green="\033[1;32m";
    yellow="\033[1;93m";
    noColor="\033[0m"; # No Color

    colorMap = {
        "new" : red,
        "work" : yellow,
        "done" : green
        }

    tasks = tsklib.listTasks( location )

    if len(tasks) == 0:
        print("No tasks found in "+location+noColor)
        exit(1)
        pass
    keys = ["No.", "id", "context", "project", "name", "status"];

    maxLenghts = {};
    for key in keys:
        #print(key)
        maxLenghts[key] = mb_strlen(key);
        for task in tasks:
            length = mb_strlen(task[key]);
            if length > maxLenghts[key]:
                maxLenghts[key] = length;
                pass
            pass
        pass

    columnNames = {};
    horizontalLines = {};
    rows = []
    for task in tasks:
        rows.append({})
        pass
    for key in keys:
        columnNames[key] = key.ljust( maxLenghts[key])
        horizontalLines[key] = "".ljust( maxLenghts[key], "─")
        for i, task in enumerate(tasks):
            rows[i][key] = str(task[key]).ljust( maxLenghts[key] )
            pass
        pass

    print("╭─"+"─┬─".join(horizontalLines.values())+"─╮");
    print("│ "+" │ ".join(columnNames.values()    )+" │");
    print("├─"+"─┼─".join(horizontalLines.values())+"─┤");
    for i, task in enumerate(tasks):
        row = rows[i]
        color = ""
        #print( row["status"] , colorMap )
        if task["status"] in colorMap.keys():
            color = colorMap[ task["status"] ];
            pass
        print("│ "+color+(noColor+" │ "+color).join(row.values())+noColor+" │")
        pass
    print("╰─"+"─┴─".join(horizontalLines.values())+"─╯")

    print(noColor)
    pass

if __name__ == "__main__":
    main()
    pass
