' keep_awake.vbs
' This script simulates a key press every 60 seconds to prevent screen timeout.

Set WshShell = CreateObject("WScript.Shell")

Do
  WshShell.SendKeys("{SCROLLLOCK}") ' Toggle Scroll Lock
  WScript.Sleep 100
  WshShell.SendKeys("{SCROLLLOCK}") ' Toggle back
  WScript.Sleep 60000
Loop
