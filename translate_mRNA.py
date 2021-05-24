# Make a program that translates mRNA into protein
# It should report the longest ORF in each mRNA
# Make sure you translate all 3 reading frames on both strands
# It should use argparse and your library, of course


#1. make reverse compliment
#2. look for orfs and keep track of longest one
#3. translate the longest orf

import argparse
import mcb185

parser = argparse.ArgumentParser(description='translate RNAs to proteins')
parser.add_argument('--fasta', required = True, type = str, metavar='<str>', 
	help = 'fasta file needed')
arg = parser.parse_args()

fasta = {}
antifasta = {}	
for name, seq in mcb185.read_fasta(arg.fasta):
	fasta[name] = seq #make dictionary of fasta sequences
	antifasta[name] = mcb185.anti(seq) #makes dictionary of revcomp

for name, seq in fasta.items():
	fasta[name] = mcb185.longestorf(seq) #changes value to longest orf

for name, seq in antifasta.items():
	antifasta[name] = mcb185.longestorf(seq) #changes value to longest orf

for name, seq in fasta.items():
	if len(fasta[name]) > len(antifasta[name]):
		print(f'>{name}')
		print(mcb185.translate(seq))
	else:
		sequence = antifasta[name]
		print(f'>{name}')
		print(mcb185.translate(sequence))
		
