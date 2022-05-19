# Blacklist - Dig 

Projeto realizado para realizar a tradução dos domínios encontrados em black lists para IPS, facilitando assim a aplicação de regras de block.




Contexte
The Université Toulouse 1 Capitole propose a blacklist managed by Fabrice Prigent from many years, to help administrator to regulate Internet use. This database, often used in school, can be used with many commercial or free software.
Be careful : this list should not be seen as a "to be block". It must be seen as a "web categorization" : some categories can be blocked or allowed, depending on your environnement..
Licenses
Contrat Creative Commons
This creation is available under un Creative Commons Contract.
Description
Many categories are defined, but it's the main one is "pornography".
A archive file contain all category : blacklists.tar.gz
Category	Nmber	Description
adult	4413142	Some adult site from erotic to hard pornography.
arjel	69	ARJEL which is a french certification authority for gambling sites
associations_religieuses	1	religious_association
astrology	29	Astrology
audio-video	3568	Some audio and video sites.
bank	1845	Online bank
bitcoin	267	Sites for bitcoin mining
blog	1471	Some blogs sites.
celebrity	674	Famous people, actors, and magazine which talk about them
chat	243	Chat site
child	74	Any website allowed to child (less than 10 years old)
cleaning	173	Sites to disinfect, update and protect computers.
cooking	21	Sites for cooking
cryptojacking	14224	Mining site by hijacking
dangerous_material	49	Sites which describe how to make bomb and some dangerous material.
dating	3810	Dating, matching site for single person
ddos	421	DDoS or Stresser Sites
dialer	4	Dialer Sites
doh	89	Site which provides DNS over HTTP service
download	4019	Sites which propose to download software
drogue	1064	Sites relative to drugs.
educational_games	11	educational games sites (flash and online games )
examen_pix	276	A list reserved exclusively for French students taking the PIX exam. DO NOT USE in other circumstances
filehosting	896	Websites which host files (pictures, video, ...)
financial	84	Sites relative financial information.
forums	209	Forums site.
gambling	1326	Gambling and games sites, casino, etc.
games	11510	games sites (flash and online games )
hacking	304	Hacking sites.
jobsearch	386	Site to looking for job
lingerie	85	Sites for lingerie
liste_bu	2898	A french list for educational sites. VERY locally oriented. may help libraries.
malware	62529	Any website which deliver malware
manga	827	Any website related to manga, and cartoons
marketingware	33	Very special marketing sites
mixed_adult	153	Websites which contains adult sections unstructured
mobile-phone	50	Sites for mobile phone (rings, etc).
phishing	62799	Phishing sites (same as malware category)
press	4493	Any press (informational) site
publicite	4044	Advertisement.
radio	513	Internet radio sites
reaffected	8	Websites which have been reaffected
redirector	129669	Some redirector sites, which are used to circumvent filtering.
remote-control	48	site which allow remote control of user s dekstop
sect	144	Sect
sexual_education	19	Website which talk about sexual education, and can be misdetected as porn
shopping	36565	Any shopping, selling center
shortener	345	URLs shortening sites
social_networks	679	All social networks sites
sports	2292	Sports
stalkerware	22	Site which sells spying software for everybody
strict_redirector	129396	Same as redirector, but with google, yahoo, and other cache/images search robots.
strong_redirector	129396	Same as strict_redirector, but, for google, yahoo, we are only blocking some terms.
translation	178	Sites for translation
tricheur	46	Sites which are designed to explains cheating on exams.
update	6	Update sites for software or OS
vpn	1451	VPN site
warez	1174	Warez sites.
webmail	410	Webmail sites (hotmail like...)
These lists contain certainly some mistakes. If you find some, send me a mail : fabrice.prigent@ut-capitole.fr or you can use this interface https://dsi.ut-capitole.fr/cgi-bin/squidguard_modify.cgi.
How are these lists constituted
2 ways :
Contributors (See below), send modifications
Un spider crawl on Internet to find adult urls.
Database is renewed more or less, twice a week.
Contributors
This database exists because many contributors help :
Alban Caporossi
Alexandre Chevrier CSVT (for its contribution in games jeux)
www.app3l.org Association...
Barbagelata Pierre (MATICE - rectorat de Nice)
Benjamin E. Nichols http://www.squidblacklist.org
Benjamin Bellec
Cedric Foll (Now with much more responsability)
Charles COLLET
Christian ORNAGHI
David Garroux (CARIP de l'académie de Lyon)
Deckert Florian
Dilain Laurent
Eric Jansen (les sites de hosting)
Francesco Mascaro
Gotzon Astondoa, from http://www.wesify.com parental control app
Hervé Bienvenu
Hans Musil (German sites)
Henrique Araujo (Many spanish adult sites)
IAE pconline
Jago27
Jozef Skarba
Kris Carlier
Laura Corsaca
Marc Kool (7% came from him)
Marcos Manoni (Many spanish sites for adult, games and filehosting)
Mark Bizzell
Maxime Brunier(NITD)
Michel Roiron
Nicolas DELAMARRE NSI-ADMR (ADMR's information system dedicated enterprise)
Philippe Ferreira
Pierre Bardou du MiPih
Rick Matthews
Rogério Pinheiro da Silva
Sean Riley
Sylvain Vincent
Sylvain Poidras
Symon Aked
Stéphanie Chevtchenko
Société SOFIA Informatique
Todd Sieland-Peterson
Centre des Systèmes et Réseaux(Université Hassiba Benbouali CHLEF (Algeria))
Yann Cézard (CRI - Université de Pau et des Pays de l'Adour) (games)
Yann Guillemot
And many anonymous one
malware and marketingware
These bases are based on the work of :
the great https://www.abuse.ch/
malwarehunterteam http://cybertracker.malwarehunterteam.com
cybercrime-tracker team http://cybercrime-tracker.net
SAGA D.C. http://dns-bh.sagadc.org/
Malekal http://www.malekal.com/
the compilation of malware-domains : http://www.malware-domains.com
ANSSI http://www.ssi.gouv.fr
Local additions (mostly detected on honeypot, mail, virus, and so on);
Other database
Some database exist in other countries, but most of them have disappeared. Last ones :
http://www.squidblacklist.org/,
http://squidguard.mesd.k12.or.us/blacklists.tgz (mixed of bn-paf, our database and some local additions)
http://www.shallalist.de/ squidguard maintainers,
http://urlblacklist.com a commercial one.
