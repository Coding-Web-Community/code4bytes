@echo off & setlocal & goto main

:hextoint %1:string
set "remainingHexString=%~1"
set /a position = 0
set /a base = 16
set /a result = 0
set "hexCharValueMap=(a:10,b:11,c:12,d:13,e:14,f:15)"

:_hextoint
if not defined remainingHexString echo:%result%&exit /b 0
set "currentChar=%remainingHexString:~-1%
set "remainingHexString=%remainingHexString:~0,-1%"
set "currentDigit="

call :power %base% %position%
set /a multiplier = %errorlevel%
set /a position += 1

if "%currentChar%" geq "0" if "%currentChar%" leq "9" (
  set /a currentDigit = %currentChar%
)
if /i "%currentChar%" geq "a" if /i "%currentChar%" leq "f" (
  for %%p in %hexCharValueMap% do for /f "tokens=1,2 delims=:" %%c in ("%%p") do (
    if /i "%currentChar%" equ "%%c" set /a currentDigit = %%d
  )
)

if not defined currentDigit echo:0&exit /b 1
set /a result += multiplier * currentDigit
goto _hextoint


:power %1:number %2:number
setlocal
set /a result = 1
for /l %%i in (1 1 %2) do set /a result *= %1
endlocal & exit /b %result%


:main
if "%~1"=="" (
  set /p "input=Input Hexadecimal: "
  set "stayOpen=true"
) else (
  set "input=%~1"
)
call :hextoint "%input%"
set "success=%errorlevel%"
if defined stayOpen pause
endlocal & exit /b %success%