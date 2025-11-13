   Projektbeskriving
Hej! Jag heter Hamza och här är mitt projekt - en avancerad bolånekalkylator som hjälper dig att beräkna månadskostnader för bolån, renoveringskostnader och vinst/förlust vid försäljning av bostad.
# Skapa ett nytt virtuellt miljö
python3 -m venv venv

# Aktivera det virtuella miljön
# På macOS/Linux:
source venv/bin/activate

# På Windows:
# venv\Scripts\activate

# För att köra programmet "python main.py"
# För att köra tester "cd test" sen "pytest", "pytest -v"

   Syfte och Mål
Programmet är utformat för att ge bostadsköpare och säljare en tydlig översikt över alla kostnader och potentiell vinst i en bostadsaffär. Min vision är att utveckla detta till en fullskalig webbplats som lanseras sommaren 2026.

   Funktioner
   Användarsystem
Registrering - Skapa nytt konto med e-postverifiering

Inloggning - Säker inloggning med lösenord

Lösenordsändring - Möjlighet att uppdatera lösenord

Sessionshantering - Sparar användardata mellan sessioner

   Bolåneberäkning
Beräkna månadskostnad baserat på:

Lägenhetspris

Lånebelopp

Ränta (%)

Återbetalningstid (år)

   Renoveringskalkylator
Fördefinierade renoveringsalternativ:

Badrum: 70,000 kr

Kök: 130,000 kr

Målarfärg: 20,000 kr

Golv: 20,000 kr

Lister: 7,000 kr

Dörrar: 10,000 kr

Arbetskostnad: 80,000 kr

Övrigt: 30,000 kr

Möjlighet att ange egna kostnader

Automatisk beräkning av månadskostnadsökning

   Försäljningsanalys
Beräkna vinst/förlust

Totalöversikt av hela affären

Inkluderar alla kostnader

   Datalagring
Spara alla beräkningar per användare

Visa historik över tidigare affärer

JSON-baserad datalagring

   Teknisk Implementation
Klassstruktur
BolanApp - Huvudlogik
Hanterar alla beräkningar

Separerad logik från användargränssnitt

UserSystem - Användarhantering
Registrering och inloggning

Lösenordshanterring

E-postvalidering

Database - Datalagring
Spara och hämta användardata

Historik över beräkningar

Filbaserad lagring

   Installation och Körning
Förutsättningar
Python 3.6 eller högre

Ingen extra installation krävs

   Starta programmet

   Användning
Starta programmet - Välj att logga in eller skapa konto

Gör beräkning - Fyll i uppgifter om bostad och lån

Lägg till renovering - Välj från fördefinierade alternativ

Lägg till avgifter - Ange månadsavgift för bostaden

Analysera försäljning - Se potentiell vinst/förlust

Spara resultat - Spara beräkningen i din historik

   Felsökning och Utmaningar
Under utvecklingen stötte jag på flera utmaningar:

Bugg med datalagring
Problem: Programmet kraschade med felmeddelandet AttributeError: 'float' object has no attribute 'lägenhetspris'

Lösning: Efter timmar av felsökning visade det sig vara en bugg där Visual Studio Code cacheade gamla versioner av koden. En enkel omstart av datorn löste problemet!

Separering av logik och gränssnitt
Utmaning: Att separera beräkningslogik från användarinteraktion

Lösning: Skapade tydliga gränssnitt mellan klasser och flyttade all input/output till main.py

   Testning
Programmet inkluderar omfattande tester för att säkerställa kvalitet:

Enhetstester för alla klasser

Integrationstester för klassinteraktion

Edge cases och felhantering

Datalagringstester med temporära filer

   Framtida Utveckling
Planer för 2026 Lansering
Webbgränssnitt med React/Flask

Avancerad grafisk visualisering

Mobilanpassning

Integration med riktiga bankräntor

Bostadsmarknadsdata

Investeringsanalysverktyg

Skatteberäkningar

Export till PDF/Excel

Tekniska Förbättringar
Databassupport (SQLite/PostgreSQL)

API för integration med andra tjänster

Säkerhetsförbättringar (hashade lösenord)

Prestandaoptimering

   Utvecklingsprocess
Inspiration och Lärande
YouTube tutorials för Python-koncept

Skolans resurser på LearnPoint

Lärarstöd via digital kommunikation

Eget forskande och experimenterande

Tidsåtgång
Sena kvällar - ofta kodande till 03:00

Problemlösning - timmar av research och testing

Kontinuerlig förbättring - iterativ utveckling

  Tack
Ett stort tack till:

Min lärare för ovärderligt stöd och guidance

Klasskamrater för feedback och diskussioner

Python-communityt för omfattande resurser

"Varje bugg är en möjlighet att lära sig något nytt" - Hamza Fa

Kontakt: [Hamza.hf44@gmail.com]

Version: 1.0
Planerad lansering: Sommaren 2026