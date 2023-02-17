"""
LeetCode: https://leetcode.com/problems/word-search-ii/description/

[[Blind75]]

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

## Example 1

Input:
    board = [
        [ "o", "a", "a", "n" ],
        [ "e", "t", "a", "e" ],
        [ "i", "h", "k", "r" ],
        [ "i", "f", "l", "v" ],
    ],
    words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

## Example 2

Input:
    board = [
        [ "a", "b" ],
        [ "c", "d" ],
    ],
    words = ["abcb"]
Output: []

## Constraints

* m == board.length
* n == board[i].length
* 1 <= m, n <= 12
* board[i][j] is a lowercase English letter.
* 1 <= words.length <= 3 * 10^4
* 1 <= words[i].length <= 10
* words[i] consists of lowercase English letters.
* All the strings of words are unique.
"""
from typing import List, Dict, Set, Tuple
from unittest import TestCase


class TrieNode:
    children: Dict[str, 'TrieNode']
    is_end_of_word: bool = False
    ref: int = 0

    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        root.ref += 1
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
            root.ref += 1

        root.is_end_of_word = True

    def remove(self, word: str) -> None:
        root = self.root
        root.ref -= 1
        for w in word:
            root = root.children[w]
            root.ref -= 1
        root.is_end_of_word = False


