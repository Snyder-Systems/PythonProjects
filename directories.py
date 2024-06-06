from pathlib import Path

path1 = Path("venv")
path2 = Path("new")
print(path1.exists()) #checks if directory exists

#path2.mkdir() #creates a new directory
#path2.rmdir() #removes directory


#will find all py files current directory

path3 = Path()
for file in path3.glob('*.py'): #asterisk means everything, means find all .py files *.* means find everything
    print(file)
