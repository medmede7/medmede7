#!/bin/bash


# This script clears the terminal, displays a greeting and gives information


clear								# clear terminal window

echo "The script starts now."		
echo
echo "------------------------------------------------------------------------------"
echo "This is information provided by $0. Program start now"	# $0 is the executed script var
								# dollar sign is used to get content of variable
echo

echo "=================================== USER ====================================="

echo "Hello, $USER"						# $USER is the actual user
echo
echo "------------------------------------------------------------------------------"

# about currently connected users. The two example variables are set and displayed.
echo "These users are currently connected:"
w | cut -d " " -f 1 | grep -v USER | sort -u			# w: give details on connected user
								# cut remove section from each line of file
								# -d " " option precise the section to be remove
								# -f 1 - option select only the first field of the cut file
								# grep return the associate to "USER" = user name in this case
								# Sort -u sort output and remove redondant

echo

echo "================================ DATE ========================================"

echo "Today's date is `date`, this is week `date +"%V"`."	# '`' allow to interprete a command as it and not as part of the quotes
# test the date for other day to see if it print "Do"
echo
echo "------------------------------------------------------------------------------"
echo "This is the uptime information"
uptime
echo

echo "=============================== SYSTEM ======================================="

echo "This is `uname -s` running on a `uname -m` processor."	# uname print system information
								# -s option for kernel name
								# -m option for processor architecture
echo
echo "------------------------------------------------------------------------------"
echo "I will now fetch you a list of connected users detailed with the 'w' command:" echo # here "'" symbol is not interpreted
set -x								# active debug
w 								# show who is logged on and
set +x								# deactive debug
echo								# what they are doing

echo "=============================== VARIABLES ===================================="

echo "I'm setting two variables now."
COLOUR="black"							# set a local shell variable
VALUE="9"							# set a local shell variable
echo "This is a string: $COLOUR" 				# displays content of variable
echo "And this is a number: $VALUE" 				# displays content of variable
echo
echo "------------------------------------------------------------------------------"
echo "Your home directory is:"
echo $HOME							# displays the home directory
echo
echo "------------------------------------------------------------------------------"
echo "the terminal you are using is:"
echo $TERM							# displays the terminal used
echo
echo "------------------------------------------------------------------------------"
echo "terminal setup is:"
env | grep TERM							# displays lines that contain TERM from env command
echo

echo "============================= USEFUL COMMANDS ================================="

echo "command 'dirs' display the directory stack like `dirs`."
echo
echo "------------------------------------------------------------------------------"
echo "command 'wc' display lines words char and file name of a file like"
echo "`wc $0`."
echo
echo "------------------------------------------------------------------------------"
echo "command 'ps' display running process like"
echo "`ps`"
echo
echo "------------------------------------------------------------------------------"
echo "command 'hash' dispaly the hashed table of command used like" 
echo "`hash`"
echo
echo "------------------------------------------------------------------------------"
echo "command 'hostname' display the name of the host like"
echo "`hostname`"

echo "=============================== END OF NOTES =================================="

#remove the next line to print the first part
clear

echo "================================== TRAINING ==================================="
echo "This is information provided by $0. program starts now."

echo "Hello $USER"
echo

echo "Today's date is `date`, this is week `date +"%V"`."
echo

echo "These users are currently connected:"
w | cut -d " " -f 1 - | grep -v USER | sort -u
echo

echo "This is `uname -s` running on a `uname -m` processor."
echo

echo "This is the uptime information:"
uptime
echo

echo "That's all folks!"
