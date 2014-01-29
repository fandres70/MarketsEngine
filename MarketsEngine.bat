@echo off
setlocal enableextensions enabledelayedexpansion



:while1
   
engine.py > log.txt

ping -n 903 127.0.0.1 > nul


        goto :while1
   
endlocal