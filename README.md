# SaveDAT Library v1.1 (BETA)

 Backup and Restore variables at real-time over multiple 
 Python3 programs

 Using MIT Open Source Licences
 By: Ari Stehney

 This file is the step by step example of how to use the library
 THIS IS A BETA VERSION AND IS MESSY AND IMPERFECT

 Import the library like a regular library
`import savedat`


# setloader()

 This command checks for a file in the program
 Folder named 'DatENV.txt' and reads the data.
 It is used for storing json data.
 always call this command first
`savedat.setloader()`

# write() and read()

 Write and read directly adress the variable holder.
 To write use write(<variable name (string)>, <variable value (variable)>)
 To read use read(<variable name (string)>)

`savedat.write("hello", "Hello, World")`
`print( savedat.read("hello") )`

# backup_env()

 Use this command to backup all of your program's global variables
 to the json save file
`savedat.backup_env()`

# restore_env()

 This command takes all of the stored variables
 and makes them global variables
 no prior definition is required!
`savedat.restore_env()`

# raw() and savedat

 The raw() command returns the savedat variable for addressing 
 data directly
`print( raw() )`
`print( savedat )`

That's it, all of the current commands! 
If you encountor any bugs or errors while
using this library please report them to my github page.
Thank you!

# Cloud Saves (Samba Share Storage)

To Easily save your Pyhon environment to the cloud call setloader with
the Cloud access info. Use cloudmode as true to make this save to samba server

`setloader(ip, user, passwd, cloudmode ,timeout=15, port=139, name_port=137, direct_tcp=False)`

To Save to the cloud you must manually save

`savelink(sharename="Network")`

# State Save Interface

To clarify an entry point function use the entry point decorator
above the command you want to be the entry point, and put all 
arguments in a comma seperated string

`@entrypoint(<arguments>)`
