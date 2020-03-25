#! python 3
# This program: (1) Takes a list of students who are signed up for workshops, (2) Takes a list of all students in the school,
# (3) Produces a list of students who have not signed up, (4)

import random
import re

# compare students who signed up and students who didnt
Signed_Up = '''
aansha20@bergen.org
abihob22@bergen.org
adakuc22@bergen.org
adapio20@bergen.org
adrso23@bergen.org
aedcho23@bergen.org
aidhar21@bergen.org
aksmeh22@bergen.org
alabag23@bergen.org
alalew23@bergen.org
albcho21@bergen.org
alecal21@bergen.org
alenow@bergen.org
alepal21@bergen.org
alepap23@bergen.org
alepep23@bergen.org
aleruh21@bergen.org
alewan20@bergen.org
alivee21@bergen.org
allarc23@bergen.org
allfor20@bergen.org
alykang14-@gmail.com
amacon21@bergen.org
amadep20@bergen.org
amedej21@bergen.org
amylee23@gmail.com
anafon21@bergen.org
anddia23@bergen.org
anddra21@bergen.org
andfor21@bergen.org
angcar20@bergen.org
angcha23@bergen.org
angmej21@bergen.org
angpar23@bergen.org
angser22@bergen.org
anncar20@bergen.org
annhuh20@bergen.org
annswa23@bergen.org
anotan23@bergen.org
antale20@bergen.org
antcam21@bergen.org
antsaf21@bergen.org
antzha21@bergen.org
aprmul21@bergen.org
arjaje21@bergen.org
arlrod21@bergen.org
ashoha22@bergen.org
ashpar22@bergen.org
ashwal21@bergen.org
autper22@bergen.org
ayasno23@bergen.org
belelt22@gmail.com
bensyt21@bergen.org
beskur23@bergen.org
bijcho22@gmail.com
bilwan23@bergen.org
bragre20@bergen.org
brakan22@bergen.org
bralop21@bergen.org
bramik20@bergen.org
brason22@bergen.org
breser21@bergen.org
brihai21@bergen.org
brobai23@bergen.org
brusia23@bergen.org
cadsch22@bergen.org
cailan20@bergen.org
cambel22@bergen.org
campen22@bergen.org
cardun20@bergen.org
cathun20@bergen.org
catyam23@bergen.org
chabim21@bergen.org
chahan23@bergen.org
chaji21@bergen.org
chasoh23@bergen.org
chlkoo23@bergen.org
chlo'n23@bergen.org
chrarr21@bergen.org
chrlen23@bergen.org
chrsic22@bergen.org
chrtes20@bergen.org
clamer23@bergen.org
colchr22@bergen.org
colson20@bergen.org
conpar21@bergen.org
crinag23@bergen.org
danmal23@bergen.org
danper22@bergen.org
darlau20@bergen.org
darmol21@bergen.org
daschr23@bergen.org
dercha22@bergen.org
devrap20@bergen.org
diastr22@bergen.org
diefei22@bergen.org
domgen23@bergen.org
domhaj21@bergen.org
donfol21@bergen.org
doumcm21@bergen.org
edwgas22@bergen.org
edwlle22@bergen.org
edwpen22@bergen.org
efsnic21@bergen.org
eilkim20@bergen.org
elivil20@bergen.org
elizis23@bergen.org
ellfle23@bergen.org
ellkim22@bergen.org
emiche23@bergen.org
emigar23@bergen.org
emijac20@bergen.org
emikoz23@bergen.org
emivil20@bergen.org
emmbac21@bergen.org
emmmcd21@bergen.org
emmrey23@bergen.org
emmshe22@bergen.org
enrram22@bergen.org
eriyau23@bergen.org
estbur23@bergen.org
evariv21@bergen.org
evepie21@bergen.org
eyadav20@bergen.org
faimyi22@bergen.org
faishi21@bergen.org
fiocas21@bergen.org
fiogao21@bergen.org
fostie23@bergen.org
gabcar23@berge.org
gabgor22@bergen.org
gabswa23@bergen.org
gabthi22@bergen.org
galyak20@bergen.org
gehzab21@bergen.org
giameu22@bergen.org
giasmi22@bergen.org
gilson20@bergen.org
gissil21@bergen.org
grapar21@bergen.org
gyukim23@bergen.org
haekim23@bergen.org
hammah23@bergen.org
hanawa23@bergen.org
hugmar22@bergen.org
hunlou23@bergen.org
iankit20@bergen.org
inhna22@bergen.org
iripie23@bergen.org
isacor22@bergen.org
isamaz20@bergen.org
isaram21@bergen.org
isasan21@bergen.org
isayi20@bergen.org
jacalt22@bergen.org
jacdin20@bergen.org
jadco21@bergen.org
jadmck22@bergen.org
jakcac21@bergen.org
jandar21@bergen.org
janlim20@bergen.org
janpar22@bergen.org
jantec21@bergen.org
jasdel22@bergen.org
jasoha22@bergen.com
jasyu20@bergen.org
jeahan22@bergen.org
jenabr21@bergen.org
Jenbel21@bergen.org
jenkim20@bergen.org
jenmat22@bergen.org
jenpha20@bergen.org
jenxu21@bergen.org
jesogb23@bergen.org
jessha23@bergen.org
jeswil21@bergen.org
jiason21@bergen.org
jimsil23@bergen.org
jirdel23@bergen.org
jiycho21@bergen.org
jmazzer1023@gmail.com
jocgonz0419@gmail.com
johwsz22@bergen.org
joncho22@bergen.org
jondin23@bergen.org
jonrep23@bergen.org
jonwei20@bergen.org
jooshi21@bergen.org
jorzei21@bergen.org
josbar23@bergen.org
joscapu22@bergen.org
josdec20@bergen.org
josmat20@bergen.org
jossci20@bergen.org
Joswar22@bergen.org
joybot22@bergen.org
juldel23@bergen.org
julkin23@bergen.org
julnam23@bergen.org
julqui22@bergen.org
julsan20@bergen.org
julwal21@bergen.org
jundel23@bergen.org
jusjan22@bergen.org
jusmar22@bergen.org
justlee20@bergen.org
kaipos23@bergen.org
kateng21@bergen.org
katgon20@bergen.org
katmcc20@bergen.org
katpal20@bergen.org
kaybar22@bergen.org
kaycha23@bergen.org
kaylee23@bergen.org
kelrib23@bergen.org
kenche23@bergen.org
kentob23@bergen.org
keoroh21@bergen.org
kevjim21@bergen.org
kevmas23@bergen.org
kevshen23@bergen.org
kirmat20@bergen.org
kribay22@bergen.org
krijan22@bergen.org
kuskav23@bergen.org
kyukim22@bergen.org
laucar22@bergen.org
lawony20@bergen.org
leedan21@bergen.org
leoban22@bergen.org
leosha23@bergen.org
lesjae23@bergen.org
lexkes22@bergen.org
liario21@bergen.org
liashi23@bergen.org
lildre22@bergen.org
lilpat21@bergen.org
linahn23@bergen.org
linjle21@bergen.org
lisvas20@bergen.org
logrey20@bergen.org
lorwol20@bergen.org
lucmar21@bergen.org
lukwri23@bergen.org
lynyoo21@bergen.org
madkon22@bergen.org
madshi21@bergn.org
malism23@bergen.org
manpal23@bergen.org
marbou21@bergen.org
mardem21@bergen.org
marger21@bergen.org
marlaz23@bergen.org
marpal21@bergen.org
marpun22@bergen.org
marrey20@bergen.org
marrya23@bergen.org
marsca21@bergen.org
martou20@bergen.org
marven23@bergen.org
marzub21@bergen.org
masdou23@bergen.org
masgan21@bergen.org
matpad20@bergen.org
matsch23@bergen.org
maxada22@bergen.org
maydav20@bergen.org
maygos21@bergen.org
mckfly23@bergen.org
megsan23@bergen.org
mehkoh20@bergen.org
mehsaw21@bergen.org
merozg20@bergen.org
miabro21@bergen.org
miccho23@bergen.org
micgal20@bergen.org
micmar20@bergen.org
micmeg20@bergen.org
micmur21@bergen.org
mildel20@bergen.org
milpat23@bergen.org
moncza21@bergen.org
natcua22@bergen.org
natmaz22@bergen.org
natono22@bergen.org
natrob21@bergen.org
natsen22@bergen.org
naycho21@bergen.org
neibel22@bergen.org
ngasod23@bergen.org
nicsan22@bergen.org
niczha21@bergen.org
nikdia21@bergen.org
niksch22@bergen.org
noakim22@bergen.org
noasta23@bergen.org
norels21@bergen.org
ohnche21@bergen.org
okpoge20@bergen.org
olidra22@bergen.org
olipie20@bergen.org
oluola21@bergen.org
oluola23@bergen.org
paljai20@bergen.org
petbis22@bergen.org
phitsi23@bergen.org
pioles23@bergen.org
qansma22@bergen.org
queasa22@bergen.org
quease20@bergen.org
rahpat23@bergen.org
rayzha22@bergen.org
rebone20@bergen.org
reegue23@bergen.org
rhirue23@bergen.org
ridpat22@bergen.org
robkap22@bergen.org
ryajor21@bergen.org
sabedi21@bergen.org
sabfer20@bergen.org
samgomez20@icloud.com
samgri23@bergen.org
samsac21@bergen.org
samsal21@bergen.org
samsuh20@bergen.org
sankim20@bergen.org
sarels23@bergen.org
sarpar22@bergen.org
savell21@bergen.org
sebtor23@bergen.org
shacla20@bergen.org
shelop22@bergen.org
sheyi20@bergen.org
shrpat20@bergen.orh
shrsan20@bergen.org
siahan23@bergen.org
sidams21@bergen.org
siewie20@bergen.org
sofben23@bergen.org
sofdia23@bergen.org
sofdra23@bergen.org
sopfra22@bergen.org
sopsan23@bergen.org
sopsus21@bergen.org
steyoo21@bergen.org
sunpar20@bergen.org
suskim21@bergen.org
taaher22@bergen.org
takmor20@bergen.org
tander20@bergen.org
tanhan21@bergen.org
terdec23@bergen.org
thodeo23@bergen.org
tifper22@bergen.org
timhol20@bergen.org
tyligl23@bergen.org
vanbol23@bergen.org
verdol21@bergen.org
vicbed22@bergen.org
viccor21@bergen.org
vicsur23@bergen.org
vivchu20@bergen.org
walcha20@bergen.org
weijin22@bergen.org
weskim22@bergen.org
wikjur20@bergen.org
yanlea20@bergen.org
yasmah20@bergen.org
yhabar23@bergen.org
yoolee23@bergen.org
yoskak20@bergen.org
yunkwa21@bergen.org
Zahlat23@bergen.org'''

