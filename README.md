<H1> BLACK LIST DIG </H1>

This project can be used to facilitate downloading and DIG (Dig (Domain Information Groper) is a command line that performs DNS lookup for nameserver queries and shows the result to you.)


For this, we use the blacklists of the site: http://dsi.ut-capitol.fr


<H2>How to download lists with download.sh script </H2>
<div>
<PRE>
./download.sh [categorie]
## all available categories will be available in Description
</PRE>

<H2>Using the DIG script to perform domain translation </H2>
<div>
<PRE>
##this script will translate the domains into IP addresses and create a file for one of the categories.
./dig.py 

example: [adult]-result 
</PRE>


















<H2>Contexte</H2>
<div>
The Université Toulouse 1 Capitole propose a blacklist managed by
 <A HREF="mailto:fabrice.prigent@ut-capitole.fr">Fabrice Prigent</A> from many years, to help
administrator to regulate Internet use.
This database, often used in school, can be used with many commercial or free software.
</div>
<div>
Be careful : this list should not be seen as a "to be block". It must be seen as a "web categorization" : some categories can be blocked or allowed, depending on your environnement..
</div>
<H2>Licenses</H2>
<!-- Contrat Creative Commons -->
">Creative Commons Contract</a>.</div>
<!-- /Contrat Creative Commons -->


<!--

<rdf:RDF xmlns="http://web.resource.org/cc/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<Work rdf:about="">
   <license rdf:resource="http://creativecommons.org/licenses/by-nc-sa/4.0/en/" />
</Work>

<License rdf:about="http://creativecommons.org/licenses/by-nc-sa/4.0/en/">
   <permits rdf:resource="http://web.resource.org/cc/Reproduction" />
   <permits rdf:resource="http://web.resource.org/cc/Distribution" />
   <requires rdf:resource="http://web.resource.org/cc/Notice" />
   <requires rdf:resource="http://web.resource.org/cc/Attribution" />
   <prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" />
   <permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" />
   <requires rdf:resource="http://web.resource.org/cc/ShareAlike" />
</License>

</rdf:RDF>

-->
<H2>Description</H2>
	<div>
	Many categories are defined, but it's the main one is "pornography".
	</div>
	<div>
	We are actively working on the adult database, but you can help me with the others one.
	</div>
	<div>I add between 50 and 300 urls per day.
	</div>
	<div>A archive file contain all category :
	<A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/blacklists.tar.gz">blacklists.tar.gz</A>
	</div>
	<div>
		<table>
