@echo off
setlocal

set URL="http://localhost:8100/emoji"

for /L %%i in (1,1,10) do (
    START curl %URL%
)

endlocal

