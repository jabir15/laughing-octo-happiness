set /p fn="Enter test name "
set /p sn="Enter subject name "
python examrand.py %fn%_questions %sn% ch1 1 ch2 1 ch3 1 ch4 1 ch5 1 ch6 1 ch7 2 ch8 2
cd %cd%\exams
pdflatex -jobname=quiz/%fn% "\gdef\condition{0}\gdef\questionbank{%fn%_questions}\input base"
pdflatex -jobname=quiz/%fn% "\gdef\condition{0}\gdef\questionbank{%fn%_questions}\input base"
pdflatex -jobname=solution/%fn%_solution "\gdef\condition{1}\gdef\questionbank{%fn%_questions}\input base"
pdflatex -jobname=solution/%fn%_solution "\gdef\condition{1}\gdef\questionbank{%fn%_questions}\input base"