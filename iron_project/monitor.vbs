'************************************
'** Seting basic email information **
'************************************
Set emailObj      = CreateObject("CDO.Message")

emailObj.From     = "ken83924@yahoo.com.tw"
emailObj.To       = "ken83924@gmail.com"

emailObj.Subject  = "Test CDO"
emailObj.TextBody = "Test CDO"

Set emailConfig = emailObj.Configuration
'***************************************
'** 設定寄信需要的工具
'***************************************
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpserver") = "smtp.mail.yahoo.com.tw"
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = 465
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendusing")    = 2  
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") = 1  
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpusessl")      = true 
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendusername")    = "ken83924@yahoo.com.tw"
emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendpassword")    = "zrslwmaeqvrlrtou"
'*******************************************************
'** 設定Content body顯示文字檔的內容**
'*******************************************************
Dim fso, f
Set fso = CreateObject("Scripting.FileSystemObject")
'** Open the file for reading
set f = fso.OpenTextFile("D:\test.txt",1) 
'** The ReadAll method reads the entire file into the variable BodyText
emailObj.Textbody = f.ReadAll
'** Close the file
f.Close
'** Clear variables
Set f = Nothing
Set fso = Nothing

'********************************
'** Parameters (DO NOT CHANGE) **
'*******************************
emailConfig.Fields.Update

emailObj.Send

If err.number = 0 then Msgbox "Done"