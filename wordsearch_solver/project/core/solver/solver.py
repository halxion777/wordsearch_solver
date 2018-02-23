from typing import List


class WordSearchSolver:
    def __init__(self, puzzle: List[List[str]], items: List[str]):
        self._puzzle = puzzle
        self._items = items

    def solve(self):
        validators = [
            Top(),
            TopRight(),
            Right(),
            BottomRight(),
            Bottom(),
            BottomLeft(),
            Left(),
            TopLeft()
        ]
        stripped_items = {item.lower().replace(" ", "") for item in self._items}
        solver = _WordSearchSolver(self._puzzle, stripped_items, validators)
        return solver.solve()


class _WordSearchSolver:
    def __init__(self, puzzle: List[List[str]], items: List[str], validators: List[object]):
        self._puzzle = puzzle
        self._items = items
        self._validators = validators
        self._data_info = {
            "rows": len(puzzle),
            "cols": len(puzzle[0])
        }
        self._item_data = {item: len(item) for item in items}

    def solve(self):
        found_items = set()
        found_data = []
        if self._items:
            for row in range(self._data_info["rows"]):
                for col in range(self._data_info["cols"]):
                    diffs = self._items.difference(found_items)
                    if not diffs:
                        return found_data
                    for item in diffs:
                        for validator in self._validators:
                            if validator(self._puzzle,
                                         {"current": row, "len": self._data_info["rows"]},
                                         {"current": col, "len": self._data_info["cols"]},
                                         {"current": item, "len": self._item_data[item]}):
                                found_items.add(item)
                                found_data.append((row, col, item, validator.NAME))
                                break
        return found_data


data = [i.lower().split(" ") for i in """L I D F R E S H K Y F T U K O S F E D H A L F A R H O
X E H T Y E E D R O L Y P A A F L A F L A D S R E N X
C F U W H Y S Z E J T R A G K L I W B U D O S A V U B
S A J E R T C U M E J E Q A K E P O T J Y D A N U G A
O R T B I H Y L R D R E C H E R M I L S A G V C E L R
K Y R T W D G K A N S A S O L M Z H K I W D S H Q V R
A S D J L M U W F J U G T K I F A A J E T O P E N O E
J Y C O R E S T E N L O C M U K C L I W J M I R E D D
U M A F V T O Y B R E Z H L W O A G Q U L F F B O N T
R I N D C S K G E L Q B O K T S H E A T J D E D V C I
A S O Y B E A N S O P I C T A X G S L K G E X K L O G
L K F N O U C R T S Z M O J W O A R Q X B P U H S T E
A T J S E L Q W E C O N O M Y H B S O Y K I L D U M R
C M I R T B L E J N W E S C K O L U E T N U M S E L S
R G S V O E S H L O V N D I N R A N S A H O M E T H A
E L A R S L O P O F E H K A M S O F E K L Q R Y A T L
S J A N U T F D V S U G J A G H Y L X L D S H U E N A
Y R C T K T I L G Z S A H J W B K O I L M I L R H Y M
J P N S E I R Y H W O N B F K I F W O R L K U N W X A
X H U N M L E R F S I T O L A H J E K L O T E B R S N
S F O O D C H O M R L A R T K E H R I N L D G H O P D
W E S T E R N M E A D O W L A R K V M U T I Q N B E E
J L O A N U T I W Q N S A E S H J E C Y K L M O O S R
Q A V S Z L F X K S L R P D I S F I D V I U R D W S X
B O N R Y D S H O M E O N T H E R A N G E Q S O N H Y
J S K U T S B I N D G L E H U G O M E S Z I D A S I N
L E R D A V M E Z E M S D G A T Y L Z A D B V X U L W
W C U T T R E F A T A S J O R S M N F Y Q G O R T S E
H E R U O L Y I L S N O R E S I J S O W V R K S I K R
K T B E L A D W S O J X M U N V A X T P S A N N L M E
D O R G A G Z E X H W I L T Y D S R Y H M I R T U B D
E B U R F D E L T R U T X O B E T A N R O N E H W F N
F T T A F I S B E Y T M N Q L G S N E Y S V G O L P A
O P A X U R H E C R O F T S O M Y W C N I R A Z E R M
R E K T B O Y R C O R N X E R T S L K B O W Y D S T L
L Z H E S T G I F W K S O T N S E N Y S R U T X O N S""".splitlines()]

