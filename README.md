## RR2020_SOCKETS

Projekti permbane gjithsej kater programe: **(1) TCPklienti.py, (2) TCPserver.py, (3) UDPklienti.py dhe (4) UDPserver.py.**
Te dy serveret, si TCPserveri ashtu edhe UDPserveri, jane dizajnuar dhe implementuar ne ate menyre qe te punojne pa nderprerje dhe te pranojne nje sekuence te kerkesave nga i njejti klient apo nga klient te ndryshem. Pra, te dy serveret e perkrahin punen me shume klienta (multithreading) njekohesisht dhe i perkrahin keto kerkesa (metoda):

- Metoda **IPADDRESS**, e cila kthen IP adresen e klientit p.sh. (10.10.7.251)
- Metoda **PORT**, e cila kthen portin e klientit
- Metoda **COUNT**, e cila pranon nje tekst ne forme stringu dhe kthen numrin e zanoreve e bashketingelloreve te atij teksti
- Metoda **REVERSE**, e cila pranon nje tekst ne forme stringu dhe ate tekst e kthen te permbysur
- Metoda **PALINDROME**, e cila pranon nje tekst ne forme stringu dhe tregon per ate tekst se a eshte palindrome apo jo
- Metoda **TIME**, e cila kthen kohen aktuale ne nje format te lexueshem per njerezit, ne formatin 12h
- Metoda **GAME**, e cila kthen nje liste te sortuar me karakter rrites prej 5 numrave te zgjedhur random nga bashkesia [1, 2, …, 35]4
- Metoda **GCF**, e cila si hyrje pranon 2 teskte te formatit int dhe e kthen faktorin me te madh te perbashket te atyre 2 numrave
- Metoda **CONVERT**, e cila pranon dy tekste, njeri I formatit string e tjetri I formatit float. Varesisht nga stringu qe pranon, kjo metode bene keto shnderrime: cmToFeet, FeetToCm, kmToMiles, MileToKm dhe kthen shnderrimin perkates.
- Metoda **BMI**, e cila pranon dy tekste te formatit float, gajtesine (m) dhe peshen (kg), dhe kthen BMI index-in dhe nje tekst qe tregon se sa i shendetshem jeni
- Metoda **PRIME_NUMBERS**, e cila pranon dy tekste te formatit int dhe kthen nje liste e cila permbane te gjithe numrat e thjeshte (prime) ndermjet atyre dy numrave.

Ndersa per tu shkycur nga serveri shenoni 'quit'.

Per te ekzekutuar programin, se pari behet duhet hapur file-n **TCPserver.py** (apo **UDPserver.py.**) ne menyre qe te startohet serveri dhe pastaj duhet hapur file-n **TCPklienti.py** (apo **UDPklienti.py**) te cilen mund ta bejme disa here radhazi ne menyre qe te lidhim disa klienta ne server.
