"""
# https://blockdmask.tistory.com/25
● Linux
    1. file editor : vi filename
        1) command mode : ESC
            (1) write : : w filename
            (2) 1word erase : x
            (2) 1line erase : dd
            (2) nline erase : 2dd or 3dd ...

            (3) 1word append : a (input mode change)
            (3) 1line append : o (input mode change)

		(4) cw : 1word replace
		(4) r : 1word replace

            (4) 1line copy : Y
            (4) nline copy : 2YY or 3YY...
            (4) paste : P
            
            (5) undo : u
            (5) redo : Ctrl + R

            (6) exit : :q
            (6) force exit : :q!
            (6) keep : Ctrl + z
        2) input mode : i
    2. workspace save & load
    	1) file foreground(previous work) : fg
	    2) current state save : pushd .
	    2) previous state load : pop .
	3. file control
		1) file copy(file1 -> file2) : cp file1.extension file2.extension
		2) file copy(file1 -> dir1) : cp file1.extension dir1/
		3) multifile copy(file1, file2, ... -> dir1) : cp file1.extension file2.extension dir1/
		4) dir copy(dir1 -> dir2) : cp -r dir1/ dir2/
"""
