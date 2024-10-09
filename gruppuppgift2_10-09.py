# Gruppdikusion: i slutuppgiften kan det bli aktuellt att hantera fel. 
# Vilka typ av fel kan bli aktuellt att hantera i den? Tänk t.ex. på vad som kan hända med:
# Användarinput, När man försöker skapa larm, När man försöker spara eller läsa en fil (för VG nivå)

#SVAR: Allt som tar in input. 

#TILLS PÅ MÅNDAG (14/10): Addera felhantering på de ställen i din slutuppgift där du anser att det passar.
# Hantera eventuella fel genom att t.ex fånga dem och skriv ut till användaren vad som gått fel.
#Du kan även lägga till funktionalitet vid din felhantering. 
# T.ex. Att du går tillbaka till huvudmenyn eller liknande.

#LÄS PÅ OM: Git, branching, scripting(python), CI/CD.
#1. GitFlow som metodik för att arbeta med Git.
#2. Hur man kan anropa Git från ett python script!

#DAGENS UPPGIFT: Skriv ett kort pythonscript som klonar ner ett repo, skapar en branch och pushar den branchen till repot.
#Kräver: import subprocess
#Tips: använd subprocess.run() för att exekvera gitkommandon.

import subprocess

print('hello world')
process = subprocess.Popen("git status")
