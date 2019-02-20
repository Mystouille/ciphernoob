#!/usr/bin/python3.5
import unicodedata

charOffset = 97
baseOffset = 8

words=[
"jdkkzevyzokzzfvrmdgwpygnppqccuevpe",
"vzckdnkriqugkmuyvbtrhugezdgpmggszykadzg",
"gatqmqgfooqemqeg",
"vojrmapcjeuryqwazhtndqlhhqnyz",
"hmpbvfjcmugtjxibotc"]
#from POs text
keysInput = ["abandonner","absence","absorbe","abysses","accepter","accompagnent","accoster","accoucha","Acheron","acte","active","actives","activiste","actuellement","adeptes","adversaires","affaires","affichee","affiliations","affranchi","afin","Agamendi","agapes","agathes","age","agent","agents","agile","agreable","Agua","ai","aide","aigle","aiguisee","ainsi","Ainsi","aisance","aisement","ait","Alceste","Aleistar","alentours","aliene","alimente","allait","alors","Alxh","Alxhariales","amenes","amertume","ames","ami","amis","an","Anaxete","Anaxetes","Anaxibie","ancestral","Anchor","ancien","ancienne","anciennement","anciens","anglaises","animee","annees","ans","apparaissait","apparait","apparament","apparence","appartements","appartenance","apparu","apparue","appel","appeler","appelerait","appelle","appellent","apprendre","apprirent","apprit","approprie","appropriee","apres","Apres","Aquila","arbore","arcanique","arcaniques","arcanotellurique","archer","Arcturus","argente","Arial","ariales","arme","armee","armees","armes","armure","arraches","Arraches","arrange","arrangement","arranger","arrive","arrivee","arriver","arriverent","art","artisans","artistes","artistique","aspirais","aspirant","assassin","assassinat","assassine","assemblee","attachement","attaquer","atteignit","atteindre","atteint","attendait","attendit","attentats","attention","attirer","au","Au","aubaine","aucune","auraient","auraisje","aurait","Aurora","aurpes","aussi","Autarcia","Autarcien","auteur","autochtones","autonomie","autorite","autre","autrefois","autres","aux","avaient","avait","avant","avec","aventure","aveux","avidite","avoir","avons","avouer","Bahamuth","baignade","banniere","Banshee","Barash","barman","basfonds","basse","basses","batiments","baton","beaucoup","Behemoth","Bella","belliqueux","benie","bercee","bete","Bharash","bibliotheque","bicephale","bien","Bien","biens","bientot","blason","bleu","blonde","Bogdan","bon","bonheur","bonne","bouclier","bougre","bousculant","bousculerent","bout","bras","bretteur","brise","brunes","brusque","brutal","brutalement","brutaux","butin","c","C","cache","cacher","cacophonie","cadeau","cadence","calamiteux","calcul","calculateur","Caleb","calme","camp","campagne","campagnes","capable","capacite","capitaine","capital","capitale","capturee","car","Car","carte","cas","caste","cause","causes","ce","Ce","ceci","Ceci","ceder","cela","Cela","celebre","celle","celleci","celui","celuici","censure","centre","Cependant","cerf","certain","certains","Certains","ces","Ces","cesse","cest","Cest","cet","cetait","cette","ceux","chacun","chaine","champs","chandelier","changement","changer","chaos","chaotique","chapitre","Chapitre","chaque","charmantes","chaude","chef","Cher","cherchait","cherchant","cherche","Cherche","cherchent","chercher","chercheur","chetif","chevalier","Chevalier","chevaliers","Chevaliers","chevauchees","chez","choir","choisi","chose","choses","cicatrices","ciel","cimeterre","Circonsciption","circonstances","clair","clan","clandestinite","clans","Clara","Claudia","cle","clignotait","close","code","coeur","coffre","coffrefort","cois","colere","colerique","collines","colonialisation","colonies","colonisation","colonne","colons","combat","combattant","combattre","comme","Comme","commencaient","commencer","commencerent","commerce","commettre","commun","communication","communications","compagnie","compagnons","compense","comperes","completement","complexe","Compose","composee","composes","Comprenant","compte","comptine","concentre","concerne","concis","conclave","conclavela","conclurent","conclusion","conduite","confiance","confirma","conflits","connais","connaissait","connaissance","connaitre","connectee","connu","connues","conquete","conscient","consentit","consequences","conservateurs","considera","considerations","consommer","constamment","constater","constituait","constituees","constitution","construction","contact","conter","contestent","contexte","contiendrait","continent","continuait","continuer","contourna","contraires","contre","contreoperations","conversation","convoiter","convoque","cooperer","copiant","copie","copier","copiste","coquelicots","coquillage","Corinthus","corps","cote","couche","coule","coupable","couper","cour","courageusement","courbes","cousin","coute","couteaux","couverture","cracher","crains","creation","creatrices","creature","creatures","creer","crepuscule","Crest","cri","croyait","Crucis","cruel","culte","culturels","cynisme","d","dabord","dAgamendi","dagressivite","dailleurs","daller","dame","danger","dannee","dans","dapporter","dapprendre","Dapres","dArcturus","darmure","darreter","daucun","daussi","dautre","davantage","davoir","de","De","deborde","debuter","debuts","decent","dechainee","decheance","dechirerent","decida","deciderent","decision","decisions","declara","declare","declares","decollerent","decombres","deconcertante","decoudre","decoupant","decouvert","decouvrait","decouvrir","decouvriras","decroit","defaut","defection","defforts","defiance","defunte","deguise","degusta","dehors","deite","deja","delicate","delicatesse","delire","delite","delle","demanda","demandant","demande","demi","demoiselle","demonstration","demonta","demontrer","den","denergie","denonciation","denseignements","dentre","dents","depourvu","depuis","derivees","dernier","derniers","des","Des","desaccords","descend","descendant","desequilibrer","designait","desireux","desorganisee","Desorganises","desormais","Dessence","destabilisant","destin","destinant","detail","detailler","details","dete","determiner","detranges","detre","detres","deux","Deux","deuxieme","devaient","devait","devant","devoirs","devraint","devras","dexception","dexfiltrer","dexterite","dhonneur","dieu","dieux","difference","differend","different","difficilement","diluer","dimension","dimensions","dinformations","dinvestiguer","dire","directement","dirigent","disait","discipline","discordant","discutables","disent","disons","disparaitre","disparu","disparus","dispensait","dispose","dissensions","distingue","dit","dite","divine","divinites","division","dizaine","Djinns","dOctave","document","documents","dois","domination","don","donc","donnaient","donnant","donne","dont","dorigine","dormeur","dote","double","doubler","douce","douleur","doute","doutre","doyen","draconide","draconnide","dragon","druide","du","duel","dun","dune","durant","dutiliser","dynastie","dYswetch","eau","Eau","ebranle","ecarlate","ecartee","echange","echappa","echauffe","echauffoures","echos","echoue","economie","ecrase","ecris","ecrits","effectuer","effet","effort","egalement","egard","elan","elements","elevee","elevent","eleves","Elianh","elite","elle","Elle","elles","Elles","ellesmemes","eme","Emergerent","eminent","emmener","emoussant","empeche","empereur","empire","emplacement","empoisonnement","en","En","encerclaient","enchaine","encore","endroits","endurance","endurant","enervees","enfants","enfin","Enfin","enjoindrais","enjoint","ennemis","ennivre","enqueter","ensorceleuse","ensuite","entend","entendait","entende","Entendre","entendu","entente","entites","entouree","entre","entrer","entretient","envahies","environs","envoya","envoye","Eodeth","ephemeres","epoque","equilibrees","equipes","equivalent","Ermeth","erudit","esclavage","esoteristes","esperant","EsperDjinns","Espers","esprit","essaye","essence","essences","essentielles","essuye","est","estce","estiment","et","Et","etabli","etablie","etablir","etaient","etait","etant","etat","ete","Ether","etoiles","etou","etouffer","etranger","etre","etreint","etres","etroites","etymologique","eu","eut","eux","evenements","eventuelles","evidemment","eviter","evoque","exacte","exactement","exactions","excelle","exfiltrer","expliqua","expliquant","exploitee","explosee","exterieurs","extraction","extremement","extremites","facon","faiblesse","faire","faisait","fait","famille","farouchement","fatale","fauchees","faudra","Faune","faux","faveur","feconde","feconderaient","feminin","feminine","femme","fermant","fete","feu","Feu","fiable","fille","fils","fin","finalement","financer","financier","finir","finira","finirait","finirent","finit","firent","fit","fleches","fleur","fleurs","fleuve","Flore","florissante","flot","floues","fois","fondamentales","fondateurs","fonde","font","force","forces","foret","forets","forme","fort","Fort","Foudre","fouille","foule","fourbes","fracas","frere","froide","fuir","furent","fusionnes","fut","fuyaient","gain","gamin","garcon","garde","Garde","gardes","gaussa","gay","geant","general","generale","generalement","generent","genous","gens","gestes","gestuelle","glace","Gladius","glaive","glauque","glisser","globale","globalement","gnome","gonfla","gorge","grace","graisse","grand","grande","grandes","grandit","grands","grassement","griffes","groupe","groupes","guerre","guet","guettent","guilde","habitants","habite","hache","hagarde","hargneux","harmonieuse","haut","haute","hautes","herbe","heritage","herite","heros","hetre","heure","heureusement","heurter","histoire","homme","hommes","honneur","honora","honteusement","hors","hotel","houspillant","humains","humeur","ici","Ici","ideal","identifie","ignorant","ignore","ignorer","II","il","Il","ile","illegalement","illisible","illustre","ils","Ils","imaginer","immediatement","immense","imminente","imperiale","imperiales","imperialiste","impitoyable","importantes","impossible","imprevisible","impunite","incarnant","incarnation","incendie","incendier","incertaine","inciter","inconnu","inconnue","inconnus","incontournable","incroyablement","inculquer","indic","indomptables","ineluctablement","inepuisable","inevitable","infiltre","infini","influence","information","informations","ingorait","inlassablement","innombrables","inquisition","insistance","inspection","intarissable","intellect","intellectuelle","intellectuels","intense","interpella","interpelle","interrompu","intimidants","Introductif","investigations","inviolable","iodee","Ircisses","ironiquement","j","J","jai","jamais","je","Je","Jebeddo","jeu","jeune","jeux","joint","jolie","jouait","jouer","joues","joueur","jour","journal","jours","Julius","jure","jusqualors","KanKis","Kinlan","l","L","la","La","lac","laffaire","laigle","laissa","laissaient","laissant","laissemoi","lalcool","lallegeant","laller","lamantin","Lamantin","lame","lames","lance","lancees","lancer","lancier","langoureuse","lappartement","lappelant","lappellation","laquelle","larcherie","lardeur","large","larmee","larrivee","laspect","lassassin","lastroport","laube","lautre","le","Le","leau","lecole","lecon","Lecrit","legende","legere","legerement","legitimite","lempereur","lempire","lemprise","lendemain","lendroit","lentement","lenvie","lenvoyer","Leopoldine","lequel","les","Les","lethal","lettre","leur","leurs","Leurs","lexistence","lexterieur","lharmonie","lhomme","lhonneur","liaison","liaisons","liberation","lideal","lidentite","lie","liees","lien","lieu","ligne","lignes","lile","Limminence","limprevisible","lincarnation","linconsistant","lindic","linsistance","linsouciant","liqueur","lirastu","litteralement","livre","livrogne","local","localise","loeuvre","loin","lointain","longtemps","longue","longues","lopportunite","loppression","loquace","LordOhn","loriginal","lorigine","lors","lorsque","Lorsque","lorsquil","louche","loyaute","lui","luimeme","lumiere","lun","Lun","lune","lusage","lutilise","m","ma","macabres","mage","magie","main","mains","maintenant","Maintenant","mais","Mais","maison","maitre","maitres","maitrise","majoritairement","mal","maladie","malchance","malfames","malformation","malgre","Malgre","malignes","malveillantes","manege","maniant","manie","maniere","manifesta","manifeste","manipule","ManOath","manoir","manque","mante","Mante","mantes","Manus","marchande","marchands","marche","mariage","masculin","masculinesfeminins","masculins","massacre","masses","me","mediocrite","meilleur","melanger","mele","melopee","membre","Membre","membres","meme","mene","menees","meneur","mentionner","menus","meprise","mer","meritent","mes","mesure","mettre","meurent","meurtrier","meut","milice","milieu","militaires","millenaires","miraclesquot","mirent","mis","mise","misere","moi","moins","mois","moment","mon","monde","Mondek","monstre","monta","montagnes","montrait","montre","montrer","morale","morceau","mort","mortalite","motif","moults","mourir","mourrant","mouvement","Mouvement","mouvements","moyen","moyens","mues","muni","mur","murement","murmure","murmures","musique","Myrok","mysterieuse","mystiques","mythologie","n","na","Na","nage","naissent","nait","naquirent","naquit","natif","nature","naturellement","navait","ne","neant","necessaire","necessairement","necessite","necoutant","nen","netait","netant","neufs","Neufs","neurent","neut","neutralise","neuves","neveu","nexistera","ni","Ni","Nihili","noble","nobles","Nobles","noccasionne","noires","nom","nombre","nombreuses","nombreux","nommee","nommes","noms","non","nonchalante","nos","Nos","nostalgie","notre","nous","Nous","nouveau","nouveaux","nues","nul","ny","objectifs","obliger","observait","observatoire","occasion","Occasion","occulter","oceans","Octave","octroierait","officie","officiel","officiellement","Officiellement","Officieusement","Olbakihim","omis","on","On","oncle","Oncle","ont","operations","Ophichius","Ophicius","oppose","oppression","originaire","originellement","origines","Orir","Orix","orne","orque","ose","ou","oublie","oui","outrance","outrevie","ouvertement","ouvriere","ouvriers","ouvrir","pairs","papillon","par","parcourir","pareil","parfaite","parfois","parfum","parjure","parlait","parmi","parole","paroles","paroxysme","parrain","part","parti","participer","particulier","particuliere","particulierement","partie","partis","partitions","parviendra","pas","passage","passe","passer","passerent","passionne","passions","pauvre","pauvres","pauvrete","payaient","payer","peche","pegre","peine","pendant","Pendant","pensante","pense","pensent","penser","perdit","perdre","perdue","perdurait","peripeties","permanent","permettait","permit","personne","personnel","personnelle","personnellement","personnes","personnifiees","perspicacite","pertinente","peste","petit","petite","Petitfils","peu","peut","peutetre","Peutetre","peux","phenomenes","philosophe","physique","physiquement","pieces","pied","pieds","pierre","Pierre","piete","pins","pis","pisteur","place","plait","plan","planete","planque","planter","plaques","plates","pleine","pleureur","plonger","plume","plumes","plus","plusieurs","plutot","poete","poignards","poings","point","points","poitrine","politique","politiquement","politiques","populaire","populaires","population","populations","portait","porte","porteparole","porter","possede","Possede","poubelle","poumons","pour","Pour","pourraisje","pourrait","pourtant","Pourtant","pousse","pouvait","pouvoir","pouvoirs","pratique","precieux","precis","prefere","preferent","prefererent","premier","premiere","premiers","prenaient","prenait","prend","prendre","preparait","pres","present","presenter","pression","Prestance","presume","preta","preter","pretexte","pretresses","prevenant","pria","priait","primales","principale","principalement","prisonniers","probabiliste","probable","probablement","probleme","proche","produire","professeur","profita","profonde","profondeurs","promesse","prophete","proposa","proposer","propre","prositution","Prosopia","prospere","protection","prouva","provenant","providence","provinces","prudemment","prudent","pu","publique","puis","Puis","puiser","puisque","Puisque","puisquil","puissance","puissances","puissant","puissent","pulmonaire","pulsion","pur","pure","purent","purge","put","qi","qu","quabsence","qualite","quand","Quand","quant","Quant","Quarion","quartier","quartiers","quasiment","quatre","quauparavant","que","Que","quelle","quelles","quelqu","quelque","quelques","question","questionner","quete","qui","quietude","quil","quils","quitter","quOctave","quoi","quon","quorganisait","quOrir","quotchasse","quotla","quotsainte","quun","quune","racines","Radius","raffinee","raffinement","rageur","Ragnar","Rai","raid","raids","Raids","raison","rallier","ramener","rang","rangs","rapidement","rappele","rapport","rapprocher","rare","rassemble","rauque","ravages","ravisa","ravitaillement","Raya","RayaPrestance","Rayen","Rayenne","rebondir","recemment","recente","recherches","rechignent","recompense","recompenses","reconquerir","recrue","recrutee","recrutement","reculees","recuperation","recupere","recuperer","reduites","reellement","reflechi","reflexion","refus","regard","regarder","regret","Rei","reitere","rejoindre","rejoint","rejoints","remarqua","remarquant","rempli","renaissant","rencontrer","rend","rendait","rendant","rendent","rendezvous","rendirent","rendre","rends","renouveau","repere","repliquer","repondit","repondre","reponse","repose","reposent","reprere","representent","reputation","repute","reside","resonnant","resonner","respectueux","ressentirent","ressources","restaient","restait","reste","restent","rester","retour","retractile","retrouver","retrouverent","revee","reveille","Rhenan","Rhenans","Rhennane","riche","rien","rigoureuse","rigoureusement","rigueur","rire","risque","rivalise","rivaux","riviere","robe","Rodomanciens","role","romantique","rongees","rossignol","rouge","rouges","rp","RP","rumeur","rumeurs","rupture","s","sa","Sa","sacrifices","sage","sagesse","sainte","Sainte","saintetrinite","sais","saisons","salle","salon","samusait","sang","sanimer","sans","sanspouvoir","sapercoive","sappellait","sappelle","sapprocha","sapprochant","Sapprochant","sapprocher","sarcasme","sattirerent","saule","sauvages","savera","savoir","scientifiques","scission","Scuta","Scythe","se","seclipse","second","seconde","secondes","secret","secte","seductions","seigneur","sein","seloignant","selon","semblables","semblait","semble","Semble","semblent","senchevetrer","sent","sentait","sentent","sentit","separatiste","separer","separes","sept","septieme","sera","seraient","serieusement","serode","service","servir","ses","Ses","sesquisserent","setablissant","seul","seule","seulement","Seuls","seurent","sexe","sherisse","si","Si","siege","sifflement","signe","Sil","silence","silencieuse","simple","sinteresser","sinterrompit","Sire","situation","situe","sixieme","Slynath","societe","soctroyer","soeurs","soiree","soirs","soldaient","soldats","solde","sollicite","sombres","sommes","sommets","son","Son","sont","sorcellerie","sorcieresquot","sororite","Sortant","sortir","soudainement","souffrance","souleves","source","Source","sous","souseduquee","soutenir","soutien","soutirer","souvent","souverain","statue","stopper","strident","substantiel","subtilite","suggerer","suite","suivait","suivi","sujet","supplementaire","suppose","supposement","sur","surement","surprenant","surprise","surtout","surveiller","suspectes","suspsicion","sy","symphonie","Symphonie","synthetique","systeme","t","tableau","tactique","taille","taire","talent","talents","tandis","tant","Tant","tantot","Tantot","tard","tatouages","taupe","taverne","te","telles","telluriques","temoin","temperer","tempete","temps","tenant","tendent","tenebres","tentait","tentative","tentatives","tente","tenter","termina","termine","ternir","terrain","terre","Terre","terres","terribles","terrifie","terroriste","tete","tetre","texte","Thessalie","tiens","tient","timidement","tire","titan","titres","toilettes","toimeme","tombe","torrents","torture","touchable","touche","toucher","toujours","tour","tous","tout","toute","toutes","trace","tractant","traditionnelles","traditions","traffic","trafic","trahison","traitres","transforma","transformait","travaillait","travers","traversees","Tremans","tres","Tres","tressaillements","tribales","tribaux","tribu","tribus","tribut","tributs","tricephale","tricpehale","trinite","Trinite","trinitemante","trinitequot","trois","troisieme","trompa","trop","trouble","troubles","trouvaient","trouvait","Trouvant","trouve","trouver","trouverent","tu","Tu","tue","tuer","tumulte","typhons","un","Un","une","Une","unes","unique","uniquement","uns","urgent","us","use","utiles","utilise","utilite","va","vague","vais","vaisseau","valu","vaporise","variation","vegetation","venait","vendre","venimeuse","Vent","vents","verra","verre","vertebrale","vetements","veut","vibre","victime","victimes","Vide","vie","vierge","vieux","ville","vingt","violemment","violente","visiblement","Visiblement","vision","vivace","vivait","vive","vivre","voient","Voila","voir","voisine","voix","vol","vole","voler","volonte","voulait","voulu","voyages","voyageur","voyait","vraiment","vrais","vraisemblablement","vu","vue","y","yeux","zone"]
keysDic = {}
keys = []
#obvious ones
oviousKeys = ["eodeth", "kinlan","mondek","demnok","lannik","kinlanmondek","demnoklannik","myrok"]

#extend or crop a key depending on the word we wanna decrypt
def getResizedKey(baseKey,word):
	key = baseKey
	while len(key)< len(word):
		key.extend(key)
	key = key[:len(word)]
	return key



def main():
	log = {}
	totalKeys = len(keys)
	index = 0
	keys3=["neuf"]
	oldProgress = 0
	for key in keys3:
		index+=1
		progress = int(round(index*100/totalKeys))
		if progress!=oldProgress:
			print(str(progress)+"% : "+key)
			oldProgress=progress
		for word in words:
			decrypted = pretty(vigenere(dirty(key),dirty(word),1,True))
			#try to detect a french word of size 5 to 8 in the decrypted word
			#if foud, log it to memory
			log[decrypted] = key
			#print(decrypted+"\tk:"+key)
			found = True


	#dump search log into a file
	f = open("out.txt","w+")
	for key, value in log.items():
		f.write(key+"\tk: "+value+"\n")
	f.close()
