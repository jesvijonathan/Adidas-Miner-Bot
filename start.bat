@echo off

Title Adidas miner tool starter
cd %~dp0

:someRoutine
setlocal
%@Try%
  REM
  cd %~dp0
  cd ./
  start /B python main.py
%@EndTry%
:@Catch
  REM
  main.py &
  exit
  exit
:@EndCatch

@echo -ended
@echo.
exit
exit