# data = [list(i) for i in """aaykakaykayykkaakayaaaykykyayk
# kyyakyaaaykaakkyakkkaaakaaykaa
# kkkyakakaykkykkykkakyaaaakaakk
# ykaakyaakkkkkayayyyyyaakaakkkk
# kkayyaakkyyayaakaakkaaykakkaak
# kkaaakaaakkakkkyaaaykyayakykaa
# kkykaaaaaaaaaakkaaakyyakakakky
# kkkkkkakyykyykkaayakaaakyakkaa
# kkkkakaykaayakyykkaykkkaaaaaka
# kkakakakaaakayaykakayyaykkakyy
# aaayakkkakkakykaykkakkykaakkyy
# ykkkykkyaaakkkkakaykkkkkaakkky
# kkakaykaakakkyyakayaakyaaaaaaa
# aaaakkyaakkaaykkaaayayakyakayk
# akkkkkaykaaykykakyaakkykkkkkka
# kykaakkyaykakkkykakayaykyaaakk
# kayykkakykayaakayaayyyakkykykk
# kkkkakayaaakkayaykkyakaaaaykay
# aykakkkaakakayaaakkykkaykayayy
# kyaykayakakyykykakaaykykkaykak
# akakkakkakkkkaaakyyyykakaaaaak
# kakyykakkykyakyaaaaakakayaakka
# kkaaakkakakkaakayaayaaakkaayya
# kkkkyykkayaykkakkyykykykkaaaka""".splitlines()]
#
# data = [list(i) for i in """oobonoobbonononobboonnbbnnnooonbbbn
# boooobbbnnonnnbnoonnbnnoobbnbnnobon
# bbbbnbnnbnobbnnbbnnobbnbooobbnbonon
# bnnbbononnobnonobbobnbnbobonbbnonnn
# obnnbnbbonobbnnonbonnonnonoonobonnb
# bnoboonnonnbononobonnbbbbnooonnnooo
# bbbbnbnbbnnnonobnnnobnbnobbonnnbnbo
# noonoboobonbnobbnnobnnbbnbbnnbonnbn
# boonobonnobbobnonnnbonbbbobbobnnoob
# bnnbnbboboonobnoonnnbnnboboonnobnob
# nnobnoonnnnnbnnbbobononnbnbooonooon
# onoonbbooonnobbboobbbbbonboonbbobnb
# nbbnnooobnnobbnoonbbobnbbnnonnonnbo
# onnbbnnnoonnnonbbbnobnonoboonnbnobn
# nbbobnbbbnnbbbbnbbbbnbnbboonnnbnnoo
# bbbonbobonnooonobonnbbnobnnnnbboooo
# onbboonbnnbnnnnboobbobbbononbbnoobb
# oooonooooobobnnonbnnonoobonnbnnnooo
# obbnonobbbbobbonbbbnobobbnonobnbbnb
# nnobnboobnbononnbnoobbnbnbnnbnnbnnb
# nnnobononbonbobnnonbbnbbbobbonobnbn
# bnononobbbobnnbbbbnoobnnonbobnoonnb
# bonobbnbbboobnbnoonbbnoonobbbbnbbon
# bonoonnbbnobbbbobbbnbnbnnbooobbonbn
# obnbonoonnnobbonobbbbnnobnnnnbnoboo
# obbobbooonboboboonobbnbboobboonobbb
# ooobbbonbnbnnnobbboonnobnbnbobbbbno
# bbnbbnbonbbbooonbnbooonobnnbbnonobo
# obonnnooobnnooobnnbnnnooobonnnbbnbb
# bbnoonnnnobnbnonbboononnonnnbbbbonn""".splitlines()]

