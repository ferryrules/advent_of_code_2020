# advent_of_code_2020
My answers to advent of code 2020

Grab your session cookie ID
In Google Chrome, click on the link in advent of code to get your puzzle input (URL is something along the lines of https://adventofcode.com/2020/day/1/input where "1" is the date so https://adventofcode.com/2020/day/13/input would be for December 13th)
Right click and select "Inspect"
At the top of the new window either click on "Application" or the ">>" icon and select Application
In the "Storage" section, under "Cookies" click on the advent of code URL
Find "session" under the "Name" column and copy the value.

In the "days" folder, create a .env file
Create a variable called "SESSION_COOKIE" and set it equal to the value you copied. (ie SESSION_COOKIE = "5328abunchofrandomshit12315")

In terminal, while in the days directory: `python3 day_<#>.py`