"""
python3 translate_mRNA.py --fasta hs_rna.fa
>NM_001368885.1
MVAERTHKAAATGARGPGELGAPGTVALVAARAERGARLPSPGSCGLLTLALCSLALSLLAHFRTAELQARVLRLEAERG
EQQMETAILGRVNQLLDEKWKLHSRRRREAPKTSPGCNCPPGPPGPTGRPGLPGVKGQPGEKGSPGDAGLSIIGPRGPPG
QPGTRGFPGFPGPIGLDGKPGHPGPKGDMGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGE
QSQASIQGPPGPPGPPGPSGPLGHPGLPGPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGM
KGEPGIPGTKGEKGAEGSPGLPGLLGQKGEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGA
AGEQGPDGPKGSKGEPGKGEMVDYNGNINEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPR
GKPGDMGPPGPQGPPGKDGPPGVKGENGHPGSPGEKGEKGETGQAGSPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGP
LGLPGTPGPIGVPGPAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGE
DGLPVQGCWNK
>NM_001368886.1
MGLTGPPGQPGPQGQKGEKGQCGEYPHRLLPLLNSVRLAPPPVIKRRTFQGEQSQASIQGPPGPPGPPGPSGPLGHPGLP
GPMGPPGLPGPPGPKGDPGIQGYHGRKGERGMPGMPGKHGAKGAPGIAVAGMKGEPGIPGTKGEKGAEGSPGLPGLLGQK
GEKGDAGNSIGGGRGEPGPPGLPGPPGPKGEAGVDGQVGPPGQPGDKGERGAAGEQGPDGPKGSKGEPGKGEMVDYNGNI
NEALQEIRTLALMGPPGLPGQIGPPGAPGIPGQKGEIGLPGPPGHDGEKGPRGKPGDMGPPGPQGPPGKDGPPGVKGENG
HPGSPGEKGEKGETGQAGSPVPGLPGPEGPPGPPGLQGVPGPKGEAGLDGAKGEKGFQGEKGDRGPLGLPGTPGPIGVPG
PAGPKGERGSKGDPGMTGPTGAAGLPGLHGPPGDKGNRGHRGFKGEKGEPGLPGLDGLDAPCPLGEDGLPVQGCWNK
>NR_148047.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_148053.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NM_001374457.1
MSTPDPPLGGTPRPGPSPGPGPSPGAMLGPSPGPSPGSAHSMMGPSPGPPSAGHPIPTQGPGGYPQDNMHQMHKPMESMH
EKGMSDDPRYNQMKGMGMRSGGHAGMGPPPSPMDQHSQGYPSPLGGSEHASSPVPASGPSSGPQMSSGPGGAPLDGADPQ
ALGQQNRGPTPFNQNQLHQLRAQIMAYKMLARGQPLPDHLQMAVQGKRPMPGMQQQMPTLPPPSVSATGPGPGPGPGPGP
GPGPAPPNYSRPHGMGGPNMPPPGPSGVPPGMPGQPPGGPPKPWPEGPMANAAAPTSTPQKLIPPQPTGRPSPAPPAVPP
AASPVMPPQTQSPGQPAQPAPMVPLHQKQSRITPIQKPRGLDPVEILQEREYRLQARIAHRIQELENLPGSLAGDLRTKA
TIELKALRLLNFQRQLRQEVVVCMRRDTALETALNAKAYKRSKRQSLREARITEKLEKQQKIEQERKRRQKHQEYLNSIL
QHAKDFKEYHRSVTGKIQKLTKAVATYHANTEREQKKENERIEKERMRRLMAEDEEGYRKLIDQKKDKRLAYLLQQTDEY
VANLTELVRQHKAAQVAKEKKKKKKKKKAENAEGQTPAIGPDGEPLDETSQMSDLPVKVIHVESGKILTGTDAPKAGQLE
AWLEMNPGYEVAPRSDSEESGSEEEEEEEEEEQPQAAQPPTLPVEEKKKIPDPDSDDVSEVDARHIIENAKQDVDDEYGV
SQALARGLQSYYAVAHAVTERVDKQSALMVNGVLKQYQIKGLEWLVSLYNNNLNGILADEMGLGKTIQTIALITYLMEHK
RINGPFLIIVPLSTLSNWAYEFDKWAPSVVKVSYKGSPAARRAFVPQLRSGKFNVLLTTYEYIIKDKHILAKIRWKYMIV
DEGHRMKNHHCKLTQVLNTHYVAPRRLLLTGTPLQNKLPELWALLNFLLPTIFKSCSTFEQWFNAPFAMTGEKVDLNEEE
TILIIRRLHKVLRPFLLRRLKKEVEAQLPEKVEYVIKCDMSALQRVLYRHMQAKGVLLTDGSEKDKKGKGGTKTLMNTIM
QLRKICNHPYMFQHIEESFSEHLGFTGGIVQGLDLYRASGKFELLDRILPKLRATNHKVLLFCQMTSLMTIMEDYFAYRG
FKYLRLDGTTKAEDRGMLLKTFNEPGSEYFIFLLSTRAGGLGLNLQSADTVIIFDSDWNPHQDLQAQDRAHRIGQQNEVR
VLRLCTVNSVEEKILAAAKYKLNVDQKVIQAGMFDQKSSSHERRAFLQAILEHEEQDEEEDEVPDDETVNQMIARHEEEF
DLFMRMDLDRRREEARNPKRKPRLMEEDELPSWIIKDDAEVERLTCEEEEEKMFGRGSRHRKEVDYSDSLTEKQWLKAIE
EGTLEEIEEEVRQKKSSRKRKRDSDAGSSTPTTSTRSRDKDDESKKQKKRGRPPAEKLSPNPPNLTKKMKKIVDAVIKYK
DSSSGRQLSEVFIQLPSRKELPEYYELIRKPVDFKKIKERIRNHKYRSLNDLEKDVMLLCQNAQTFNLEGSLIYEDSIVL
QSVFTSVRQKIEKEDDSEGEESEEEEEGEEEGSESESRSVKVKIKLGRKEKAQDRLKGGRRRPSRGSRAKPVVSDDDSEE
EQEEDRSGSGSEED
>NR_148052.2
MILSWWLYVHKYIRHLSKLIECIIPRANSNVNYGLWIIMIHQCRFIDCSKCTTLVWDVDSGEAICVGVGGVWELSVLSSQ
FSCESKTALKK
>NR_137288.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPGAERNLLYEDAHRAGA
PRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLG
DSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRHILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKC
QVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVASFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLK
RRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRGHPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKS
VSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKERRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVV
KWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASGQAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGT
YQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLPGKPDK
>NR_132740.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPGEARPAPAQKPAQLKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEE
SEEEEEEEEEEEEETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVP
EQDRGGHLWSGLQSKRQENR
>NR_037687.2
MGTRQKELLDIDSSSVILEDGITKLNTIGHYEISNGSTIKVFKKIANFTSDVEYSDDHCHLILPDSEAFQDVQGKRHRGK
HKFKVKEMYLTKLLSTKVAIHSVLEKLFRSIWSLPNSRAPFAIKYFFDFLDAQAENKKITDPDVVHIWKTNSLPLRFWVN
ILKNPQFVFDIKKTPHIDGCLSVIAQAFMDAFSLTEQQLGKEAPTNKLLYAKDIPTYKEEVKSYYKAIRDLPPLSSSEME
EFLTQESKKHENEFNEEVALTEIYKYIVKYFDEILNKLERERGLEEAQKQLLHVKVLFDEKKKCKWM
>NR_137287.2
MASSNPPPQPAIGDQLVPGVPGPSSEAEDDPGEAFEFDDSDDEEDTSAALGVPSLAPERDTDPPLIHLDSIPVTDPDPAA
APPGTGVPAWVSNGDAADAAFSGARHSSWKRKSSRRIDRFTFPALEEDVIYDDVPCESPDAHQPAGAERNLLYEDAHRAG
APRQAEDLGWSSSEFESYSEDSGEEAKPEVEVEPAKHRVSFQPKLSPDLTRLKERYARTKRDILALRVGGRDMQELKHKY
DCKMTQLMKAAKSGTKDGLEKTRMAVMRKVSFLHRKDVLGDSEEEDMGLLEVSVSDIKPPAPELGPMPEGLSPQQVVRRH
ILGSIVQSEGSYVESLKRILQDYRNPLMEMEPKALSARKCQVVFFRVKEILHCHSMFQIALSSRVAEWDSTEKIGDLFVA
SFSKSMVLDVYSDYVNNFTSAMSIIKKACLTKPAFLEFLKRRQVCSPDRVTLYGLMVKPIQRFPQFILLLQDMLKNTPRG
HPDRLSLQLALTELETLAEKLNEQKRLADQVAEIQQLTKSVSDRSSLNKLLTSGQRQLLLCETLTETVYGDRGQLIKSKE
RRVFLLNDMLVCANINFKPANHRGQLEISSLVPLGPKYVVKWNTALPQVQVVEVGQDGGTYDKDNVLIQHSGAKKASASG
QAQNKVYLGPPRLFQELQDLQKDLAVVEQITLLISTLHGTYQNLNMTVAQDWCLALQRLMRVKEEEIHSANKCRLRLLLP
GKPDK
>NR_157088.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_132739.2
MGDEKDSWKVKTLDEILQEKKRRKEQEEKAEIKRLKNSDDRDSKRDSLEEGELRDHCMEITIRNSPYRREDSMEDRGEED
DSLAIKPPQQMSRKEKVHHRKDEKRKEKCRHHSHSAEGGKHARVKEREHERRKRHREEQDKARREWERQKRREMAREHSR
RERDRLEQLERKRERERKMREQQKEQREQKERERRAEERRKEREARREVSAHHRTMREDYSDKVKASHWSRSPPRPPRER
FELGDGRKPVKEEKMEERDLLSDLQDISDSERKTSSAESSSAESGSGSEEEEEEEEEEEEEGSTSEESEEEEEEEEEEEE
ETGSNSEEASEQSAEEVSEEEMSEDEERENENHLLVVPESRFDRDSGESEEAEEEVGLPERRGVPVPEQDRGGHLWSGLQ
SKRQENR
>NR_045724.2
MADDFGFFSSSESGAPEAAEEDPAAAFLAQQESEIAGIENDEGFGAPAGSHAAPAQPGPTSGAGSEDMGTTVNGDVFQPV
HHQRVQLQTQLPIQPKDEPAHNYSSSIWHSQGQGQKGPAGLRLPTSAQILSPFP
>NR_038863.2
MKSGEDGCPSPKRERICPSLFILLEPLTDWMMPVHIDEGGSSVLSLLLQMLVSSENSLTDPPRNVLPAIWLSLNPVKLTH
KINHHRMLFGFRF
>NR_168349.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168346.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSLVMCVRPLSPSKAIISPVTCMYTSRWPEASEESQKK
>NR_168352.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168351.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCLVNGKGSLSRPQESILGSLARKNLRR
IHRVSKASYFYIEGCTLTDQTMLSDVCQTSEPKQSHHIPCDLHVYIQMA
>NR_168350.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRLTLFADTLYFVWQPYSPLNHLFELFRVMDIVKVRSQMCGNNNAKFKIVVSMEHEGEKHHQGSCQRKGVPIQTPR
EHSWISCKKEFEANP
>NR_168347.1
MFGACYKQPLKPSGSEPPAEECRMTPRHAGCDVTEMQRILSQPTFTEHLLRAVCTKLANMYSTSTDCREHCRRGMKAKQL
KAEAGRSCQRKGVPIQTPREHSWISCKKEFEANP
>NR_168348.1
MSSVKAGTGPFHFFCDSSLASGHLDVYMQVTGDMMALLGLRGLTHITKLTLWIRLKFFLARDPRMLSWGLDRDPFPLTRR
HEVDAQ
>NR_123717.2
MPLVEVQLLLLLYTSMRSGLGKKDKEVMTDTQWKPHIVSWQTEERDVGSSASFDCKVPGFCCTFAHAHGWWEERGIAETH
RRGYRVGEKESRRANTPKEQGQLHLVSLRGTETQE
>NR_168381.1
MLHGRRLGAKATLPHPPLWEAPERGPEIVPHSPPGKEARPPWTEATRSPGRKERTHRPPCGGGRTWSPVVSGRGGISLPV
GLQC
>NR_168373.1
MWLQVRPMPRQFCTAWHMALILSLERNVAVGPASHGVKLHLLLLYSGSNLFLILVL
>NR_168385.1
MLRCLGVSGWGRKDQGTHVLRPRRGVPGRRDFRSLPSAGDLGLCRSPPGSSIRAGVLPAAPKVAWGRWGVPEGMEGPCLG
KEGFRCLWGFSAEPGSPEQTRTELPKPDREGALVASGIHVVDRESARSSPPQ
"""
	