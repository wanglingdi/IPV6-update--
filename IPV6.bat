@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
@echo off
echo netsh interface ipv6 set privacy state=disable

cls
@ECHO OFF
title Open or Close WEB
CLS
color 0a
GOTO MENU
:MENU
ECHO.
ECHO. ==============Open or Close==============
ECHO.
ECHO. 1 Closea
ECHO. 2 Openb
ECHO. 3 Exit
ECHO. ==========================================
ECHO.
ECHO.
echo. Please inputer your choose:
set /p ID=
if "%id%"=="1" goto qiyong
if "%id%"=="2" goto jinyong
if "%id%"=="3" exit
PAUSE
:qiyong
echo Closea
netsh interface set interface name="YTW" admin=DISABLED
goto MENU
:jinyong
echo Openb
netsh interface set interface name="YTW" admin=ENABLED
GOTO MENU