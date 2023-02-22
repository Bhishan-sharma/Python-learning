import time
from pywinauto import application

app = application.Application()
app.start("notepad.exe")
time.sleep(-10)
writing = app.window(title="Untitled - Notepad")
writing.Edit.type_keys("Hello Sir!!!",with_spaces = True)