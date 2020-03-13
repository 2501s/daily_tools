#!/usr/bin/env python3
import sys
import time
import subprocess as sp
import pathlib


def main():
    timer_length = int(sys.argv[1])
    run = input("Start(y)? > ")

    if run == "y":
        countdown(timer_length)
        print_time_up()
        sp.run(['mpv', '/home/z/git/daily_tools/horn.wav'])
        time.sleep(10)
        sp.run(['mpv', '/home/z/git/daily_tools/horn.wav'])

def countdown(timer_length):
    print("Minutes passed:")
    for minute in range(timer_length):
        print("> {}".format(minute))
        time.sleep(60)


def print_time_up():
    print(" _____ _                              ")
    print("|_   _(_)_ __ ___   ___   _   _ _ __  ")
    print("  | | | | '_ ` _ \ / _ \ | | | | '_ \ ")
    print("  | | | | | | | | |  __/ | |_| | |_) |")
    print("  |_| |_|_| |_| |_|\___|  \__,_| .__/ ")
    print("                               |_|    ")
    

main()