class Solution(TestCase):
    def test_example_1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["eat", "oath"]
        expected.sort()
        answer = self.findWords(board, words)
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        board = [
            ["a", "b"],
            ["c", "d"],
        ]
        words = ["abcb"]
        expected = []
        answer = self.findWords(board, words)

        self.assertEqual(expected, answer)

    def test_leetcode_56_out_of_64(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
        expected = ["oath", "eat", "hklf", "hf"]
        expected.sort()
        answer = self.findWords(board, words)
        answer.sort()

        self.assertEqual(expected, answer)

    # this and next tests are disabled, just because they are too long
    def tst_leetcode_62_out_of_64(self):
        board = [["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
                 ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
        words = ["aaaaaaaaaa", "aaaaaaaaab", "aaaaaaaaac", "aaaaaaaaad", "aaaaaaaaae", "aaaaaaaaaf", "aaaaaaaaag",
                 "aaaaaaaaah", "aaaaaaaaai", "aaaaaaaaaj", "aaaaaaaaak", "aaaaaaaaal", "aaaaaaaaam", "aaaaaaaaan",
                 "aaaaaaaaao", "aaaaaaaaap", "aaaaaaaaaq", "aaaaaaaaar", "aaaaaaaaas", "aaaaaaaaat", "aaaaaaaaau",
                 "aaaaaaaaav", "aaaaaaaaaw", "aaaaaaaaax", "aaaaaaaaay", "aaaaaaaaaz", "aaaaaaaaba", "aaaaaaaabb",
                 "aaaaaaaabc", "aaaaaaaabd", "aaaaaaaabe", "aaaaaaaabf", "aaaaaaaabg", "aaaaaaaabh", "aaaaaaaabi",
                 "aaaaaaaabj", "aaaaaaaabk", "aaaaaaaabl", "aaaaaaaabm", "aaaaaaaabn", "aaaaaaaabo", "aaaaaaaabp",
                 "aaaaaaaabq", "aaaaaaaabr", "aaaaaaaabs", "aaaaaaaabt", "aaaaaaaabu", "aaaaaaaabv", "aaaaaaaabw",
                 "aaaaaaaabx", "aaaaaaaaby", "aaaaaaaabz", "aaaaaaaaca", "aaaaaaaacb", "aaaaaaaacc", "aaaaaaaacd",
                 "aaaaaaaace", "aaaaaaaacf", "aaaaaaaacg", "aaaaaaaach", "aaaaaaaaci", "aaaaaaaacj", "aaaaaaaack",
                 "aaaaaaaacl", "aaaaaaaacm", "aaaaaaaacn", "aaaaaaaaco", "aaaaaaaacp", "aaaaaaaacq", "aaaaaaaacr",
                 "aaaaaaaacs", "aaaaaaaact", "aaaaaaaacu", "aaaaaaaacv", "aaaaaaaacw", "aaaaaaaacx", "aaaaaaaacy",
                 "aaaaaaaacz", "aaaaaaaada", "aaaaaaaadb", "aaaaaaaadc", "aaaaaaaadd", "aaaaaaaade", "aaaaaaaadf",
                 "aaaaaaaadg", "aaaaaaaadh", "aaaaaaaadi", "aaaaaaaadj", "aaaaaaaadk", "aaaaaaaadl", "aaaaaaaadm",
                 "aaaaaaaadn", "aaaaaaaado", "aaaaaaaadp", "aaaaaaaadq", "aaaaaaaadr", "aaaaaaaads", "aaaaaaaadt",
                 "aaaaaaaadu", "aaaaaaaadv", "aaaaaaaadw", "aaaaaaaadx", "aaaaaaaady", "aaaaaaaadz", "aaaaaaaaea",
                 "aaaaaaaaeb", "aaaaaaaaec", "aaaaaaaaed", "aaaaaaaaee", "aaaaaaaaef", "aaaaaaaaeg", "aaaaaaaaeh",
                 "aaaaaaaaei", "aaaaaaaaej", "aaaaaaaaek", "aaaaaaaael", "aaaaaaaaem", "aaaaaaaaen", "aaaaaaaaeo",
                 "aaaaaaaaep", "aaaaaaaaeq", "aaaaaaaaer", "aaaaaaaaes", "aaaaaaaaet", "aaaaaaaaeu", "aaaaaaaaev",
                 "aaaaaaaaew", "aaaaaaaaex", "aaaaaaaaey", "aaaaaaaaez", "aaaaaaaafa", "aaaaaaaafb", "aaaaaaaafc",
                 "aaaaaaaafd", "aaaaaaaafe", "aaaaaaaaff", "aaaaaaaafg", "aaaaaaaafh", "aaaaaaaafi", "aaaaaaaafj",
                 "aaaaaaaafk", "aaaaaaaafl", "aaaaaaaafm", "aaaaaaaafn", "aaaaaaaafo", "aaaaaaaafp", "aaaaaaaafq",
                 "aaaaaaaafr", "aaaaaaaafs", "aaaaaaaaft", "aaaaaaaafu", "aaaaaaaafv", "aaaaaaaafw", "aaaaaaaafx",
                 "aaaaaaaafy", "aaaaaaaafz", "aaaaaaaaga", "aaaaaaaagb", "aaaaaaaagc", "aaaaaaaagd", "aaaaaaaage",
                 "aaaaaaaagf", "aaaaaaaagg", "aaaaaaaagh", "aaaaaaaagi", "aaaaaaaagj", "aaaaaaaagk", "aaaaaaaagl",
                 "aaaaaaaagm", "aaaaaaaagn", "aaaaaaaago", "aaaaaaaagp", "aaaaaaaagq", "aaaaaaaagr", "aaaaaaaags",
                 "aaaaaaaagt", "aaaaaaaagu", "aaaaaaaagv", "aaaaaaaagw", "aaaaaaaagx", "aaaaaaaagy", "aaaaaaaagz",
                 "aaaaaaaaha", "aaaaaaaahb", "aaaaaaaahc", "aaaaaaaahd", "aaaaaaaahe", "aaaaaaaahf", "aaaaaaaahg",
                 "aaaaaaaahh", "aaaaaaaahi", "aaaaaaaahj", "aaaaaaaahk", "aaaaaaaahl", "aaaaaaaahm", "aaaaaaaahn",
                 "aaaaaaaaho", "aaaaaaaahp", "aaaaaaaahq", "aaaaaaaahr", "aaaaaaaahs", "aaaaaaaaht", "aaaaaaaahu",
                 "aaaaaaaahv", "aaaaaaaahw", "aaaaaaaahx", "aaaaaaaahy", "aaaaaaaahz", "aaaaaaaaia", "aaaaaaaaib",
                 "aaaaaaaaic", "aaaaaaaaid", "aaaaaaaaie", "aaaaaaaaif", "aaaaaaaaig", "aaaaaaaaih", "aaaaaaaaii",
                 "aaaaaaaaij", "aaaaaaaaik", "aaaaaaaail", "aaaaaaaaim", "aaaaaaaain", "aaaaaaaaio", "aaaaaaaaip",
                 "aaaaaaaaiq", "aaaaaaaair", "aaaaaaaais", "aaaaaaaait", "aaaaaaaaiu", "aaaaaaaaiv", "aaaaaaaaiw",
                 "aaaaaaaaix", "aaaaaaaaiy", "aaaaaaaaiz", "aaaaaaaaja", "aaaaaaaajb", "aaaaaaaajc", "aaaaaaaajd",
                 "aaaaaaaaje", "aaaaaaaajf", "aaaaaaaajg", "aaaaaaaajh", "aaaaaaaaji", "aaaaaaaajj", "aaaaaaaajk",
                 "aaaaaaaajl", "aaaaaaaajm", "aaaaaaaajn", "aaaaaaaajo", "aaaaaaaajp", "aaaaaaaajq", "aaaaaaaajr",
                 "aaaaaaaajs", "aaaaaaaajt", "aaaaaaaaju", "aaaaaaaajv", "aaaaaaaajw", "aaaaaaaajx", "aaaaaaaajy",
                 "aaaaaaaajz", "aaaaaaaaka", "aaaaaaaakb", "aaaaaaaakc", "aaaaaaaakd", "aaaaaaaake", "aaaaaaaakf",
                 "aaaaaaaakg", "aaaaaaaakh", "aaaaaaaaki", "aaaaaaaakj", "aaaaaaaakk", "aaaaaaaakl", "aaaaaaaakm",
                 "aaaaaaaakn", "aaaaaaaako", "aaaaaaaakp", "aaaaaaaakq", "aaaaaaaakr", "aaaaaaaaks", "aaaaaaaakt",
                 "aaaaaaaaku", "aaaaaaaakv", "aaaaaaaakw", "aaaaaaaakx", "aaaaaaaaky", "aaaaaaaakz", "aaaaaaaala",
                 "aaaaaaaalb", "aaaaaaaalc", "aaaaaaaald", "aaaaaaaale", "aaaaaaaalf", "aaaaaaaalg", "aaaaaaaalh",
                 "aaaaaaaali", "aaaaaaaalj", "aaaaaaaalk", "aaaaaaaall", "aaaaaaaalm", "aaaaaaaaln", "aaaaaaaalo",
                 "aaaaaaaalp", "aaaaaaaalq", "aaaaaaaalr", "aaaaaaaals", "aaaaaaaalt", "aaaaaaaalu", "aaaaaaaalv",
                 "aaaaaaaalw", "aaaaaaaalx", "aaaaaaaaly", "aaaaaaaalz", "aaaaaaaama", "aaaaaaaamb", "aaaaaaaamc",
                 "aaaaaaaamd", "aaaaaaaame", "aaaaaaaamf", "aaaaaaaamg", "aaaaaaaamh", "aaaaaaaami", "aaaaaaaamj",
                 "aaaaaaaamk", "aaaaaaaaml", "aaaaaaaamm", "aaaaaaaamn", "aaaaaaaamo", "aaaaaaaamp", "aaaaaaaamq",
                 "aaaaaaaamr", "aaaaaaaams", "aaaaaaaamt", "aaaaaaaamu", "aaaaaaaamv", "aaaaaaaamw", "aaaaaaaamx",
                 "aaaaaaaamy", "aaaaaaaamz", "aaaaaaaana", "aaaaaaaanb", "aaaaaaaanc", "aaaaaaaand", "aaaaaaaane",
                 "aaaaaaaanf", "aaaaaaaang", "aaaaaaaanh", "aaaaaaaani", "aaaaaaaanj", "aaaaaaaank", "aaaaaaaanl",
                 "aaaaaaaanm", "aaaaaaaann", "aaaaaaaano", "aaaaaaaanp", "aaaaaaaanq", "aaaaaaaanr", "aaaaaaaans",
                 "aaaaaaaant", "aaaaaaaanu", "aaaaaaaanv", "aaaaaaaanw", "aaaaaaaanx", "aaaaaaaany", "aaaaaaaanz",
                 "aaaaaaaaoa", "aaaaaaaaob", "aaaaaaaaoc", "aaaaaaaaod", "aaaaaaaaoe", "aaaaaaaaof", "aaaaaaaaog",
                 "aaaaaaaaoh", "aaaaaaaaoi", "aaaaaaaaoj", "aaaaaaaaok", "aaaaaaaaol", "aaaaaaaaom", "aaaaaaaaon",
                 "aaaaaaaaoo", "aaaaaaaaop", "aaaaaaaaoq", "aaaaaaaaor", "aaaaaaaaos", "aaaaaaaaot", "aaaaaaaaou",
                 "aaaaaaaaov", "aaaaaaaaow", "aaaaaaaaox", "aaaaaaaaoy", "aaaaaaaaoz", "aaaaaaaapa", "aaaaaaaapb",
                 "aaaaaaaapc", "aaaaaaaapd", "aaaaaaaape", "aaaaaaaapf", "aaaaaaaapg", "aaaaaaaaph", "aaaaaaaapi",
                 "aaaaaaaapj", "aaaaaaaapk", "aaaaaaaapl", "aaaaaaaapm", "aaaaaaaapn", "aaaaaaaapo", "aaaaaaaapp",
                 "aaaaaaaapq", "aaaaaaaapr", "aaaaaaaaps", "aaaaaaaapt", "aaaaaaaapu", "aaaaaaaapv", "aaaaaaaapw",
                 "aaaaaaaapx", "aaaaaaaapy", "aaaaaaaapz", "aaaaaaaaqa", "aaaaaaaaqb", "aaaaaaaaqc", "aaaaaaaaqd",
                 "aaaaaaaaqe", "aaaaaaaaqf", "aaaaaaaaqg", "aaaaaaaaqh", "aaaaaaaaqi", "aaaaaaaaqj", "aaaaaaaaqk",
                 "aaaaaaaaql", "aaaaaaaaqm", "aaaaaaaaqn", "aaaaaaaaqo", "aaaaaaaaqp", "aaaaaaaaqq", "aaaaaaaaqr",
                 "aaaaaaaaqs", "aaaaaaaaqt", "aaaaaaaaqu", "aaaaaaaaqv", "aaaaaaaaqw", "aaaaaaaaqx", "aaaaaaaaqy",
                 "aaaaaaaaqz", "aaaaaaaara", "aaaaaaaarb", "aaaaaaaarc", "aaaaaaaard", "aaaaaaaare", "aaaaaaaarf",
                 "aaaaaaaarg", "aaaaaaaarh", "aaaaaaaari", "aaaaaaaarj", "aaaaaaaark", "aaaaaaaarl", "aaaaaaaarm",
                 "aaaaaaaarn", "aaaaaaaaro", "aaaaaaaarp", "aaaaaaaarq", "aaaaaaaarr", "aaaaaaaars", "aaaaaaaart",
                 "aaaaaaaaru", "aaaaaaaarv", "aaaaaaaarw", "aaaaaaaarx", "aaaaaaaary", "aaaaaaaarz", "aaaaaaaasa",
                 "aaaaaaaasb", "aaaaaaaasc", "aaaaaaaasd", "aaaaaaaase", "aaaaaaaasf", "aaaaaaaasg", "aaaaaaaash",
                 "aaaaaaaasi", "aaaaaaaasj", "aaaaaaaask", "aaaaaaaasl", "aaaaaaaasm", "aaaaaaaasn", "aaaaaaaaso",
                 "aaaaaaaasp", "aaaaaaaasq", "aaaaaaaasr", "aaaaaaaass", "aaaaaaaast", "aaaaaaaasu", "aaaaaaaasv",
                 "aaaaaaaasw", "aaaaaaaasx", "aaaaaaaasy", "aaaaaaaasz", "aaaaaaaata", "aaaaaaaatb", "aaaaaaaatc",
                 "aaaaaaaatd", "aaaaaaaate", "aaaaaaaatf", "aaaaaaaatg", "aaaaaaaath", "aaaaaaaati", "aaaaaaaatj",
                 "aaaaaaaatk", "aaaaaaaatl", "aaaaaaaatm", "aaaaaaaatn", "aaaaaaaato", "aaaaaaaatp", "aaaaaaaatq",
                 "aaaaaaaatr", "aaaaaaaats", "aaaaaaaatt", "aaaaaaaatu", "aaaaaaaatv", "aaaaaaaatw", "aaaaaaaatx",
                 "aaaaaaaaty", "aaaaaaaatz", "aaaaaaaaua", "aaaaaaaaub", "aaaaaaaauc", "aaaaaaaaud", "aaaaaaaaue",
                 "aaaaaaaauf", "aaaaaaaaug", "aaaaaaaauh", "aaaaaaaaui", "aaaaaaaauj", "aaaaaaaauk", "aaaaaaaaul",
                 "aaaaaaaaum", "aaaaaaaaun", "aaaaaaaauo", "aaaaaaaaup", "aaaaaaaauq", "aaaaaaaaur", "aaaaaaaaus",
                 "aaaaaaaaut", "aaaaaaaauu", "aaaaaaaauv", "aaaaaaaauw", "aaaaaaaaux", "aaaaaaaauy", "aaaaaaaauz",
                 "aaaaaaaava", "aaaaaaaavb", "aaaaaaaavc", "aaaaaaaavd", "aaaaaaaave", "aaaaaaaavf", "aaaaaaaavg",
                 "aaaaaaaavh", "aaaaaaaavi", "aaaaaaaavj", "aaaaaaaavk", "aaaaaaaavl", "aaaaaaaavm", "aaaaaaaavn",
                 "aaaaaaaavo", "aaaaaaaavp", "aaaaaaaavq", "aaaaaaaavr", "aaaaaaaavs", "aaaaaaaavt", "aaaaaaaavu",
                 "aaaaaaaavv", "aaaaaaaavw", "aaaaaaaavx", "aaaaaaaavy", "aaaaaaaavz", "aaaaaaaawa", "aaaaaaaawb",
                 "aaaaaaaawc", "aaaaaaaawd", "aaaaaaaawe", "aaaaaaaawf", "aaaaaaaawg", "aaaaaaaawh", "aaaaaaaawi",
                 "aaaaaaaawj", "aaaaaaaawk", "aaaaaaaawl", "aaaaaaaawm", "aaaaaaaawn", "aaaaaaaawo", "aaaaaaaawp",
                 "aaaaaaaawq", "aaaaaaaawr", "aaaaaaaaws", "aaaaaaaawt", "aaaaaaaawu", "aaaaaaaawv", "aaaaaaaaww",
                 "aaaaaaaawx", "aaaaaaaawy", "aaaaaaaawz", "aaaaaaaaxa", "aaaaaaaaxb", "aaaaaaaaxc", "aaaaaaaaxd",
                 "aaaaaaaaxe", "aaaaaaaaxf", "aaaaaaaaxg", "aaaaaaaaxh", "aaaaaaaaxi", "aaaaaaaaxj", "aaaaaaaaxk",
                 "aaaaaaaaxl", "aaaaaaaaxm", "aaaaaaaaxn", "aaaaaaaaxo", "aaaaaaaaxp", "aaaaaaaaxq", "aaaaaaaaxr",
                 "aaaaaaaaxs", "aaaaaaaaxt", "aaaaaaaaxu", "aaaaaaaaxv", "aaaaaaaaxw", "aaaaaaaaxx", "aaaaaaaaxy",
                 "aaaaaaaaxz", "aaaaaaaaya", "aaaaaaaayb", "aaaaaaaayc", "aaaaaaaayd", "aaaaaaaaye", "aaaaaaaayf",
                 "aaaaaaaayg", "aaaaaaaayh", "aaaaaaaayi", "aaaaaaaayj", "aaaaaaaayk", "aaaaaaaayl", "aaaaaaaaym",
                 "aaaaaaaayn", "aaaaaaaayo", "aaaaaaaayp", "aaaaaaaayq", "aaaaaaaayr", "aaaaaaaays", "aaaaaaaayt",
                 "aaaaaaaayu", "aaaaaaaayv", "aaaaaaaayw", "aaaaaaaayx", "aaaaaaaayy", "aaaaaaaayz", "aaaaaaaaza",
                 "aaaaaaaazb", "aaaaaaaazc", "aaaaaaaazd", "aaaaaaaaze", "aaaaaaaazf", "aaaaaaaazg", "aaaaaaaazh",
                 "aaaaaaaazi", "aaaaaaaazj", "aaaaaaaazk", "aaaaaaaazl", "aaaaaaaazm", "aaaaaaaazn", "aaaaaaaazo",
                 "aaaaaaaazp", "aaaaaaaazq", "aaaaaaaazr", "aaaaaaaazs", "aaaaaaaazt", "aaaaaaaazu", "aaaaaaaazv",
                 "aaaaaaaazw", "aaaaaaaazx", "aaaaaaaazy", "aaaaaaaazz"]
        expected = ['aaaaaaaaaa', 'aaaaaaaaab', 'aaaaaaaaac', 'aaaaaaaaad', 'aaaaaaaaae', 'aaaaaaaaaf', 'aaaaaaaaag',
                    'aaaaaaaaah', 'aaaaaaaaai', 'aaaaaaaaaj', 'aaaaaaaaak', 'aaaaaaaaal', 'aaaaaaaaan', 'aaaaaaaaao',
                    'aaaaaaaaap', 'aaaaaaaaaq', 'aaaaaaaaar', 'aaaaaaaaas', 'aaaaaaaaat', 'aaaaaaaaau', 'aaaaaaaaav',
                    'aaaaaaaaaw', 'aaaaaaaaay', 'aaaaaaaaaz', 'aaaaaaaabc', 'aaaaaaaabm', 'aaaaaaaacb', 'aaaaaaaacd',
                    'aaaaaaaadc', 'aaaaaaaade', 'aaaaaaaaed', 'aaaaaaaaef', 'aaaaaaaafe', 'aaaaaaaafg', 'aaaaaaaagf',
                    'aaaaaaaagh', 'aaaaaaaahg', 'aaaaaaaahi', 'aaaaaaaaih', 'aaaaaaaaij', 'aaaaaaaaji', 'aaaaaaaajk',
                    'aaaaaaaakj', 'aaaaaaaakl', 'aaaaaaaalk', 'aaaaaaaanm', 'aaaaaaaano', 'aaaaaaaaon', 'aaaaaaaaop',
                    'aaaaaaaapo', 'aaaaaaaapq', 'aaaaaaaaqp', 'aaaaaaaaqr', 'aaaaaaaarq', 'aaaaaaaars', 'aaaaaaaasr',
                    'aaaaaaaast', 'aaaaaaaats', 'aaaaaaaatu', 'aaaaaaaaut', 'aaaaaaaauv', 'aaaaaaaavu', 'aaaaaaaavw',
                    'aaaaaaaawv', 'aaaaaaaawx', 'aaaaaaaayx', 'aaaaaaaayz', 'aaaaaaaaza', 'aaaaaaaazy']
        expected.sort()
        answer = self.findWords(board, words)
        answer.sort()

        self.assertEqual(expected, answer)

    def tst_leetcode_63_out_of_64(self):
        board = [["m", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
                 ["n", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["o", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["p", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["q", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["r", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["t", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["u", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["v", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                 ["x", "y", "z", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
        words = ["aaaaaaaaaa", "baaaaaaaaa", "caaaaaaaaa", "daaaaaaaaa", "eaaaaaaaaa", "faaaaaaaaa", "gaaaaaaaaa",
                 "haaaaaaaaa", "iaaaaaaaaa", "jaaaaaaaaa", "kaaaaaaaaa", "laaaaaaaaa", "maaaaaaaaa", "naaaaaaaaa",
                 "oaaaaaaaaa", "paaaaaaaaa", "qaaaaaaaaa", "raaaaaaaaa", "saaaaaaaaa", "taaaaaaaaa", "uaaaaaaaaa",
                 "vaaaaaaaaa", "waaaaaaaaa", "xaaaaaaaaa", "yaaaaaaaaa", "zaaaaaaaaa", "abaaaaaaaa", "bbaaaaaaaa",
                 "cbaaaaaaaa", "dbaaaaaaaa", "ebaaaaaaaa", "fbaaaaaaaa", "gbaaaaaaaa", "hbaaaaaaaa", "ibaaaaaaaa",
                 "jbaaaaaaaa", "kbaaaaaaaa", "lbaaaaaaaa", "mbaaaaaaaa", "nbaaaaaaaa", "obaaaaaaaa", "pbaaaaaaaa",
                 "qbaaaaaaaa", "rbaaaaaaaa", "sbaaaaaaaa", "tbaaaaaaaa", "ubaaaaaaaa", "vbaaaaaaaa", "wbaaaaaaaa",
                 "xbaaaaaaaa", "ybaaaaaaaa", "zbaaaaaaaa", "acaaaaaaaa", "bcaaaaaaaa", "ccaaaaaaaa", "dcaaaaaaaa",
                 "ecaaaaaaaa", "fcaaaaaaaa", "gcaaaaaaaa", "hcaaaaaaaa", "icaaaaaaaa", "jcaaaaaaaa", "kcaaaaaaaa",
                 "lcaaaaaaaa", "mcaaaaaaaa", "ncaaaaaaaa", "ocaaaaaaaa", "pcaaaaaaaa", "qcaaaaaaaa", "rcaaaaaaaa",
                 "scaaaaaaaa", "tcaaaaaaaa", "ucaaaaaaaa", "vcaaaaaaaa", "wcaaaaaaaa", "xcaaaaaaaa", "ycaaaaaaaa",
                 "zcaaaaaaaa", "adaaaaaaaa", "bdaaaaaaaa", "cdaaaaaaaa", "ddaaaaaaaa", "edaaaaaaaa", "fdaaaaaaaa",
                 "gdaaaaaaaa", "hdaaaaaaaa", "idaaaaaaaa", "jdaaaaaaaa", "kdaaaaaaaa", "ldaaaaaaaa", "mdaaaaaaaa",
                 "ndaaaaaaaa", "odaaaaaaaa", "pdaaaaaaaa", "qdaaaaaaaa", "rdaaaaaaaa", "sdaaaaaaaa", "tdaaaaaaaa",
                 "udaaaaaaaa", "vdaaaaaaaa", "wdaaaaaaaa", "xdaaaaaaaa", "ydaaaaaaaa", "zdaaaaaaaa", "aeaaaaaaaa",
                 "beaaaaaaaa", "ceaaaaaaaa", "deaaaaaaaa", "eeaaaaaaaa", "feaaaaaaaa", "geaaaaaaaa", "heaaaaaaaa",
                 "ieaaaaaaaa", "jeaaaaaaaa", "keaaaaaaaa", "leaaaaaaaa", "meaaaaaaaa", "neaaaaaaaa", "oeaaaaaaaa",
                 "peaaaaaaaa", "qeaaaaaaaa", "reaaaaaaaa", "seaaaaaaaa", "teaaaaaaaa", "ueaaaaaaaa", "veaaaaaaaa",
                 "weaaaaaaaa", "xeaaaaaaaa", "yeaaaaaaaa", "zeaaaaaaaa", "afaaaaaaaa", "bfaaaaaaaa", "cfaaaaaaaa",
                 "dfaaaaaaaa", "efaaaaaaaa", "ffaaaaaaaa", "gfaaaaaaaa", "hfaaaaaaaa", "ifaaaaaaaa", "jfaaaaaaaa",
                 "kfaaaaaaaa", "lfaaaaaaaa", "mfaaaaaaaa", "nfaaaaaaaa", "ofaaaaaaaa", "pfaaaaaaaa", "qfaaaaaaaa",
                 "rfaaaaaaaa", "sfaaaaaaaa", "tfaaaaaaaa", "ufaaaaaaaa", "vfaaaaaaaa", "wfaaaaaaaa", "xfaaaaaaaa",
                 "yfaaaaaaaa", "zfaaaaaaaa", "agaaaaaaaa", "bgaaaaaaaa", "cgaaaaaaaa", "dgaaaaaaaa", "egaaaaaaaa",
                 "fgaaaaaaaa", "ggaaaaaaaa", "hgaaaaaaaa", "igaaaaaaaa", "jgaaaaaaaa", "kgaaaaaaaa", "lgaaaaaaaa",
                 "mgaaaaaaaa", "ngaaaaaaaa", "ogaaaaaaaa", "pgaaaaaaaa", "qgaaaaaaaa", "rgaaaaaaaa", "sgaaaaaaaa",
                 "tgaaaaaaaa", "ugaaaaaaaa", "vgaaaaaaaa", "wgaaaaaaaa", "xgaaaaaaaa", "ygaaaaaaaa", "zgaaaaaaaa",
                 "ahaaaaaaaa", "bhaaaaaaaa", "chaaaaaaaa", "dhaaaaaaaa", "ehaaaaaaaa", "fhaaaaaaaa", "ghaaaaaaaa",
                 "hhaaaaaaaa", "ihaaaaaaaa", "jhaaaaaaaa", "khaaaaaaaa", "lhaaaaaaaa", "mhaaaaaaaa", "nhaaaaaaaa",
                 "ohaaaaaaaa", "phaaaaaaaa", "qhaaaaaaaa", "rhaaaaaaaa", "shaaaaaaaa", "thaaaaaaaa", "uhaaaaaaaa",
                 "vhaaaaaaaa", "whaaaaaaaa", "xhaaaaaaaa", "yhaaaaaaaa", "zhaaaaaaaa", "aiaaaaaaaa", "biaaaaaaaa",
                 "ciaaaaaaaa", "diaaaaaaaa", "eiaaaaaaaa", "fiaaaaaaaa", "giaaaaaaaa", "hiaaaaaaaa", "iiaaaaaaaa",
                 "jiaaaaaaaa", "kiaaaaaaaa", "liaaaaaaaa", "miaaaaaaaa", "niaaaaaaaa", "oiaaaaaaaa", "piaaaaaaaa",
                 "qiaaaaaaaa", "riaaaaaaaa", "siaaaaaaaa", "tiaaaaaaaa", "uiaaaaaaaa", "viaaaaaaaa", "wiaaaaaaaa",
                 "xiaaaaaaaa", "yiaaaaaaaa", "ziaaaaaaaa", "ajaaaaaaaa", "bjaaaaaaaa", "cjaaaaaaaa", "djaaaaaaaa",
                 "ejaaaaaaaa", "fjaaaaaaaa", "gjaaaaaaaa", "hjaaaaaaaa", "ijaaaaaaaa", "jjaaaaaaaa", "kjaaaaaaaa",
                 "ljaaaaaaaa", "mjaaaaaaaa", "njaaaaaaaa", "ojaaaaaaaa", "pjaaaaaaaa", "qjaaaaaaaa", "rjaaaaaaaa",
                 "sjaaaaaaaa", "tjaaaaaaaa", "ujaaaaaaaa", "vjaaaaaaaa", "wjaaaaaaaa", "xjaaaaaaaa", "yjaaaaaaaa",
                 "zjaaaaaaaa", "akaaaaaaaa", "bkaaaaaaaa", "ckaaaaaaaa", "dkaaaaaaaa", "ekaaaaaaaa", "fkaaaaaaaa",
                 "gkaaaaaaaa", "hkaaaaaaaa", "ikaaaaaaaa", "jkaaaaaaaa", "kkaaaaaaaa", "lkaaaaaaaa", "mkaaaaaaaa",
                 "nkaaaaaaaa", "okaaaaaaaa", "pkaaaaaaaa", "qkaaaaaaaa", "rkaaaaaaaa", "skaaaaaaaa", "tkaaaaaaaa",
                 "ukaaaaaaaa", "vkaaaaaaaa", "wkaaaaaaaa", "xkaaaaaaaa", "ykaaaaaaaa", "zkaaaaaaaa", "alaaaaaaaa",
                 "blaaaaaaaa", "claaaaaaaa", "dlaaaaaaaa", "elaaaaaaaa", "flaaaaaaaa", "glaaaaaaaa", "hlaaaaaaaa",
                 "ilaaaaaaaa", "jlaaaaaaaa", "klaaaaaaaa", "llaaaaaaaa", "mlaaaaaaaa", "nlaaaaaaaa", "olaaaaaaaa",
                 "plaaaaaaaa", "qlaaaaaaaa", "rlaaaaaaaa", "slaaaaaaaa", "tlaaaaaaaa", "ulaaaaaaaa", "vlaaaaaaaa",
                 "wlaaaaaaaa", "xlaaaaaaaa", "ylaaaaaaaa", "zlaaaaaaaa", "amaaaaaaaa", "bmaaaaaaaa", "cmaaaaaaaa",
                 "dmaaaaaaaa", "emaaaaaaaa", "fmaaaaaaaa", "gmaaaaaaaa", "hmaaaaaaaa", "imaaaaaaaa", "jmaaaaaaaa",
                 "kmaaaaaaaa", "lmaaaaaaaa", "mmaaaaaaaa", "nmaaaaaaaa", "omaaaaaaaa", "pmaaaaaaaa", "qmaaaaaaaa",
                 "rmaaaaaaaa", "smaaaaaaaa", "tmaaaaaaaa", "umaaaaaaaa", "vmaaaaaaaa", "wmaaaaaaaa", "xmaaaaaaaa",
                 "ymaaaaaaaa", "zmaaaaaaaa", "anaaaaaaaa", "bnaaaaaaaa", "cnaaaaaaaa", "dnaaaaaaaa", "enaaaaaaaa",
                 "fnaaaaaaaa", "gnaaaaaaaa", "hnaaaaaaaa", "inaaaaaaaa", "jnaaaaaaaa", "knaaaaaaaa", "lnaaaaaaaa",
                 "mnaaaaaaaa", "nnaaaaaaaa", "onaaaaaaaa", "pnaaaaaaaa", "qnaaaaaaaa", "rnaaaaaaaa", "snaaaaaaaa",
                 "tnaaaaaaaa", "unaaaaaaaa", "vnaaaaaaaa", "wnaaaaaaaa", "xnaaaaaaaa", "ynaaaaaaaa", "znaaaaaaaa",
                 "aoaaaaaaaa", "boaaaaaaaa", "coaaaaaaaa", "doaaaaaaaa", "eoaaaaaaaa", "foaaaaaaaa", "goaaaaaaaa",
                 "hoaaaaaaaa", "ioaaaaaaaa", "joaaaaaaaa", "koaaaaaaaa", "loaaaaaaaa", "moaaaaaaaa", "noaaaaaaaa",
                 "ooaaaaaaaa", "poaaaaaaaa", "qoaaaaaaaa", "roaaaaaaaa", "soaaaaaaaa", "toaaaaaaaa", "uoaaaaaaaa",
                 "voaaaaaaaa", "woaaaaaaaa", "xoaaaaaaaa", "yoaaaaaaaa", "zoaaaaaaaa", "apaaaaaaaa", "bpaaaaaaaa",
                 "cpaaaaaaaa", "dpaaaaaaaa", "epaaaaaaaa", "fpaaaaaaaa", "gpaaaaaaaa", "hpaaaaaaaa", "ipaaaaaaaa",
                 "jpaaaaaaaa", "kpaaaaaaaa", "lpaaaaaaaa", "mpaaaaaaaa", "npaaaaaaaa", "opaaaaaaaa", "ppaaaaaaaa",
                 "qpaaaaaaaa", "rpaaaaaaaa", "spaaaaaaaa", "tpaaaaaaaa", "upaaaaaaaa", "vpaaaaaaaa", "wpaaaaaaaa",
                 "xpaaaaaaaa", "ypaaaaaaaa", "zpaaaaaaaa", "aqaaaaaaaa", "bqaaaaaaaa", "cqaaaaaaaa", "dqaaaaaaaa",
                 "eqaaaaaaaa", "fqaaaaaaaa", "gqaaaaaaaa", "hqaaaaaaaa", "iqaaaaaaaa", "jqaaaaaaaa", "kqaaaaaaaa",
                 "lqaaaaaaaa", "mqaaaaaaaa", "nqaaaaaaaa", "oqaaaaaaaa", "pqaaaaaaaa", "qqaaaaaaaa", "rqaaaaaaaa",
                 "sqaaaaaaaa", "tqaaaaaaaa", "uqaaaaaaaa", "vqaaaaaaaa", "wqaaaaaaaa", "xqaaaaaaaa", "yqaaaaaaaa",
                 "zqaaaaaaaa", "araaaaaaaa", "braaaaaaaa", "craaaaaaaa", "draaaaaaaa", "eraaaaaaaa", "fraaaaaaaa",
                 "graaaaaaaa", "hraaaaaaaa", "iraaaaaaaa", "jraaaaaaaa", "kraaaaaaaa", "lraaaaaaaa", "mraaaaaaaa",
                 "nraaaaaaaa", "oraaaaaaaa", "praaaaaaaa", "qraaaaaaaa", "rraaaaaaaa", "sraaaaaaaa", "traaaaaaaa",
                 "uraaaaaaaa", "vraaaaaaaa", "wraaaaaaaa", "xraaaaaaaa", "yraaaaaaaa", "zraaaaaaaa", "asaaaaaaaa",
                 "bsaaaaaaaa", "csaaaaaaaa", "dsaaaaaaaa", "esaaaaaaaa", "fsaaaaaaaa", "gsaaaaaaaa", "hsaaaaaaaa",
                 "isaaaaaaaa", "jsaaaaaaaa", "ksaaaaaaaa", "lsaaaaaaaa", "msaaaaaaaa", "nsaaaaaaaa", "osaaaaaaaa",
                 "psaaaaaaaa", "qsaaaaaaaa", "rsaaaaaaaa", "ssaaaaaaaa", "tsaaaaaaaa", "usaaaaaaaa", "vsaaaaaaaa",
                 "wsaaaaaaaa", "xsaaaaaaaa", "ysaaaaaaaa", "zsaaaaaaaa", "ataaaaaaaa", "btaaaaaaaa", "ctaaaaaaaa",
                 "dtaaaaaaaa", "etaaaaaaaa", "ftaaaaaaaa", "gtaaaaaaaa", "htaaaaaaaa", "itaaaaaaaa", "jtaaaaaaaa",
                 "ktaaaaaaaa", "ltaaaaaaaa", "mtaaaaaaaa", "ntaaaaaaaa", "otaaaaaaaa", "ptaaaaaaaa", "qtaaaaaaaa",
                 "rtaaaaaaaa", "staaaaaaaa", "ttaaaaaaaa", "utaaaaaaaa", "vtaaaaaaaa", "wtaaaaaaaa", "xtaaaaaaaa",
                 "ytaaaaaaaa", "ztaaaaaaaa", "auaaaaaaaa", "buaaaaaaaa", "cuaaaaaaaa", "duaaaaaaaa", "euaaaaaaaa",
                 "fuaaaaaaaa", "guaaaaaaaa", "huaaaaaaaa", "iuaaaaaaaa", "juaaaaaaaa", "kuaaaaaaaa", "luaaaaaaaa",
                 "muaaaaaaaa", "nuaaaaaaaa", "ouaaaaaaaa", "puaaaaaaaa", "quaaaaaaaa", "ruaaaaaaaa", "suaaaaaaaa",
                 "tuaaaaaaaa", "uuaaaaaaaa", "vuaaaaaaaa", "wuaaaaaaaa", "xuaaaaaaaa", "yuaaaaaaaa", "zuaaaaaaaa",
                 "avaaaaaaaa", "bvaaaaaaaa", "cvaaaaaaaa", "dvaaaaaaaa", "evaaaaaaaa", "fvaaaaaaaa", "gvaaaaaaaa",
                 "hvaaaaaaaa", "ivaaaaaaaa", "jvaaaaaaaa", "kvaaaaaaaa", "lvaaaaaaaa", "mvaaaaaaaa", "nvaaaaaaaa",
                 "ovaaaaaaaa", "pvaaaaaaaa", "qvaaaaaaaa", "rvaaaaaaaa", "svaaaaaaaa", "tvaaaaaaaa", "uvaaaaaaaa",
                 "vvaaaaaaaa", "wvaaaaaaaa", "xvaaaaaaaa", "yvaaaaaaaa", "zvaaaaaaaa", "awaaaaaaaa", "bwaaaaaaaa",
                 "cwaaaaaaaa", "dwaaaaaaaa", "ewaaaaaaaa", "fwaaaaaaaa", "gwaaaaaaaa", "hwaaaaaaaa", "iwaaaaaaaa",
                 "jwaaaaaaaa", "kwaaaaaaaa", "lwaaaaaaaa", "mwaaaaaaaa", "nwaaaaaaaa", "owaaaaaaaa", "pwaaaaaaaa",
                 "qwaaaaaaaa", "rwaaaaaaaa", "swaaaaaaaa", "twaaaaaaaa", "uwaaaaaaaa", "vwaaaaaaaa", "wwaaaaaaaa",
                 "xwaaaaaaaa", "ywaaaaaaaa", "zwaaaaaaaa", "axaaaaaaaa", "bxaaaaaaaa", "cxaaaaaaaa", "dxaaaaaaaa",
                 "exaaaaaaaa", "fxaaaaaaaa", "gxaaaaaaaa", "hxaaaaaaaa", "ixaaaaaaaa", "jxaaaaaaaa", "kxaaaaaaaa",
                 "lxaaaaaaaa", "mxaaaaaaaa", "nxaaaaaaaa", "oxaaaaaaaa", "pxaaaaaaaa", "qxaaaaaaaa", "rxaaaaaaaa",
                 "sxaaaaaaaa", "txaaaaaaaa", "uxaaaaaaaa", "vxaaaaaaaa", "wxaaaaaaaa", "xxaaaaaaaa", "yxaaaaaaaa",
                 "zxaaaaaaaa", "ayaaaaaaaa", "byaaaaaaaa", "cyaaaaaaaa", "dyaaaaaaaa", "eyaaaaaaaa", "fyaaaaaaaa",
                 "gyaaaaaaaa", "hyaaaaaaaa", "iyaaaaaaaa", "jyaaaaaaaa", "kyaaaaaaaa", "lyaaaaaaaa", "myaaaaaaaa",
                 "nyaaaaaaaa", "oyaaaaaaaa", "pyaaaaaaaa", "qyaaaaaaaa", "ryaaaaaaaa", "syaaaaaaaa", "tyaaaaaaaa",
                 "uyaaaaaaaa", "vyaaaaaaaa", "wyaaaaaaaa", "xyaaaaaaaa", "yyaaaaaaaa", "zyaaaaaaaa", "azaaaaaaaa",
                 "bzaaaaaaaa", "czaaaaaaaa", "dzaaaaaaaa", "ezaaaaaaaa", "fzaaaaaaaa", "gzaaaaaaaa", "hzaaaaaaaa",
                 "izaaaaaaaa", "jzaaaaaaaa", "kzaaaaaaaa", "lzaaaaaaaa", "mzaaaaaaaa", "nzaaaaaaaa", "ozaaaaaaaa",
                 "pzaaaaaaaa", "qzaaaaaaaa", "rzaaaaaaaa", "szaaaaaaaa", "tzaaaaaaaa", "uzaaaaaaaa", "vzaaaaaaaa",
                 "wzaaaaaaaa", "xzaaaaaaaa", "yzaaaaaaaa", "zzaaaaaaaa"]
        expected = ['aaaaaaaaaa', 'azaaaaaaaa', 'baaaaaaaaa', 'bcaaaaaaaa', 'caaaaaaaaa', 'cbaaaaaaaa', 'cdaaaaaaaa',
                    'daaaaaaaaa', 'dcaaaaaaaa', 'deaaaaaaaa', 'eaaaaaaaaa', 'edaaaaaaaa', 'efaaaaaaaa', 'faaaaaaaaa',
                    'feaaaaaaaa', 'fgaaaaaaaa', 'gaaaaaaaaa', 'gfaaaaaaaa', 'ghaaaaaaaa', 'haaaaaaaaa', 'hgaaaaaaaa',
                    'hiaaaaaaaa', 'iaaaaaaaaa', 'ihaaaaaaaa', 'ijaaaaaaaa', 'jaaaaaaaaa', 'jiaaaaaaaa', 'jkaaaaaaaa',
                    'kaaaaaaaaa', 'kjaaaaaaaa', 'klaaaaaaaa', 'laaaaaaaaa', 'lkaaaaaaaa', 'mbaaaaaaaa', 'mnaaaaaaaa',
                    'naaaaaaaaa', 'noaaaaaaaa', 'oaaaaaaaaa', 'onaaaaaaaa', 'opaaaaaaaa', 'paaaaaaaaa', 'poaaaaaaaa',
                    'pqaaaaaaaa', 'qaaaaaaaaa', 'qpaaaaaaaa', 'qraaaaaaaa', 'raaaaaaaaa', 'rqaaaaaaaa', 'rsaaaaaaaa',
                    'saaaaaaaaa', 'sraaaaaaaa', 'staaaaaaaa', 'taaaaaaaaa', 'tsaaaaaaaa', 'tuaaaaaaaa', 'uaaaaaaaaa',
                    'utaaaaaaaa', 'uvaaaaaaaa', 'vaaaaaaaaa', 'vuaaaaaaaa', 'vwaaaaaaaa', 'waaaaaaaaa', 'wvaaaaaaaa',
                    'xwaaaaaaaa', 'xyaaaaaaaa', 'yaaaaaaaaa', 'yzaaaaaaaa', 'zaaaaaaaaa', 'zyaaaaaaaa']
        expected.sort()
        answer = self.findWords(board, words)
        answer.sort()

        self.assertEqual(expected, answer)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result: Set[str] = set()

        max_word_length = 0
        trie = Trie()
        for word in words:
            trie.insert(word)
            max_word_length = max(max_word_length, len(word))

        visited: Set[Tuple[int, int]] = set()
        word_so_far = []

        def dfs(row: int, col: int, node: TrieNode) -> None:
            if len(word_so_far) >= max_word_length:
                return

            visited.add((row, col))

            word_so_far.append(board[row][col])
            if node.is_end_of_word:
                word = "".join(word_so_far)
                result.add(word)
                trie.remove(word)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc

                if (
                    new_row < 0 or new_row >= len(board)
                    or new_col < 0 or new_col >= len(board[row])
                    or (new_row, new_col) in visited
                    or board[new_row][new_col] not in node.children
                    or node.children[board[new_row][new_col]].ref < 1
                ):
                    # out of bounds or already visited or no such path exists in trie
                    continue

                dfs(new_row, new_col, node.children[board[new_row][new_col]])
            word_so_far.pop()
            visited.remove((row, col))

        first_letters = set(trie.root.children.keys())
        for row in range(len(board)):
            for col in range(len(board[row])):
                if len(result) == len(words):
                    break

                letter = board[row][col]
                if letter in first_letters:
                    visited = set()
                    dfs(row, col, trie.root.children[letter])

        return list(result)
