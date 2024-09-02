Keeping a copy of the readme here because I don't wanna alter my code to create
this directory...

I was going through some of my old code and found a program I
wrote a few years ago to help me practice mental math, and later
repurposed to help my little brother practice timetables and
monitor his progress.

I decided to rewrite it to see how much my programming mentality
has changed over the years. I've learned some OOP and file handling
since then and wanted to put them to use here.

The updated code is called 'classy_multiplication', and it makes use of
'json_file_generator'. The old code is - for lack of a better name - called
'Old_code'.

Anyway, here are some things I changed in the new version:

- Implemented questions into a class which I could then use a method
  on to return if they were answered correctly.
- Drastically increased the amount of error handling (Not sure if there are 
  any edge cases I missed).
- Separated part of the code into another file.
- Can now keep track of stats in-between executions
- Used a function to dynamically create statfiles as needed to avoid having
  them exist while they aren't needed.
- Clear screen liberally to make experience feel cleaner.
- Added some more pauses to make the whole experience feel less... janky?

Done with this anyway, so I'm gonna move on to learning some Data Structures
and Algorithms while working on something involving Digital Signal Processing
next...

Hurray for Fourier tranforms!