<th>Category</th><th>Number</th><th>Description</th>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/adult.tar.gz">adult</A></td><td align=right><A HREF="adult.png">4415761
 </A></td><td>Some adult site from erotic to hard pornography.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/agressif.tar.gz">agressif</A></td><td align=right><A HREF="agressif.png">387
 </A></td><td>Some aggressive sites.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/arjel.tar.gz">arjel</A></td><td align=right><A HREF="arjel.png">69
 </A></td><td>ARJEL which is a french certification authority for gambling sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/associations_religieuses.tar.gz">associations_religieuses</A></td><td align=right><A HREF="associations_religieuses.png">1
 </A></td><td>religious_association</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/astrology.tar.gz">astrology</A></td><td align=right><A HREF="astrology.png">29
 </A></td><td>Astrology</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/audio-video.tar.gz">audio-video</A></td><td align=right><A HREF="audio-video.png">3568
 </A></td><td>Some audio and video sites.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/bank.tar.gz">bank</A></td><td align=right><A HREF="bank.png">1845
 </A></td><td>Online bank</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/bitcoin.tar.gz">bitcoin</A></td><td align=right><A HREF="bitcoin.png">267
 </A></td><td>Sites for bitcoin mining</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/blog.tar.gz">blog</A></td><td align=right><A HREF="blog.png">1471
 </A></td><td>Some blogs sites.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/celebrity.tar.gz">celebrity</A></td><td align=right><A HREF="celebrity.png">674
 </A></td><td>Famous people, actors, and magazine which talk about them</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/chat.tar.gz">chat</A></td><td align=right><A HREF="chat.png">243
 </A></td><td>Chat site</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/child.tar.gz">child</A></td><td align=right><A HREF="child.png">74
 </A></td><td>Any website allowed to child (less than 10 years old)</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/cleaning.tar.gz">cleaning</A></td><td align=right><A HREF="cleaning.png">173
 </A></td><td>Sites to disinfect, update and protect computers.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/cooking.tar.gz">cooking</A></td><td align=right><A HREF="cooking.png">21
 </A></td><td>Sites for cooking</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/cryptojacking.tar.gz">cryptojacking</A></td><td align=right><A HREF="cryptojacking.png">14224
 </A></td><td>Mining site by hijacking</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/dangerous_material.tar.gz">dangerous_material</A></td><td align=right><A HREF="dangerous_material.png">49
 </A></td><td>Sites which describe how to make bomb and some dangerous material.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/dating.tar.gz">dating</A></td><td align=right><A HREF="dating.png">3810
 </A></td><td>Dating, matching site for single person</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/ddos.tar.gz">ddos</A></td><td align=right><A HREF="ddos.png">421
 </A></td><td>DDoS or Stresser Sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/dialer.tar.gz">dialer</A></td><td align=right><A HREF="dialer.png">4
 </A></td><td>Dialer Sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/doh.tar.gz">doh</A></td><td align=right><A HREF="doh.png">89
 </A></td><td>Site which provides DNS over HTTP service</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/download.tar.gz">download</A></td><td align=right><A HREF="download.png">4019
 </A></td><td>Sites which propose to download software</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/drogue.tar.gz">drogue</A></td><td align=right><A HREF="drogue.png">1064
 </A></td><td>Sites relative to drugs.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/educational_games.tar.gz">educational_games</A></td><td align=right><A HREF="educational_games.png">11
 </A></td><td>educational games sites (flash and online games )</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/examen_pix.tar.gz">examen_pix</A></td><td align=right><A HREF="examen_pix.png">276
 </A></td><td>A list reserved exclusively for French students taking the PIX exam. DO NOT USE in other circumstances</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/filehosting.tar.gz">filehosting</A></td><td align=right><A HREF="filehosting.png">896
 </A></td><td>Websites which host files (pictures, video, ...)</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/financial.tar.gz">financial</A></td><td align=right><A HREF="financial.png">84
 </A></td><td>Sites relative financial information.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/forums.tar.gz">forums</A></td><td align=right><A HREF="forums.png">209
 </A></td><td>Forums site.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/gambling.tar.gz">gambling</A></td><td align=right><A HREF="gambling.png">1326
 </A></td><td>Gambling and games sites, casino, etc.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/games.tar.gz">games</A></td><td align=right><A HREF="games.png">11510
 </A></td><td>games sites (flash and online games )</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/hacking.tar.gz">hacking</A></td><td align=right><A HREF="hacking.png">304
 </A></td><td>Hacking sites.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/jobsearch.tar.gz">jobsearch</A></td><td align=right><A HREF="jobsearch.png">386
 </A></td><td>Site to looking for job</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/lingerie.tar.gz">lingerie</A></td><td align=right><A HREF="lingerie.png">85
 </A></td><td>Sites for lingerie</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/liste_bu.tar.gz">liste_bu</A></td><td align=right><A HREF="liste_bu.png">2898
 </A></td><td>A french list for educational sites. VERY locally oriented. may help libraries.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/malware.tar.gz">malware</A></td><td align=right><A HREF="malware.png">62629
 </A></td><td>Any website which deliver malware</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/manga.tar.gz">manga</A></td><td align=right><A HREF="manga.png">827
 </A></td><td>Any website related to manga, and cartoons</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/marketingware.tar.gz">marketingware</A></td><td align=right><A HREF="marketingware.png">33
 </A></td><td>Very special marketing sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/mixed_adult.tar.gz">mixed_adult</A></td><td align=right><A HREF="mixed_adult.png">153
 </A></td><td>Websites which contains adult sections unstructured</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/mobile-phone.tar.gz">mobile-phone</A></td><td align=right><A HREF="mobile-phone.png">50
 </A></td><td>Sites for mobile phone (rings, etc).</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/phishing.tar.gz">phishing</A></td><td align=right><A HREF="phishing.png">62509
 </A></td><td>Phishing sites (same as malware category)</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/press.tar.gz">press</A></td><td align=right><A HREF="press.png">4493
 </A></td><td>Any press (informational) site</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/publicite.tar.gz">publicite</A></td><td align=right><A HREF="publicite.png">4044
 </A></td><td>Advertisement.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/radio.tar.gz">radio</A></td><td align=right><A HREF="radio.png">513
 </A></td><td>Internet radio sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/reaffected.tar.gz">reaffected</A></td><td align=right><A HREF="reaffected.png">8
 </A></td><td>Websites which have been reaffected</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/redirector.tar.gz">redirector</A></td><td align=right><A HREF="redirector.png">129669
 </A></td><td>Some redirector sites, which are used to circumvent filtering.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/remote-control.tar.gz">remote-control</A></td><td align=right><A HREF="remote-control.png">48
 </A></td><td>site which allow remote control of user s dekstop</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/sect.tar.gz">sect</A></td><td align=right><A HREF="sect.png">144
 </A></td><td>Sect</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/sexual_education.tar.gz">sexual_education</A></td><td align=right><A HREF="sexual_education.png">19
 </A></td><td>Website which talk about sexual education, and can be misdetected as porn</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/shopping.tar.gz">shopping</A></td><td align=right><A HREF="shopping.png">36565
 </A></td><td>Any shopping, selling center</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/shortener.tar.gz">shortener</A></td><td align=right><A HREF="shortener.png">345
 </A></td><td>URLs shortening sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/social_networks.tar.gz">social_networks</A></td><td align=right><A HREF="social_networks.png">679
 </A></td><td>All social networks sites</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/sports.tar.gz">sports</A></td><td align=right><A HREF="sports.png">2292
 </A></td><td>Sports</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/stalkerware.tar.gz">stalkerware</A></td><td align=right><A HREF="stalkerware.png">22
 </A></td><td>Site which sells spying software for everybody</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/strict_redirector.tar.gz">strict_redirector</A></td><td align=right><A HREF="strict_redirector.png">129397
 </A></td><td>Same as redirector, but with google, yahoo, and other cache/images search robots.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/strong_redirector.tar.gz">strong_redirector</A></td><td align=right><A HREF="strong_redirector.png">129397
 </A></td><td>Same as strict_redirector, but, for google, yahoo, we are only blocking some terms.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/translation.tar.gz">translation</A></td><td align=right><A HREF="translation.png">178
 </A></td><td>Sites for translation</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/tricheur.tar.gz">tricheur</A></td><td align=right><A HREF="tricheur.png">46
 </A></td><td>Sites which are designed to explains cheating on exams.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/update.tar.gz">update</A></td><td align=right><A HREF="update.png">6
 </A></td><td>Update sites for software or OS</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/vpn.tar.gz">vpn</A></td><td align=right><A HREF="vpn.png">1451
 </A></td><td>VPN site</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/warez.tar.gz">warez</A></td><td align=right><A HREF="warez.png">1174
 </A></td><td>Warez sites.</td></tr>