Signed_Up_List = Signed_Up.replace('\n',' , ').split(' , ') # Make a true list of these in python)


All_Students = '''
samabd21@bergen.org
jenabr21@bergen.org
maxada22@bergen.org
rohaga20@bergen.org
juaage22@bergen.org
linahn23@bergen.org
arjaje21@bergen.org
brialc21@bergen.org
antale20@bergen.org
jacalt22@bergen.org
wilalv20@bergen.org
sidams21@bergen.org
johann21@bergen.org
antant20@bergen.org
julara20@bergen.org
allarc23@bergen.org
chrarr21@bergen.org
queasa22@bergen.org
quease20@bergen.org
tamash22@bergen.org
isaasl23@bergen.org
adravi22@bergen.org
kerawa20@bergen.org
hanawa23@bergen.org
emmbac21@bergen.org
alabag23@bergen.org
brobai23@bergen.org
matbal22@bergen.org
emibal23@bergen.org
leoban22@bergen.org
benban22@bergen.org
henbaq22@bergen.org
josbar23@bergen.org
yhabar23@bergen.org
kaybar22@bergen.org
alebar22@bergen.org
kribay22@bergen.org
vicbed22@bergen.org
neibel22@bergen.org
jenbel21@bergen.org
cambel22@bergen.org
sofben23@bergen.org
alpber22@bergen.org
megber20@bergen.org
skybia22@bergen.org
patbie23@bergen.org
chabim21@bergen.org
petbis22@bergen.org
chabla20@bergen.org
patboh23@bergen.org
izabol23@bergen.org
vanbol23@bergen.org
micbon20@bergen.org
nevbon23@bergen.org
julbon23@bergen.org
joybot22@bergen.org
virbot22@bergen.org
marbou21@bergen.org
madbri22@bergen.org
miabro21@bergen.org
karbuc23@bergen.org
estbur23@bergen.org
macbur23@bergen.org
shabyj22@bergen.org
johbyr23@bergen.org
ethcab20@bergen.org
jakcac21@bergen.org
alicai20@bergen.org
alecal21@bergen.org
marcam23@bergen.org
antcam21@bergen.org
niccam23@bergen.org
concam23@bergen.org
joscapu22@bergen.org
lorcap20@bergen.org
gabcar23@bergen.org
anncar20@bergen.org
marcar22@bergen.org
leocar20@bergen.org
laucar22@bergen.org
angcar20@bergen.org
fiocas21@bergen.org
gabcast21@bergen.org
dercha22@bergen.org
kaycha23@bergen.org
angcha23@bergen.org
walcha20@bergen.org
ohnche21@bergen.org
emiche23@bergen.org
kenche23@bergen.org
jaecho23@bergen.org
joncho22@bergen.org
kevcho21@bergen.org
thocho22@bergen.org
aedcho23@bergen.org
albcho21@bergen.org
bijcho22@bergen.org
jiycho21@bergen.org
lyncho21@bergen.org
naycho21@bergen.org
miccho23@bergen.org
colchr22@bergen.org
daschr23@bergen.org
clachu22@bergen.org
kaichu21@bergen.org
vivchu20@bergen.org
shacla20@bergen.org
jadco21@bergen.org
trico23@bergen.org
amacon21@bergen.org
isacor22@bergen.org
davcor20@bergen.org
viccor21@bergen.org
thecos22@bergen.org
miccos22@bergen.org
kevcou20@bergen.org
natcua22@bergen.org
alicys22@bergen.org
kevcys20@bergen.org
moncza21@bergen.org
jacdin20@bergen.org
leedan21@bergen.org
jandar21@bergen.org
anddas21@bergen.org
eyadav20@bergen.org
maydav20@bergen.org
fradav23@bergen.org
josdec20@bergen.org
amedej21@bergen.org
amadep20@bergen.org
terdec23@bergen.org
jirdel23@bergen.org
jundel23@bergen.org
jasdel22@bergen.org
mildel20@bergen.org
juldel23@bergen.org
mardem21@bergen.org
thodeo23@bergen.org
tander20@bergen.org
nikdia21@bergen.org
sofdia23@bergen.org
anddia23@bergen.org
naddig20@bergen.org
nobdim22@bergen.org
jondin23@bergen.org
antdio21@bergen.org
verdol21@bergen.org
dandon22@bergen.org
masdou23@bergen.org
debdra22@bergen.org
sofdra23@bergen.org
anddra21@bergen.org
olidra22@bergen.org
lildre22@bergen.org
jeedso20@bergen.org
lukduf22@bergen.org
cardun20@bergen.org
amadur22@bergen.org
brydys20@bergen.org
danedi21@bergen.org
sabedi21@bergen.org
hrhelh22@bergen.org
savell21@bergen.org
norels21@bergen.org
sarels23@bergen.org
belelt22@bergen.org
kateng21@bergen.org
antfal20@bergen.org
emifal22@bergen.org
diefei22@bergen.org
amafel21@bergen.org
sabfer20@bergen.org
ryafer22@bergen.org
tylfer21@bergen.org
olufie22@bergen.org
amafis23@bergen.org
ellfle23@bergen.org
mckfly23@bergen.org
donfol21@bergen.org
anafon21@bergen.org
allfor20@bergen.org
andfor21@bergen.org
sopfra22@bergen.org
shafre22@bergen.org
sufgaj21@bergen.org
micgal20@bergen.org
masgan21@bergen.org
fiogao21@bergen.org
emigar23@bergen.org
thogar20@bergen.org
fragar20@bergen.org
edwgas22@bergen.org
antgas23@bergen.org
natgee20@bergen.org
dhagen23@bergen.org
domgen23@bergen.org
davgeo22@bergen.org
dylger22@bergen.org
marger21@bergen.org
donger21@bergen.org
dangia20@bergen.org
chegil20@bergen.org
malgil20@bergen.org
adegjo21@bergen.org
arigjo21@bergen.org
saigog22@bergen.org
johgom21@bergen.org
samgom22@bergen.org
katgon20@bergen.org
aidgon22@bergen.org
fabgon20@bergen.org
jocgon23@bergen.org
gabgor22@bergen.org
maygos21@bergen.org
jangra21@bergen.org
bragre20@bergen.org
nolgri22@bergen.org
samgri23@bergen.org
reegue23@bergen.org
micgui22@bergen.org
iangui22@bergen.org
jongul22@bergen.org
jacgun23@bergen.org
sedguv21@bergen.org
brihai21@bergen.org
domhaj21@bergen.org
chahan23@bergen.org
jeahan22@bergen.org
siahan23@bergen.org
brohan21@bergen.org
tanhan21@bergen.org
aidhar21@bergen.org
chrher20@bergen.org
jamher22@bergen.org
nather20@bergen.org
taaher22@bergen.org
melhit20@bergen.org
abihob22@bergen.org
timhol20@bergen.org
annhuh20@bergen.org
cathun20@bergen.org
danhwa23@bergen.org
tyligl23@bergen.org
malism23@bergen.org
eseiti22@bergen.org
chrjac23@bergen.org
emijac20@bergen.org
lesjae23@bergen.org
abdjag20@bergen.org
abdujag20@bergen.org
paljai20@bergen.org
krijan22@bergen.org
tyljan22@bergen.org
jusjan22@bergen.org
wyajan23@bergen.org
samjaw20@bergen.org
hanji21@bergen.org
jesji20@bergen.org
chaji21@bergen.org
kevjim21@bergen.org
weijin22@bergen.org
linjle21@bergen.org
brijon21@bergen.org
ryajor21@bergen.org
paujun21@bergen.org
wikjur20@bergen.org
katkaga20@bergen.org
yoskak20@bergen.org
dapkal20@bergen.org
alykan22@bergen.org
brakan22@bergen.org
klakap22@bergen.org
robkap22@bergen.org
natkar20@bergen.org
kuskav23@bergen.org
endkel20@bergen.org
lexkes22@bergen.org
norkha20@bergen.org
daskim21@bergen.org
eilkim20@bergen.org
ellkim22@bergen.org
erikim21@bergen.org
gyukim23@bergen.org
haekim23@bergen.org
hyukim21@bergen.org
jenkim20@bergen.org
jerkim20@bergen.org
kyukim22@bergen.org
laurkim21@bergen.org
noakim22@bergen.org
sankim20@bergen.org
sarkim20@bergen.org
suskim21@bergen.org
weskim22@bergen.org
adakin21@bergen.org
julkin23@bergen.org
valkis20@bergen.org
iankit20@bergen.org
mehkoh20@bergen.org
madkon22@bergen.org
chlkoo23@bergen.org
harkot22@bergen.org
kaikoz21@bergen.org
emikoz23@bergen.org
matkuc21@bergen.org
adakuc22@bergen.org
kinkur23@bergen.org
beskur23@bergen.org
yunkwa21@bergen.org
alelan20@bergen.org
cailan20@bergen.org
zahlat23@bergen.org
darlau20@bergen.org
marlaz23@bergen.org
yanlea20@bergen.org
antlec20@bergen.org
amylee23@bergen.org
donlee20@bergen.org
elllee21@bergen.org
jaclee21@bergen.org
joslee20@bergen.org
justlee20@bergen.org
kaylee23@bergen.org
keblee23@bergen.org
roblee21@bergen.org
yoolee23@bergen.org
chrlen23@bergen.org
nicles23@bergen.org
pioles23@bergen.org
konles21@bergen.org
alalew23@bergen.org
jaclew22@bergen.org
janlim20@bergen.org
andlio22@bergen.org
danlio21@bergen.org
edwlle22@bergen.org
bralop21@bergen.org
shelop22@bergen.org
hunlou23@bergen.org
krilul23@bergen.org
alemac20@bergen.org
vermac22@bergen.org
oscmad21@bergen.org
brimad20@bergen.org
gabmae21@bergen.org
hammah23@bergen.org
yasmah20@bergen.org
danmal23@bergen.org
andman23@bergen.org
matmar22@bergen.org
hugmar22@bergen.org
alemari21@bergen.org
lucmar21@bergen.org
marmar20@bergen.org
danmar22@bergen.org
jusmar22@bergen.org
micmar20@bergen.org
sanmar20@bergen.org
kevmas23@bergen.org
josmat20@bergen.org
hammat23@bergen.org
jenmat22@bergen.org
kirmat20@bergen.org
isamaz20@bergen.org
madmaz23@bergen.org
natmaz22@bergen.org
julmaz20@bergen.org
katmcc20@bergen.org
emmmcd21@bergen.org
animcd23@bergen.org
lyrmck21@bergen.org
jadmck22@bergen.org
doumam21@bergen.org
micmeg20@bergen.org
aksmeh22@bergen.org
angmej21@bergen.org
ashmej22@bergen.org
lukmel23@bergen.org
decmel23@bergen.org
olimem20@bergen.org
davmen22@bergen.org
clamer23@bergen.org
brimes23@bergen.org
sofmes20@bergen.org
giameu22@bergen.org
bramik20@bergen.org
ivymit20@bergen.org
tarmod22@bergen.org
darmol21@bergen.org
halmor21@bergen.org
takmor20@bergen.org
brimor20@bergen.org
zacmos23@bergen.org
hasmul23@bergen.org
aprmul21@bergen.org
jonmul23@bergen.org
micmur21@bergen.org
faimyi22@bergen.org
inhna22@bergen.org
crinag23@bergen.org
julnam23@bergen.org
dannes23@bergen.org
efsnic21@bergen.org
yoonoh23@bergen.org
alenow23@bergen.org
ashoha22@bergen.org
jasoha22@bergen.org
chlone23@bergen.org
rebone20@bergen.org
jamosu21@bergen.org
graoet23@bergen.org
jesogb23@bergen.org
okpoge20@bergen.org
oluola21@bergen.org
oluola23@bergen.org
halolu20@bergen.org
natono22@bergen.org
lawony20@bergen.org
jacosp20@bergen.org
penowi20@bergen.org
merozg20@bergen.org
matpad20@bergen.org
marpal21@bergen.org
katpal20@bergen.org
manpal23@bergen.org
miapal22@bergen.org
alepal21@bergen.org
nicpan22@bergen.org
eftpap23@bergen.org
ellpap22@bergen.org
alepap23@bergen.org
jaypar20@bergen.org
angpar23@bergen.org
ashpar22@bergen.org
chrpar20@bergen.org
conpar21@bergen.org
grapar21@bergen.org
janpar22@bergen.org
juspar22@bergen.org
kylpar21@bergen.org
sarpar22@bergen.org
sunpar20@bergen.org
devpat21@bergen.org
lilpat21@bergen.org
milpat23@bergen.org
rahpat23@bergen.org
ridpat22@bergen.org
shrpat20@bergen.org
linpau22@bergen.org
aydpav22@bergen.org
naypeg20@bergen.org
campen22@bergen.org
edwpen22@bergen.org
kiapen23@bergen.org
alepep23@bergen.org
lilper20@bergen.org
autper22@bergen.org
danper22@bergen.org
tifper22@bergen.org
micpha22@bergen.org
jenpha20@bergen.org
evepie21@bergen.org
iripie23@bergen.org
isapie23@bergen.org
olipie20@bergen.org
sebpin21@bergen.org
adapio20@bergen.org
scopiz22@bergen.org
julpol20@bergen.org
hunpor23@bergen.org
kaipos23@bergen.org
jaypou20@bergen.org
ruspow22@bergen.org
frapuc22@bergen.org
marpun22@bergen.org
brypur23@bergen.org
julqui22@bergen.org
amiram20@bergen.org
enrram22@bergen.org
isaram21@bergen.org
rezreh23@bergen.org
noeren22@bergen.org
jonrep23@bergen.org
charev20@bergen.org
logrey20@bergen.org
emmrey23@bergen.org
marrey20@bergen.org
calrhe23@bergen.org
kelrib23@bergen.org
liario21@bergen.org
evariv21@bergen.org
samriv20@bergen.org
angrob22@bergen.org
natrob21@bergen.org
jadrob20@bergen.org
emmroc21@bergen.org
katroc21@bergen.org
arlrod21@bergen.org
julrod20@bergen.org
keoroh21@bergen.org
aerroj20@bergen.org
tanroj23@bergen.org
erirol21@bergen.org
jorrom22@bergen.org
lanroz21@bergen.org
nicroz21@bergen.org
rhirue23@bergen.org
samrug23@bergen.org
aleruh21@bergen.org
danrus23@bergen.org
marrya23@bergen.org
samsac21@bergen.org
antsaf21@bergen.org
seasal20@bergen.org
samsal21@bergen.org
alesan23@bergen.org
crysan20@bergen.org
nicsan22@bergen.org
sopsan23@bergen.org
devrap20@bergen.org
shrsan20@bergen.org
aprsan20@bergen.org
alesan20@bergen.org
samsan23@bergen.org
adisan23@bergen.org
isasan21@bergen.org
julsan20@bergen.org
megsan23@bergen.org
sopsan22@bergen.org
macsaq22@bergen.org
dansar21@bergen.org
mehsaw21@bergen.org
alesca22@bergen.org
marsca21@bergen.org
nevsch20@bergen.org
niksch22@bergen.org
cadsch22@bergen.org
thosch22@bergen.org
matsch23@bergen.org
jossci20@bergen.org
chrsel22@bergen.org
natsen22@bergen.org
adasen22@bergen.org
tylsen22@bergen.org
josseo23@bergen.org
angser22@bergen.org
breser21@bergen.org
aansha20@bergen.org
johsha20@bergen.org
jessha23@bergen.org
hibshaq20@bergen.org
leosha23@bergen.org
emmshe22@bergen.org
kevshen23@bergen.org
faishi21@bergen.org
jooshi21@bergen.org
liashi23@bergen.org
madshi21@bergen.org
kensho20@bergen.org
davshv23@bergen.org
brusia23@bergen.org
chrsic22@bergen.org
gissil21@bergen.org
jensil22@bergen.org
jimsil23@bergen.org
jassin23@bergen.org
mansin23@bergen.org
isasir20@bergen.org
qansma22@bergen.org
pausme20@bergen.org
giasmi22@bergen.org
sebsmi21@bergen.org
ayasno23@bergen.org
adrso23@bergen.org
ngasod23@bergen.org
chasoh23@bergen.org
olisoh22@bergen.org
davsol23@bergen.org
brason22@bergen.org
jiason21@bergen.org
colson20@bergen.org
danson20@bergen.org
gilson20@bergen.org
haeson21@bergen.org
jussou23@bergen.org
bryspa21@bergen.org
noasta23@bergen.org
diastr22@bergen.org
lausua20@bergen.org
samsuh20@bergen.org
vicsur23@bergen.org
sopsus21@bergen.org
gabswa23@bergen.org
annswa23@bergen.org
bensyt21@bergen.org
klaszm20@bergen.org
luktag20@bergen.org
anotan23@bergen.org
vintan22@bergen.org
isatav23@bergen.org
skytay23@bergen.org
jantec21@bergen.org
emitel20@bergen.org
chrtes20@bergen.org
alitha22@bergen.org
gabthi22@bergen.org
fostie23@bergen.org
kentob23@bergen.org
sebtor23@bergen.org
gabtor20@bergen.org
martou20@bergen.org
suhtoz20@bergen.org
tartoz22@bergen.org
pratri20@bergen.org
phitsi23@bergen.org
nattua23@bergen.org
bentur20@bergen.org
kanued22@bergen.org
andval20@bergen.org
felval20@bergen.org
alivar20@bergen.org
damvas22@bergen.org
lisvas20@bergen.org
alivee21@bergen.org
marven23@bergen.org
jorven22@bergen.org
emivil20@bergen.org
elivil20@bergen.org
vivvis22@bergen.org
ornvuk20@bergen.org
julwal21@bergen.org
ashwal21@bergen.org
alewan20@bergen.org
bilwan23@bergen.org
joswar22@bergen.org
jonwei20@bergen.org
chawes22@bergen.org
siewie20@bergen.org
aidwig21@bergen.org
jeswil21@bergen.org
calwil22@bergen.org
lorwol20@bergen.org
lukwri23@bergen.org
johwsz22@bergen.org
jenxu21@bergen.org
galyak20@bergen.org
ivayak23@bergen.org
catyam23@bergen.org
eriyau23@bergen.org
gokyer21@bergen.org
isayi20@bergen.org
isayi21@bergen.org
samyi20@bergen.org
sheyi20@bergen.org
chlyim23@bergen.org
lynyoo21@bergen.org
steyoo21@bergen.org
jasyu20@bergen.org
gehzab21@bergen.org
adazak21@bergen.org
jorzei21@bergen.org
antzha21@bergen.org
niczha21@bergen.org
rayzha22@bergen.org
elizis23@bergen.org
marzub21@bergen.org
'''

