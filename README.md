# NaN-Final-version

Til þess að keyra forrit opnaðu "main.py" og keyrir þaðan
Fyrir nýja notendur er gott að horfa á youtube myndbandið hér fyrir neðan
Linkur inn á youtube video: https://www.youtube.com/watch?v=dql70rQoYCg

Kóðinn er í 5 möppum
möppurnar innihalda eftirfarandi:

allt sem tengist gagnagrunninum er í data möppunni
allir módelklasar eru í model möppunni
csv filearnir eru í files möppunni
allt tengt UI er í ui möppunni
forritið er síðan keyrt í main.py fileinu


code structure:

data
    -crew_data
    -destination_data
    -flight_data
    -voyage_data
    -data_wrapper

files
    -crew.csv
    -destinations.csv
    -flights.csv
    -voyages.csv

logic
    -destination_logic
    -employee_logic
    -flight_logic
    -schedule_logic
    -voyage_logic
    -logic_wrapper

models
    -fligt
    -crew
    -destination
    -voyage

ui
    -destinaion_ui
    -employee_ui
    -flight_ui
    -main_menu
    -schedules_ui
    -voyage_ui

main - the code runs in this file

