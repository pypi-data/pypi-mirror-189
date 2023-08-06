<h1>Disclaimer</h1>
This package has strict syntax. If you do not like strict syntax, do not use.
This package makes file handling simpler. <br><br>Current Version: [Version 0.3.2]
<br><br>
Most functions are still in development, so please report bugs if there are any.
Report bugs by sending an email to adityasrijeet12355@gmail.com
<br><br>
<h1>Example Code</h1>
<br>

```python
from jetdb import functions

db = functions()

db.setup()
```
<h1>Functions Supplied</h1>

• Setup - Updates, Restarts, Removes dependencies in the background
<br>
• Add - Adds a line
<br>
• Index - Finds the line number for you
<br>
• Index Replace - Indexes the line and replaces it
<br>
• New File - Creates a new file for you
<br>
• Clear - Clears a whole file for you
<h1>How to use functions</h1>
<br>
Example code:<br><br>

```python
from jetdb import functions

db = jetdb_txt()

csv_db = jetdb_csv()

db.setup()

filename = "--> INSERT FILENAME HERE <--"

db.clear(f"{filename}")

db.add(f"{filename}", "This module is cool!", msg=False)

db.add(f"{filename}", "This module is cool!", msg=True)

db.index_replace(f"{filename}", "This module is cool!", "This module is the best", msg=False)

db.index(f"{filename}", "This module is the best")

db.printRead(f"{filename}")

csv.readBase(f"{filename}")
```
  
You get it, use the variable you used to control the functions, then you add the function name after it.
<br><br>
Example code:<br>
```python
  from jetdb import functions
  
  db = functions()
  
  db.setup()
  
  db.printRead(f"{filename}")
```

<br>
That previous block of code will read a file and print it.
<h1>Changelog</h1>
<br>
<h2>Version 0.3.2</h2>
+ Added new functions - Name: JetDB-CSV
<br> + New Custom Error [JetDB-CSV]
<br> + 3 New Functions [JetDB-CSV]
<br> + New Custom Error Inspection Statistics [JetDB-CSV]
<br> -\ Original Functions renamed - Name: JetDB-TXT
<h2>Version 0.3.1</h2>
<br>
-\ Removed one dependency
<br> -\ Custom Error bug fix
<br> -\ Colorama dependency changed again
<br> -\ Colorama injection revamp
<h2>Version 0.3.0</h2>
<br>
-\ Changed the dependencies
<br> -\ Minor error bug fixes
<br> -\ Colorama dependency change
<br> -\ Colorama now gets installed in your project
<h2>Version 0.2.99</h2>
<br>
-\ Changed the dependencies
<br> -\ Minor error bug fixes
<br> + Colorama
<br> + Custom Errors
<h2>Version 0.2.4</h2>
<br>
-\ Changed the dependencies
<br> -\ Minor error bug fixes
<br> + Added description
<br> + Added Changelog
<h2>Version 0.2.0</h2>
<br>
+ Added a dependency
<br> + Added index feature
<br> - Removed search line feature
<br> -\ Remastered new file feature
<br> -\ Remastered Index Replace feature
<h2>Version 0.1.5</h2>
<br>
+ Added a dependency
<br> + Added search line feature
<br> -\ Remastered new file feature
<br> -\ Remastered Index Replace feature
<h2>Version 0.1.1</h2>
<br>
-\ Minor bug fixes
<br>
-\ Revamped speed
<br> -\ Patched up clear file function
<h2>Version 0.1.0</h2>
<br>
How everything started:
<br>
+ Wait function<br>
+ Add line function<br>
+ Replace line function beta