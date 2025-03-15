@ECHO OFF

if defined %venvenable% (goto main) else (goto venv)

:main
sphinx-autobuild source build
popd

:venv
..\.venv\scripts\activate
set venvenable = true
goto main