<tr><td><A HREF="ftp://ftp.ut-capitole.fr/pub/reseau/cache/squidguard_contrib/webmail.tar.gz">webmail</A></td><td align=right><A HREF="webmail.png">410
 </A></td><td>Webmail sites (hotmail like...)</td></tr>
</table>
	</div>
	<div>
	These lists contain certainly some mistakes. If you find some, send me a mail : 
		<A HREF="mailto:fabrice.prigent@ut-capitole.fr">fabrice.prigent@ut-capitole.fr</A> or you can use
		this interface

		<A HREF="/cgi-bin/squidguard_modify.cgi">https://dsi.ut-capitole.fr/cgi-bin/squidguard_modify.cgi</A>.<BR>
	</div>
<H2>How are these lists constituted</H2>
<div>
2 ways :
<UL>
<LI> Contributors (See below), send modifications
<LI> Un spider crawl on Internet to find adult urls.
</UL>
Database is renewed more or less, twice a week. 
</div>

<H3>Contributors</H3>
<div>
	This database exists because many contributors help :
	<UL>
	<LI>Alban Caporossi
	<LI>Alexandre Chevrier CSVT (for its contribution in games jeux)
        <LI><A HREF="http://www.app3l.org">www.app3l.org</A> Association...
	<LI>Barbagelata Pierre (MATICE - rectorat de Nice)
	<LI>Benjamin E. Nichols <A HREF="http://www.squidblacklist.org">http://www.squidblacklist.org</A>
	<LI>Benjamin Bellec
	<LI>Cedric Foll (Now with much more responsability)
	<LI>Charles COLLET
	<LI>Christian ORNAGHI
	<LI>David Garroux (CARIP de l'acad&eacute;mie de Lyon)
	<LI>Deckert Florian
	<LI>Dilain Laurent
	<LI>Eric Jansen (les sites de hosting)
	<LI>Francesco Mascaro
        <LI>Gotzon Astondoa, from <A HREF="http://www.wefisy.com">http://www.wesify.com</A> parental control app
	<LI>Herv&eacute; Bienvenu
	<LI>Hans Musil (German sites)
	<LI>Henrique Araujo (Many spanish adult sites)
	<LI>IAE pconline
	<LI>Jago27
	<LI>Jozef Skarba
	<LI>Kris Carlier
	<LI>Laura Corsaca
	<LI>Marc Kool (7% came from him)
	<LI>Marcos Manoni (Many spanish sites for adult, games and filehosting)
	<LI>Mark Bizzell
	<LI>Maxime Brunier(NITD)
	<LI>Michel Roiron
	<LI>Nicolas DELAMARRE NSI-ADMR (ADMR's information system dedicated enterprise)
	<LI>Philippe Ferreira
	<LI>Pierre Bardou du MiPih
	<LI>Rick Matthews
	<LI>Rog&eacute;rio Pinheiro da Silva
	<LI>Sean Riley
	<LI>Sylvain Vincent
	<LI>Sylvain Poidras
	<LI>Symon Aked
	<LI>St&eacute;phanie Chevtchenko
	<LI>Soci&eacute;t&eacute; SOFIA Informatique
	<LI>Todd Sieland-Peterson
	<LI>Centre des Syst&egrave;mes et R&eacute;seaux(Université Hassiba Benbouali CHLEF (Algeria))
	<LI>Yann Cézard (CRI - Université de Pau et des Pays de l'Adour) (games)
	<LI>Yann Guillemot
	<LI>
	<LI>And many anonymous one
</UL>
</div>
<H3>malware and marketingware</H3>
These bases are based on the work of :
        <UL>
        <LI>the great  <A HREF="https://www.abuse.ch/">https://www.abuse.ch/</A>
        <LI>malwarehunterteam <A HREF="http://cybertracker.malwarehunterteam.com">http://cybertracker.malwarehunterteam.com</A>
        <LI>cybercrime-tracker team <A HREF="http://cybercrime-tracker.net">http://cybercrime-tracker.net</A>
        <LI>SAGA D.C. <A HREF="http://dns-bh.sagadc.org/">http://dns-bh.sagadc.org/</A>
        <LI>Malekal <A HREF="http://www.malekal.com/">http://www.malekal.com/</A>
        <LI>the compilation of malware-domains : <A HREF="http://www.malware-domains.com">http://www.malware-domains.com</A>
        <LI>ANSSI <A HREF="http://www.ssi.gouv.fr">http://www.ssi.gouv.fr</A>
        <LI>Local additions (mostly detected on honeypot, mail, virus, and so on);
        </UL>

<H3>Other database</H3>
	<div>
	Some database exist in other countries, but most of them have disappeared. Last ones :
		<UL>
		<LI><A HREF="http://www.squidblacklist.org/">http://www.squidblacklist.org/</A>,
		<LI><A HREF="http://squidguard.mesd.k12.or.us/blacklists.tgz ">http://squidguard.mesd.k12.or.us/blacklists.tgz </A> (mixed of bn-paf, our database and some local additions)
                <LI><A HREF="http://www.shallalist.de/">http://www.shallalist.de/</A> squidguard maintainers,
                <LI><A HREF="http://urlblacklist.com">http://urlblacklist.com</A> a commercial one.
		</UL>
	</div>
	


</div>
<div id="footer">Université Toulouse 1 Capitole</div>
<!--
Date de modification du fichier :mardi 15 f�vrier 2022
-->
<!--    Ceci est le Pied de Page        -->