data = [line.split() for line in """N	E	W	M	E	X	I	C	O	O	S	A	K	S	A	R	B	E	N	H	E	F	Y
A	S	U	C	Y	W	E	S	T	V	I	R	G	I	N	I	A	M	L	F	T	Q	I
S	E	O	H	A	D	I	M	J	C	P	E	N	N	S	Y	L	V	A	N	I	A	B
H	S	A	S	N	A	K	I	L	I	O	M	A	I	N	E	W	Y	O	M	I	N	G
V	H	I	K	R	N	Y	S	P	H	V	N	O	O	D	A	R	O	L	O	C	T	D
H	M	T	R	S	I	E	S	M	X	Y	O	N	S	H	J	G	Y	A	A	R	E	H
I	I	W	O	O	L	S	I	O	P	K	I	O	E	R	F	V	I	I	B	L	V	V
N	N	O	Y	U	O	R	S	N	F	R	H	R	Y	C	V	L	G	H	A	K	J	L
D	N	V	W	T	R	E	S	T	E	V	O	T	A	E	T	R	O	W	C	Y	Z	A
I	E	U	E	H	A	J	I	A	M	W	N	H	T	N	O	I	A	R	K	I	T	G
A	S	T	N	D	C	W	P	N	O	E	H	C	E	E	A	R	C	C	I	O	M	A
N	O	J	Q	A	H	E	P	A	V	A	I	A	G	E	E	I	U	U	K	D	C	J
A	T	H	Y	K	T	N	I	A	E	L	N	R	M	O	S	T	S	A	T	A	A	A
P	A	E	D	O	U	S	D	W	L	O	S	O	K	P	N	S	D	I	L	Y	M	O
I	W	X	I	T	O	A	I	I	A	X	D	L	Z	E	S	H	E	I	U	A	N	R
A	R	S	L	A	S	S	N	K	Q	K	A	I	K	I	T	H	F	N	B	O	X	E
W	H	U	J	D	C	O	O	M	M	H	S	N	D	R	R	O	I	A	N	J	L	G
O	S	D	O	O	I	U	J	F	O	K	B	A	O	I	R	A	L	R	K	E	O	O
I	S	V	N	S	V	E	R	M	O	N	T	N	L	N	R	A	Q	T	E	C	T	N
T	Z	S	U	R	S	H	A	W	A	I	I	E	I	A	A	R	K	A	N	S	A	S
V	I	W	A	S	H	I	N	G	T	O	N	A	L	X	D	N	A	L	Y	R	A	M
N	W	N	T	L	B	N	M	N	R	R	H	O	D	E	I	S	L	A	N	D	E	C
H	A	T	U	S	T	T	E	S	U	H	C	A	S	S	A	M	X	S	A	X	E	T""".splitlines()]

print("""ALABAMA
LOUISIANA
OHIO
ALASKA
MAINE
OKLAHOMA
ARIZONA
MARYLAND
OREGON
ARKANSAS
MASSACHUSETTS
PENNSYLVANIA
CALIFORNIA
MICHIGAN
RHODE ISLAND
COLORADO
MINNESOTA
SOUTH CAROLINA
CONNECTICUT
MISSISSIPPI
SOUTH DAKOTA
DELAWARE
MISSOURI
TENNESSEE
FLORIDA
MONTANA
TEXAS
GEORGIA
NEBRASKA
UTAH
HAWAII
NEVADA
VERMONT
IDAHO
NEW HAMPSHIRE
VIRGINIA
ILLINOIS
NEW JERSEY
WASHINGTON
INDIANA
NEW MEXICO
WEST VIRGINIA
IOWA
NEW YORK
WISCONSIN
KANSAS
NORTH CAROLINA
WYOMING
KENTUCKY
NORTH DAKOTA""".splitlines())

if __name__ == "__main__":
    import pprint

    test = [
        ["p", "s", "p", "r"],
        ["l", "l", "r", "d"],
        ["l", "m", "e", "t"],
        ["e", "e", "z", "h"],
        ["h", "z", "n", "i"]
    ]
    test = data
    # words = set(["acres",
    #          "food",
    #          "soil",
    #          "agriculture",
    #          "grain",
    #          "sorghum",
    #          "alfalfa",
    #          "homeontherange",
    #          "soybeans",
    #          "barred",
    #          "tiger",
    #          "salamander",
    #          "honeybee",
    #          "buffalo",
    #          "january",
    #          "sunflower",
    #          "cattle",
    #          "kansas" ,
    #          "topeka",
    #          "corn",
    #         "konza",
    #         "cottonwood",
    #         "littlebluestem",
    #         "westernmeadowlark",
    # "economy",
    # "ornate",
    # "box",
    # "turtle",
    # "wheat",
    # "farmer",
    # "rancher",
    # "windmill"])
    words = {"AGREE"}



    # solver = WordSearchSolver(test, words)
    # found = solver.solve()
    # print(f"words: {len(words)} found: {len(found)}")
    # found_set = {i[2] for i in found}
    # print(words.difference(found_set))
    for i in test:
        print(i)
    # pprint.pprint(found)


