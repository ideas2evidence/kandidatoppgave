
### Kandidatoppgave i2e

En viktig del av ideas2evidence sin virksomhet er å samle inn data fra forskjellige kilder ved hjelp av web-undersøkelse. Ideas2evidence har blant annet gjennomført en rekke befolkningsundersøkelser til bruk i forskning. Les mer om våre prosjekter <a href="https://ideas2evidence.com/nb/kvantitativ-datainnsamling-tjeneste/" target="_blank">her</a>.

Like viktig for alle undersøkelser, og særlig undersøkelser som samler inn data til forskning, er god og detaljert variabeldokumentasjon. Derfor legger ideas2evidence stor vekt på å ha gode verktøy som produserer dokumentasjon av høy kvalitet på en forutsigbar og effektiv måte.

I `/resources` finner du en [XML-spesifikasjon](resources/p828932869599.xml) hentet fra vårt surveysystem. XML-filen inneholder eksempler på typiske spørsmålsstillinger, men merk at [dataene](resources/p828932869599.xlsx) er generiske. Det er laget eksempler i [Python](parse_xml.py) og [R](parse_xml.R) for hvordan deler av informasjonen fra XML-filen kan leses. 

Oppgavene er som følger: 

1. Ved å bruke Excel-filen, velg to av oppgavene under: 
    - Bruk kode til å identifisere kolonner som inneholder tekst.
    - Bruk kode til å identifisere den tekststrengen på tvers av alle tekst-variabler med flest antall tegn.
    - Lag en tabell som viser gjennomsnittsverdier for alle numeriske variabler med mer enn 10 observasjoner.  
2. Bruk [Python](parse_xml.py) eller [R](parse_xml.R)-skript som utgangspunkt. I skriptene finner du kode som henter og printer informasjon fra XML-filen. Gjør om koden og lag hensiktsmessige datastrukturer for å systematisere dokumentasjonen slik at du enkelt kan hente dokumentasjon fra enkeltspørsmål. Du trenger ikke hente ytterligere dokumentasjon fra XML-filen.
3. Ut fra arbeidet i oppgave 2 og Excel-filen, identifiser sentrale forskjeller mellom spørsmålstypene (Single, Grid, Open, osv). Lag deretter en frekvenstabell for to forskjellige typer spørsmål, som også inkluderer dokumentasjon fra oppgave 2.
4. Skriv noen avsnitt om følgende: Hvordan kan dokumentasjonen best tilgjengeliggjøres og presenteres for sluttbruker (ekstern og/eller kollega), og hvilke nyttige verktøy/applikasjoner kan utvikles basert på XML-filen og datagrunnlaget?  

Du velger selv hvordan du ønsker å presentere arbeidet, men vi mottar gjerne koden du har skrevet. Du kan selv velge om du vil bruke R eller Python.

##### Datasettet
I datasettet er det inkludert enkelte systemvariabler som ikke er spesifisert i XML-filen. Det gjelder `responseid`, `respid`, `status`, `interview_start`, `interview_end`, `last_touched` og `lastcomplete`.


