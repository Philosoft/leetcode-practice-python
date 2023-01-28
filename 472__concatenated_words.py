"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

## Example 1:

Input:
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output:
    ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation:
    "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

## Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

## Constraints:

* 1 <= words.length <= 10^4
* 1 <= words[i].length <= 30
* words[i] consists of only lowercase English letters.
* All the strings of words are unique.
* 1 <= sum(words[i].length) <= 10^5
"""
from functools import cache
from typing import List
from unittest import TestCase

from lib.Trie import Trie


class Solution(TestCase):
    def test_example_1(self):
        expected = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
        expected.sort()
        answer = self.findAllConcatenatedWordsInADict(
            ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
        )
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        words = ["cat", "dog", "catdog"]
        expected = ["catdog"]

        self.assertEqual(expected, self.findAllConcatenatedWordsInADict(words))

    def test_leetcode_4(self):
        words = ["rfkqyuqfjkx", "vnrtysfrzrmzl", "gfve", "qfpd", "lqdqrrcrwdnxeuo", "q", "klaitgdphcspij", "hbsfyfv",
                 "adzpbfudkklrw", "aozmixr", "ife", "feclhbvfuk", "yeqfqojwtw", "sileeztxwjl", "ngbqqmbxqcqp", "khhqr",
                 "dwfcayssyoqc", "omwufbdfxu", "zhift", "kczvhsybloet", "crfhpxprbsshsjxd", "ilebxwbcto",
                 "yaxzfbjbkrxi", "imqpzwmshlpj", "ta", "hbuxhwadlpto", "eziwkmg", "ovqzgdixrpddzp", "c", "wnqwqecyjyib",
                 "jy", "mjfqwltvzk", "tpvo", "phckcyufdqml", "lim", "lfz", "tgygdt", "nhcvpf", "fbrpzlk",
                 "shwywshtdgmb", "bkkxcvg", "monmwvytby", "nuqhmfj", "qtg", "cwkuzyamnerp", "fmwevhwlezo", "ye",
                 "hbrcewjxvcezi", "tiq", "tfsrptug", "iznorvonzjfea", "gama", "apwlmbzit", "s", "hzkosvn", "nberblt",
                 "kggdgpljfisylt", "mf", "h", "bljvkypcflsaqe", "cijcyrgmqirz", "iaxakholawoydvch", "e", "gttxwpuk",
                 "jf", "xbrtspfttota", "sngqvoijxuv", "bztvaal", "zxbshnrvbykjql", "zz", "mlvyoshiktodnsjj", "qplci",
                 "lzqrxl", "qxru", "ygjtyzleizme", "inx", "lwhhjwsl", "endjvxjyghrveu", "phknqtsdtwxcktmw",
                 "wsdthzmlmbhjkm", "u", "pbqurqfxgqlojmws", "mowsjvpvhznbsi", "hdkbdxqg", "ge", "pzchrgef", "ukmcowoe",
                 "nwhpiid", "xdnnl", "n", "yjyssbsoc", "cdzcuunkrf", "uvouaghhcyvmlk", "aajpfpyljt", "jpyntsefxi",
                 "wjute", "y", "pbcnmhf", "qmmidmvkn", "xmywegmtuno", "vuzygv", "uxtrdsdfzfssmel", "odjgdgzfmrazvnd",
                 "a", "rdkugsbdpawxi", "ivd", "bbqeonycaegxfj", "lrfkraoheucsvpi", "eqrswgkaaaohxx", "hqjtkqaqh",
                 "berbpmglbjipnuj", "wogwczlkyrde", "aqufowbig", "snjniegvdvotu", "ocedkt", "bbufnxorixibbd", "rzuqsyr",
                 "qghoy", "evcuanuujszitaoa", "wsx", "glafbwzdd", "znrvjqeyqi", "npitruijvyllsi", "objltu", "ryp",
                 "nvybsfrxtlfmp", "id", "zoolzslgd", "owijatklvjzscizr", "upmsoxftumyxifyu", "xucubv", "fctkqlroq",
                 "zjv", "wzi", "ppvs", "mflvioemycnphfjt", "nwedtubynsb", "repgcx", "gsfomhvpmy", "kdohe",
                 "tyycsibbeaxn", "wjkfvabn", "llkmagl", "thkglauzgkeuly", "paeurdvexqlw", "akdt", "ihmfrj", "janxk",
                 "rqdll", "cyhbsuxnlftmjc", "yybwsjmajbwtuhkk", "ovytgaufpjl", "iwbnzhybsx", "mumbh", "jqmdabmyu", "br",
                 "lwstjkoxbczkj", "vhsgzvwiixxaob", "fso", "qnebmfl", "ooetjiz", "lq", "msxphqdgz", "mqhoggvrvjqrp",
                 "xbhkkfg", "zxjegsyovdrmw", "jav", "mshoj", "ax", "biztkfomz", "hujdmcyxdqteqja", "gqgsomonv",
                 "reqqzzpw", "lihdnvud", "lznfhbaokxvce", "fhxbldylqqewdnj", "rlbskqgfvn", "lfvobeyolyy", "v", "iwh",
                 "fpbuiujlolnjl", "gvwxljbo", "ypaotdzjxxrsc", "mwrvel", "umzpnoiei", "ogwilaswn", "yw", "egdgye",
                 "hsrznlzrf", "mwdgxaigmxpy", "yaqgault", "dtlg", "cyvfiykmkllf", "zxqyhvizqmamj", "lvvgoifltzywueyp",
                 "abinmy", "ppzaecvmx", "qsmzc", "iddymnl", "uskihek", "evxtehxtbthq", "jvtfzddlgch", "czohpyewf",
                 "ufzazyxtqxcu", "brxpfymuvfvs", "xrrcfuusicc", "aqhlswbzievij", "rv", "udvmara", "upityz", "fecd",
                 "suxteeitxtg", "dfuydrtbfypbn", "cypqodxr", "wikfuxwjht", "jrliuaifpp", "vkmxys", "wvpfyfpkvgthq",
                 "rmajxis", "jncxgviyu", "av", "nmhskodmidaj", "lkfrimprrhen", "uip", "hstyopbvuiqc", "p",
                 "vwduwmjpblqo", "fnxwgqtvwztje", "xwnbcuggl", "iehimvoymyjasin", "spsqiu", "flhyfac", "mqrbq",
                 "pstsxhplrrmbeddv", "hnegtuxx", "alsyxezjwtlwmxv", "jtxytykkcku", "bhhlovgcx", "xhhivxnutkx", "had",
                 "aysulvk", "m", "anhsyxli", "jdkgfc", "potn", "lcibpxkidmwexp", "gwoxjicdkv", "tltienw", "ngiutnuqbzi",
                 "o", "tzlyb", "vumnwehj", "os", "np", "lhv", "uzvgyeette", "ipfvr", "lpprjjalchhhcmh", "k",
                 "pciulccqssaqgd", "tp", "dmzdzveslyjad", "wtsbhgkd", "eouxbldsxzm", "vhtonlampljgzyve",
                 "xhnlcrldtfthul", "xhflc", "upgei", "rlaks", "yfqvnvtnqspyjbxr", "phouoyhvls", "voibuvbhhjcdflvl",
                 "rgorfbjrofokggaf", "dqhqats", "zchpicyuawpovm", "yzwfor", "koat", "pybf", "fhdzsbiyjld",
                 "gznfnqydisn", "xz", "po", "tcjup", "wygsnxk", "kqlima", "fgxnuohrnhg", "publurhztntgmimc", "zuufzphd",
                 "iucrmmmjqtcey", "wnnbq", "rghzyz", "ukjqsjbmp", "mdtrgv", "vyeikgjdnml", "kxwldnmi", "apzuhsbssaxj",
                 "tkbkoljyodlipof", "nkq", "ktwtj", "vgmkgjwle", "t", "agylw", "vomtuy", "jbtvitkqn", "vtdxwrclpspcn",
                 "rdrls", "yxfeoh", "upj", "myctacn", "fdnor", "ahqghzhoqprgkym", "phiuvdv", "jp", "fdgpouzjwbq",
                 "hqoyefmugjvewhxu", "qfzwuwe", "fnsbijkeepyxry", "oja", "qthkcij", "zpmqfbmnr", "ybaibmzonzqlnmd",
                 "svo", "gjftyfehik", "jfrfgznuaytvaegm", "aljhrx", "odjq", "ogwaxrssjxgvnka", "zaqswwofedxj",
                 "lugpktauixp", "dc", "odknlbvxrs", "jeobu", "vqythyvzxbcgrlbg", "hwc", "erpbaxq", "ujxcxck", "rrklkb",
                 "wlrwyuy", "zmg", "yyhga", "xwdbycdu", "htedgvsrhchox", "wr", "suhesetv", "jonqwhkwezjvjgg",
                 "sqqyrxtjkcalswq", "hvyimhe", "pjzdkmoue", "zbphmgoxq", "lbdlcumdgixjbcq", "ztzdjqmadthtdmv",
                 "qcagsyqggcf", "if", "jpjxcjyi", "chyicqibxdgkqtg", "iwpdklhum", "wljmg", "micmun", "npdbamofynykqv",
                 "ijsnfkpfy", "lmq", "oyjmeqvhcrvgm", "mqopusqktdthpvz", "fz", "r", "qbsqtipq", "nxtsnason", "xbpipyhh",
                 "topsuqomfjrd", "islif", "gbndakaq", "bwnkxnwpzeoohlx", "hrtbfnq", "fguvomeepxoffg", "mat",
                 "dzfpfnwbfuj", "onlvy", "cwcchvsasdylb", "rxfcztzqopdi", "ybrhodjn", "oqkijy", "ncvrjo", "dphbfaal",
                 "xgtpdtkz", "sebevsopjvciwljf", "rcumyacqdapwczen", "mabkapuoud", "pbozezeygljfftvy", "bvazmzbndl",
                 "vl", "qiaixdtbhqvlzd", "ffjfb", "svthrfmkoxbho", "cvet", "ucgqyvopafyttrh", "lbgihet", "naiqyufxffdw",
                 "vruh", "uz", "ukffmudygjavem", "dccamymhp", "wofwgjkykm", "fbuujzxhln", "kmm", "lzandlltowjpwsal",
                 "fapfvrmezbsjxs", "wiw", "sc", "soqlh", "hzaplclkwl", "gcdqbcdwbwa", "gadgt", "pgowefka",
                 "juffuguqepwnfh", "nbuinl", "cpdxf", "sox", "fq", "lfnrhgsxkhx", "xrcorfygjxpi", "mwtqjwbhgh", "loc",
                 "fkglorkkvx", "nlzdhucvayrz", "azefobxutitrf", "rlrstkcbtikklmh", "ggk", "sbphcejuylh", "nraoenhd",
                 "zngyodiqlchxyycx", "rrbhfwohfv", "krzolrglgn", "cpjesdzy", "yoifoyg", "hqqevqjugi", "ahmv",
                 "xgaujnyclcjq", "evhyfnlohavrj", "byyvhgh", "hyw", "kedhvwy", "ysljsqminajfipds", "rglnpxfqwu",
                 "cibpynkxg", "su", "mbntqrlwyampdg", "nig", "ldhlhqdyjcfhu", "jfymrbafmyoc", "tyjmnhlfnrtz",
                 "dlazixtlxyvm", "fbiguhsfuqo", "rhymsno", "rkbdlchs", "ocbbwwd", "astaiamnepwkya", "mplirup", "edkxjq",
                 "g", "exlwulswtvot", "tlnc", "vnrrzerz", "ygeraoozbtt", "yyifkin", "eo", "ua", "qgztvqdolf",
                 "rlzddjzcshvd", "khxkdxflwxme", "kk", "zylbhoaac", "cw", "iizic", "gcdxstpz", "kjwdqeg",
                 "earjrncmmkdel", "kbesuhquepj", "nrzbllldgdmyrpgl", "hllwnqozf", "djpchowhwevbqvjj", "zsmhylnjpktb",
                 "pxnktxkm", "fxwiaqqb", "qjwufmwresfsfaok", "aa", "d", "iobioqm", "svjgzk", "khbzp", "euexyudhrioi",
                 "yqsj", "ngrwqpoh", "rwuvd", "eruffmlg", "bxzovyew", "faz", "pmvfvyguqdi", "jlxnoixsy", "hyfrdngjf",
                 "ly", "eibcapetpmeaid", "tpnwwiif", "pfgsp", "kvhhwkzvtvlhhb", "pjxurgqbtldims", "rncplkeweoirje",
                 "akyprzzphew", "wyvfpjyglzrmhfqp", "ubheeqt", "rmbxlcmn", "taqakgim", "apsbu", "khwnykughmwrlk",
                 "vtdlzwpbhcsbvjno", "tffmjggrmyil", "schgwrrzt", "mvndmua", "nlwpw", "glvbtkegzjs", "piwllpgnlpcnezqs",
                 "xkelind", "urtxsezrwz", "zechoc", "vfaimxrqnyiq", "ybugjsblhzfravzn", "btgcpqwovwp", "zgxgodlhmix",
                 "sfzdknoxzassc", "wgzvqkxuqrsqxs", "dwneyqisozq", "fg", "vhfsf", "uspujvqhydw", "eadosqafyxbmzgr",
                 "tyff", "blolplosqnfcwx", "uwkl", "puenodlvotb", "iizudxqjvfnky", "cjcywjkfvukvveq", "jrxd", "igwb",
                 "dftdyelydzyummmt", "uvfmaicednym", "oai", "higfkfavgeemcgo", "naefganqo", "iqebfibigljbc",
                 "ulicojzjfrc", "igxprunj", "cymbrl", "fqmwciqtynca", "zjyagi", "mzuejrttefhdwqc", "zyiurxvf",
                 "wrjxffzbjexsh", "wrxw", "mhrbdxjwi", "htknfa", "wfrvxqdkhbwwef", "vqsghhhutdget", "cwupzrts", "hbjnb",
                 "wpccoa", "nx", "howbzhaoscgyk", "bilt", "wqqatye", "zceuuwg", "jxzon", "kkfj", "bwsezd",
                 "ifdegsyjtswselk", "xweimxlnzoh", "tqthlftjblnpht", "ww", "ss", "b", "jmruuqscwjp", "nxbk", "wd",
                 "cqkrtbxgzg", "xhppcjnq", "cfq", "tkkolzcfi", "wblxki", "ijeglxsvc", "kcqjjwcwuhvzydm",
                 "gubqavlqffhrzz", "hiwxrgftittd", "caybc", "ncsyjlzlxyyklc", "poxcgnexmaajzuha", "dhaccuualacyl",
                 "mtkewbprs", "oncggqvr", "sqqoffmwkplsgbrp", "ioajuppvqluhbdet", "dzwwzaelmo", "afumtqugec",
                 "wglucmugwqi", "zveswrjevfz", "nxlbkak", "pzcejvxzeoybb", "fd", "vewj", "ivws", "zjhudtpqsfc",
                 "zcmukotirrxx", "zksmx", "umofzhhowyftz", "zbotrokaxaryxlk", "ueolqk", "dxmzhoq", "zvu", "cjl",
                 "esfmqgvxwfy", "npbep", "vbgjtbv", "poeugoqynkbfiv", "fewjjscjrei", "yqssxzsydgllfzmo",
                 "urxkwcypctjkabi", "wqtldwhjouas", "tovdtkr", "onzgeyddkqwuhnim", "ffxviyvsktqrfa", "qujhd", "pvcz",
                 "hiyjlkxmeplnrvxg", "hdykehkefp", "vepcxhozpjxtreyn", "liguhuxudbnh", "f", "ordxzm", "klgohcmmbukz",
                 "yrmooliaobbnlap", "dutnbetocxylcey", "ywdsjegd", "cr", "blbxhjsgcuoxmqft", "ngzdc", "srfyjjumcbxole",
                 "dazwzwtdjoyuqeqj", "xazjarqgfm", "fxyfqbeoktcc", "qrsjchxp", "iltaqzawhgu", "sgenjcfxr", "yfikp",
                 "dvwhbyumthkiktb", "walsx", "jyajrkcvysicisab", "brdeumb", "tviihjwxdcz", "dnrrgmem", "ydgxlrjzucxyid",
                 "cdvdpvjlagwmg", "ngnpxjkxims", "gvyhnchlimsxc", "w", "jtizpezjl", "qe", "rjzv", "vhnqvi", "qm",
                 "iedzqswrsnfmnn", "lt", "utqfcqyrrwm", "wtelvsqrru", "fjwrhjcrtbcytn", "qmqxceuohpiffaq",
                 "rmoybqjjgdyo", "pmxttqftypfexlv", "tg", "qa", "iqbqjlnpbf", "kgaynkddbzllecd", "tccvslp",
                 "curkxfoimnw", "fvnyqkzlheruxr", "iiygnzfov", "coqs", "oa", "eiu", "vzemmxtklis", "lxu", "nrwsjaxzwmh",
                 "tdayz", "oxbbemejgosgcynf", "ykbcn", "hesvnctfvdsp", "ku", "rjhykpadahbhj", "at", "sxlngbtxmqr",
                 "wqrom", "qzyabzrco", "rbbyklndcqdj", "cnsmgmwmpbgjq", "krvnaf", "qrwfajnfahyqocdb", "fnlaozmff",
                 "vmoymbmytjvfcgt", "cijyy", "jdgwjbztl", "swmalgbgpaplqgz", "hfl", "typttkrpfvx", "tkzpzrscwbx",
                 "bwfqqvjcukjbsg", "nxqmxr", "x", "eyavnz", "il", "dhthp", "eyelg", "npsoqsw", "reogbmveofvusdsx",
                 "jvdrjkhxkq", "qzjbrpljwuzpl", "czqeevvbvcwh", "vzuszqvhlmapty", "yu", "yldwwgezlqur",
                 "vorxwgdtgjilgydq", "pknt", "bgihl", "ckorgrm", "ixylxjmlfv", "bpoaboylced", "zea", "igfagitkrext",
                 "ipvqq", "dmoerc", "oqxbypihdv", "dtjrrkxro", "rexuhucxpi", "bvmuyarjwqpcoywa", "qwdmfpwvamisns",
                 "bhopoqdsref", "tmnm", "cre", "ktrniqwoofoeenbz", "vlrfcsftapyujmw", "updqikocrdyex", "bcxw", "eaum",
                 "oklsqebuzeziisw", "fzgyhvnwjcns", "dybjywyaodsyw", "lmu", "eocfru", "ztlbggsuzctoc", "ilfzpszgrgj",
                 "imqypqo", "fump", "sjvmsbrcfwretbie", "oxpmplpcg", "wmqigymr", "qevdyd", "gmuyytguexnyc",
                 "hwialkbjgzc", "lmg", "gijjy", "lplrsxznfkoklxlv", "xrbasbznvxas", "twn", "bhqultkyfq", "saeq", "xbuw",
                 "zd", "kng", "uoay", "kfykd", "armuwp", "gtghfxf", "gpucqwbihemixqmy", "jedyedimaa", "pbdrx",
                 "toxmxzimgfao", "zlteob", "adoshnx", "ufgmypupei", "rqyex", "ljhqsaneicvaerqx", "ng", "sid",
                 "zagpiuiia", "re", "oadojxmvgqgdodw", "jszyeruwnupqgmy", "jxigaskpj", "zpsbhgokwtfcisj", "vep",
                 "ebwrcpafxzhb", "gjykhz", "mfomgxjphcscuxj", "iwbdvusywqlsc", "opvrnx", "mkgiwfvqfkotpdz",
                 "inpobubzbvstk", "vubuucilxyh", "bci", "dibmye", "rlcnvnuuqfvhw", "oorbyyiigppuft", "swpksfdxicemjbf",
                 "goabwrqdoudf", "yjutkeqakoarru", "wuznnlyd", "vfelxvtggkkk", "mxlwbkbklbwfsvr", "advraqovan", "smkln",
                 "jxxvzdjlpyurxpj", "ssebtpznwoytjefo", "dynaiukctgrzjx", "irzosjuncvh", "hcnhhrajahitn",
                 "vwtifcoqepqyzwya", "kddxywvgqxo", "syxngevs", "batvzmziq", "mjewiyo", "pzsupxoflq", "byzhtvvpj",
                 "cqnlvlzr", "akvmxzbaei", "mwo", "vg", "ekfkuajjogbxhjii", "isdbplotyak", "jvkmxhtmyznha",
                 "lqjnqzrwrmgt", "mbbhfli", "bpeohsufree", "ajrcsfogh", "lucidbnlysamvy", "tutjdfnvhahxy", "urbrmmadea",
                 "hghv", "acnjx", "athltizloasimp", "gu", "rjfozvgmdakdhao", "iephs", "uztnpqhdl", "rfuyp",
                 "crcszmgplszwfn", "zihegt", "xbspa", "cjbmsamjyqqrasz", "ghzlgnfoas", "ljxl", "cnumquohlcgt", "jm",
                 "mfccj", "hfedli", "vtpieworwhyiucs", "tdtuquartspkotm", "pnkeluekvelj", "ugrloq", "zljmwt",
                 "fkyvqguqq", "tpjidglpxqfxv", "l", "tvvimvroz", "yy", "opwyfovdz", "pwlumocnyuoume", "vjqpzkcfc",
                 "ihicd", "dtttiixlhpikbv", "goblttgvmndkqgg", "gwsibcqahmyyeagk", "prtvoju", "lcblwidhjpu", "kbu",
                 "pey", "gkzrpc", "bqajopjjlfthe", "bc", "lqs", "zkndgojnjnxqsoqi", "zyesldujjlp", "drswybwlfyzph",
                 "xzluwbtmoxokk", "bedrqfui", "opajzeahv", "lehdfnr", "mnlpimduzgmwszc", "velbhj", "miwdn", "wruqc",
                 "kscfodjxg", "wcbm"]
        expected = ["gfve", "qfpd", "lqdqrrcrwdnxeuo", "hbsfyfv", "ife", "feclhbvfuk", "ngbqqmbxqcqp", "khhqr",
                    "dwfcayssyoqc", "omwufbdfxu", "ilebxwbcto", "ta", "hbuxhwadlpto", "tpvo", "phckcyufdqml", "lfz",
                    "tgygdt", "nhcvpf", "shwywshtdgmb", "bkkxcvg", "monmwvytby", "qtg", "cwkuzyamnerp", "ye",
                    "tfsrptug", "gama", "nberblt", "mf", "gttxwpuk", "xbrtspfttota", "qxru", "phknqtsdtwxcktmw",
                    "pbqurqfxgqlojmws", "hdkbdxqg", "ge", "ukmcowoe", "xdnnl", "yjyssbsoc", "uvouaghhcyvmlk", "pbcnmhf",
                    "qmmidmvkn", "xmywegmtuno", "vuzygv", "uxtrdsdfzfssmel", "eqrswgkaaaohxx", "ocedkt", "qghoy", "wsx",
                    "glafbwzdd", "ryp", "nvybsfrxtlfmp", "upmsoxftumyxifyu", "xucubv", "fctkqlroq", "ppvs",
                    "nwedtubynsb", "repgcx", "gsfomhvpmy", "kdohe", "llkmagl", "thkglauzgkeuly", "paeurdvexqlw", "akdt",
                    "rqdll", "mumbh", "br", "fso", "qnebmfl", "lq", "xbhkkfg", "ax", "gqgsomonv", "reqqzzpw",
                    "rlbskqgfvn", "lfvobeyolyy", "mwrvel", "ogwilaswn", "yw", "egdgye", "yaqgault", "dtlg", "iddymnl",
                    "evxtehxtbthq", "brxpfymuvfvs", "rv", "udvmara", "fecd", "dfuydrtbfypbn", "cypqodxr", "vkmxys",
                    "wvpfyfpkvgthq", "av", "vwduwmjpblqo", "xwnbcuggl", "flhyfac", "mqrbq", "pstsxhplrrmbeddv",
                    "hnegtuxx", "bhhlovgcx", "had", "aysulvk", "potn", "os", "np", "lhv", "uzvgyeette", "tp",
                    "wtsbhgkd", "eouxbldsxzm", "xhnlcrldtfthul", "xhflc", "rlaks", "phouoyhvls", "dqhqats", "koat",
                    "pybf", "po", "wygsnxk", "kqlima", "fgxnuohrnhg", "wnnbq", "mdtrgv", "nkq", "agylw", "vomtuy",
                    "vtdxwrclpspcn", "rdrls", "yxfeoh", "myctacn", "fdnor", "qfzwuwe", "svo", "dc", "odknlbvxrs", "hwc",
                    "erpbaxq", "rrklkb", "wlrwyuy", "yyhga", "xwdbycdu", "htedgvsrhchox", "wr", "suhesetv",
                    "qcagsyqggcf", "wljmg", "npdbamofynykqv", "lmq", "oyjmeqvhcrvgm", "nxtsnason", "gbndakaq",
                    "hrtbfnq", "fguvomeepxoffg", "mat", "onlvy", "cwcchvsasdylb", "dphbfaal", "mabkapuoud", "vl",
                    "ffjfb", "svthrfmkoxbho", "cvet", "ucgqyvopafyttrh", "vruh", "ukffmudygjavem", "dccamymhp", "kmm",
                    "sc", "soqlh", "gcdqbcdwbwa", "gadgt", "pgowefka", "cpdxf", "sox", "fq", "lfnrhgsxkhx", "loc",
                    "fkglorkkvx", "ggk", "nraoenhd", "rrbhfwohfv", "yoifoyg", "ahmv", "byyvhgh", "hyw", "kedhvwy",
                    "rglnpxfqwu", "su", "mbntqrlwyampdg", "jfymrbafmyoc", "rhymsno", "rkbdlchs", "ocbbwwd",
                    "exlwulswtvot", "tlnc", "eo", "ua", "khxkdxflwxme", "kk", "cw", "pxnktxkm", "aa", "ngrwqpoh",
                    "rwuvd", "eruffmlg", "bxzovyew", "hyfrdngjf", "ly", "pfgsp", "akyprzzphew", "ubheeqt", "rmbxlcmn",
                    "apsbu", "khwnykughmwrlk", "mvndmua", "nlwpw", "btgcpqwovwp", "sfzdknoxzassc", "fg", "vhfsf",
                    "tyff", "blolplosqnfcwx", "uwkl", "puenodlvotb", "naefganqo", "cymbrl", "wrxw", "htknfa",
                    "wfrvxqdkhbwwef", "vqsghhhutdget", "wpccoa", "nx", "bilt", "wqqatye", "bwsezd", "ww", "ss",
                    "jmruuqscwjp", "nxbk", "wd", "cfq", "gubqavlqffhrzz", "caybc", "dhaccuualacyl", "mtkewbprs",
                    "oncggqvr", "sqqoffmwkplsgbrp", "afumtqugec", "nxlbkak", "fd", "ueolqk", "esfmqgvxwfy", "npbep",
                    "yqssxzsydgllfzmo", "tovdtkr", "hdykehkefp", "ordxzm", "dutnbetocxylcey", "cr", "ngzdc",
                    "fxyfqbeoktcc", "walsx", "brdeumb", "dnrrgmem", "gvyhnchlimsxc", "qe", "qm", "lt", "utqfcqyrrwm",
                    "wtelvsqrru", "qmqxceuohpiffaq", "pmxttqftypfexlv", "tg", "qa", "tccvslp", "coqs", "oa", "lxu",
                    "ykbcn", "hesvnctfvdsp", "ku", "at", "sxlngbtxmqr", "wqrom", "krvnaf", "hfl", "typttkrpfvx",
                    "nxqmxr", "dhthp", "eyelg", "npsoqsw", "reogbmveofvusdsx", "yu", "pknt", "ckorgrm", "bpoaboylced",
                    "dmoerc", "bhopoqdsref", "tmnm", "cre", "vlrfcsftapyujmw", "bcxw", "eaum", "dybjywyaodsyw", "lmu",
                    "eocfru", "fump", "oxpmplpcg", "qevdyd", "gmuyytguexnyc", "lmg", "lplrsxznfkoklxlv", "twn",
                    "bhqultkyfq", "saeq", "xbuw", "kng", "uoay", "kfykd", "armuwp", "gtghfxf", "pbdrx", "adoshnx",
                    "rqyex", "ng", "sid", "re", "vep", "ebwrcpafxzhb", "opvrnx", "vubuucilxyh", "rlcnvnuuqfvhw",
                    "goabwrqdoudf", "wuznnlyd", "vfelxvtggkkk", "mxlwbkbklbwfsvr", "advraqovan", "smkln", "kddxywvgqxo",
                    "syxngevs", "mwo", "vg", "bpeohsufree", "lucidbnlysamvy", "urbrmmadea", "hghv", "gu", "uztnpqhdl",
                    "rfuyp", "xbspa", "cnumquohlcgt", "tdtuquartspkotm", "ugrloq", "fkyvqguqq", "yy", "pwlumocnyuoume",
                    "goblttgvmndkqgg", "lcblwidhjpu", "kbu", "pey", "bc", "lqs", "xzluwbtmoxokk", "lehdfnr", "wruqc",
                    "wcbm"]
        expected.sort()
        answer = self.findAllConcatenatedWordsInADict(words)
        answer.sort()

        self.assertEqual(expected, answer)

    def findAllConcatenatedWordsInADictDP(self, words: List[str]) -> List[str]:
        # official dp solution
        dictionary = set(words)
        result = []
        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            for i in range(1, length + 1):
                for j in range(1 if i == length else 0, i):
                    dp[i] = dp[j] and word[j:i] in dictionary
                    if dp[i]:
                        break
            if dp[length]:
                result.append(word)

        return result

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        # def partition(w: str) -> List[str]:
        #     maximum = 2 ** (len(w) - 1)
        #     option = 1  # skip option 0, since we don't need whole word
        #     word_list = list(w)
        #     while option < maximum:
        #         tmp_word = word_list.copy()
        #         tmp = option
        #         partition = []
        #         to_pop = 0
        #         while tmp > 0:
        #             to_pop += 1
        #             if tmp & 1 == 1:
        #                 fragment = []
        #                 while to_pop > 0:
        #                     fragment.append(tmp_word.pop())
        #                     to_pop -= 1
        #                 partition.append(fragment)
        #             tmp >>= 1
        #
        #         option += 1
        #         fragment = []
        #         while tmp_word:
        #             fragment.append(tmp_word.pop())
        #         if fragment:
        #             partition.append(fragment)
        #         yield list(map(lambda l: "".join(list(reversed(l))), reversed(partition)))
        #     return []
        def partition(w: str) -> List[str]:
            length = len(w)
            for i in range(length + 1):
                for j in range(1 if i == length else 0, i):
                    print(w[j:i])
                print('============')
            return []

        @cache
        def search_one_word(w: str) -> bool:
            return trie.search(w)

        def is_possible(word_list: List[str]) -> bool:
            for word in word_list:
                if not search_one_word(word):
                    return False
            return True

        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            for i in range(1, length + 1):
                for j in range(1 if i == length else 0, i):
                    dp[i] = dp[j] and search_one_word(word[j:i])
                    if dp[i]:
                        break
            if dp[length]:
                result.append(word)

        # for word in filter(lambda w: len(w) > 1, words):
        #     for par in partition(word):
        #         if is_possible(par):
        #             result.append(word)
        #             break

        return result