All_Students_List = All_Students.replace('\n',' , ').split(' , ') # Get a true list of all students

Not_Signed_Up_List = list(set(All_Students_List).difference(Signed_Up_List)) # Creates a list of all students who haven't signed up




# Assign students who didn't sign up to sessions

IDT_Sessions = ['Mass Incarceration','Example Session','Gratitidue is the Attitude', 'Another One','Session B', 'Session C'] # Sample sessions (will change every year)

def Assigner(student): # My attempt to randomly assign students such that there are no repeat sessions for them
    Tracker = []
    IDT_Pick_Block1 = random.choice(IDT_Sessions)
    IDT_Session_1 = '1 - ' + str(IDT_Pick_Block1)
    Tracker.append(student)
    Tracker.append(IDT_Session_1)

    IDT_Pick_Block2 = random.choice(IDT_Sessions)
    while IDT_Pick_Block1 == IDT_Pick_Block2:
        IDT_Pick_Block2 = random.choice(IDT_Sessions)
        continue
    IDT_Session_2 = '2 - ' + str(IDT_Pick_Block2)
    Tracker.append(IDT_Session_2)

    IDT_Pick_Block3 = random.choice(IDT_Sessions)
    while IDT_Pick_Block3 == IDT_Pick_Block2 or IDT_Pick_Block3 == IDT_Pick_Block1:
        IDT_Pick_Block3 = random.choice(IDT_Sessions)
        continue
    IDT_Session_3 = '3 - ' + str(IDT_Pick_Block3)
    Tracker.append(IDT_Session_3)


    IDT_Pick_Block4 = random.choice(IDT_Sessions)
    while IDT_Pick_Block4 == IDT_Pick_Block3 or IDT_Pick_Block4 == IDT_Pick_Block2 or IDT_Pick_Block4 == IDT_Pick_Block1:
        IDT_Pick_Block4 = random.choice(IDT_Sessions)
        continue
    IDT_Session_4 = '4 - ' + str(IDT_Pick_Block4)
    Tracker.append(IDT_Session_4)
    print(Tracker)

Final = []

for i in range(0,len(Not_Signed_Up_List)): # This is the crude part that I can't get yet.
    Final.append(Assigner(Not_Signed_Up_List[i]))






