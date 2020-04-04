

Dim oFso, f
set oFso = CreateObject("Scripting.FileSystemObject")
set f = oFso.CreateTextFile("D:\test.txt", true) 

f.Write("IRON GOGO")
f.WriteLine("Next row")
f.WriteBlankLines(3)
f.Close()

set f = nothing
set oFso = nothing


Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objTextFile = objFSO.OpenTextFile ("c:\text.txt", 1)
Do Until objFile.AtEndOfStream
     arrFileLines(i) = objFile.ReadLine
     i = i + 1  '一列一列讀取
Loop
objFile.Close
For l = Ubound(arrFileLines) to LBound(arrFileLines) Step -1
    Wscript.Echo arrFileLines(l)
Next

Set objExcel = CreateObject("Excel.Application") 
	objExcel.Visible = True 
'add a new workbook
	Set objWorkbook = objExcel.Workbooks.Add 
'set a cell value at row 1 column 2
	objExcel.Cells(1,2).Value = "a"
	objExcel.Cells(1,3).Value = "b"
	objExcel.Cells(1,4).Value = "c"
'儲存
	objWorkbook.Save "C:\WriteInExcel.xlsx" 
'close the workbook
	objWorkbook(1).Close 
'exit the excel program
	objExcel.Quit
'release objects
	Set objExcel = Nothing
	Set objWorkbook = Nothing