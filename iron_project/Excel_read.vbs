Dim objExcel
Dim excelPath
Dim worksheetCount
Dim counter                                                      
Dim currentWorkSheet
‘…
excelPath = "C:\users\user\Test.xlsx"
WScript.Echo "Reading Data from Path/File: " & excelPath
Set objExcel = CreateObject("Excel.Application")
objExcel.DisplayAlerts = 0
WScript.Echo "Reading data from worksheet " & workSheetCount
WScript.Echo "-------------------------------------------------------"  & vbCRLF
Set currentWorkSheet = objExcel.ActiveWorkbook.Worksheets(workSheetCount)
' What is the leftmost column in the spreadsheet that has data in it
left = currentWorksheet.UsedRange.Column
Set Cells = currentWorksheet.Cells
'
  For row = 0 to (usedRowsCount-1)
  ' only look at rows/cols in the "used" range
    curRow = row+top
'   curCol = column+left
    If IsEmpty(strDescription) Then ' If Col 2 already populated, skip to next row in sheet
      If Not (IsEmpty(server)) Then
      End If
    End If
  Next
Set currentWorkSheet = Nothing
‘Save and close the workbook - Full code is listed in the FULL SCRIPT, download now
WScript.Echo "Finished."
Set currentWorkSheet = Nothing
' Finished with Excel object, release it from memory & get out !!!
Set objExcel = Nothing
WScript.Quit(0)
objRes.close
ObjCn.close
'---------------------
   
'-------------------------------------------------------------------------
' Subroutine (checksvr) to check for the sever name in Active Directory
'-------------------------------------------------------------------------
'
Sub checksvr(svr)
On Error Resume Next
' Point to the domain/ldap root
Set objRootDSE = GetObject("LDAP://RootDSE")
' Query all Active Directory (normally, leave this commented, query specific OU(s)
' strRoot = objRootDSE.Get("DefaultNamingContext") 'Uncomment to search ENTIRE AD TREE
' Query a specific Organizational Unit
strRoot = "OU=Servers,DC=YOUR-DOMAIN,DC=com" ' Comment this out, if searching ALL OF AD
‘…
 objCn.Provider = "ADsDSOObject"
objCn.Open "Active Directory Provider"
' Filter the query for only sAMAccountName,description of any computers in AD
objCmd.commandtext = …
‘…
svrcmp = UCase(svr) & "$" 'Upper-case the Server entry from the spreadsheet for consistent compare
svrflag = "" 'Clear out the "found-server" flag
Do While Not objRes.EOF
' If description is blank/null, set the value to the word "BLANK"
    strDescription = ""
    If Not (IsNUll(objRes.Fields("description").Value)) Then
       ‘ …
‘Full code is listed in the FULL SCRIPT, download now
     ' We want to check ALL descriptions, including null descriptions
    ' But only for the server passed into this script as an argument
    If svrcmp = objRes.Fields("sAMAccountName").Value Then
     'If Excel server name found in AD, set svrflag = "TRUE" & end the subroutine
      svrflag = "TRUE"
     'Write this to the Excel spreadsheet / exit the subroutine
      Exit Sub
    End If
   'Move to / read the next AD resource record
    objRes.MoveNext
Loop
   'If flag never set to "TRUE" then fall out through here - server not found in AD
    strDescription = "NOT FOUND IN AD"
objRes.close
ObjCn.close
'-------------------------------------------------------------------------
 End Sub