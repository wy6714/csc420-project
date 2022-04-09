# Project: Boggle Solver

## Preliminaries

In this project, the goal is to implement linked list and hash map data structures in Python and to recursively perform a depth first search on a tree.

### Development Environment

You should develop your code using Python 3+. You will also need the numpy package. 


## Data Structure Implementations

You will be implementing two basic data structures as part of this project: a Linked List and a Hash Table (or Hash Map). 

### Linked List

The Linked List you will complete only requires forward pointers on its nodes, and the `add(item)` method, that is, put a new node on the front of the list. Each node in the list stores a string value. There is no need for the list to be generic. The linked list will also have a `contains(item)` method to check if an item is contained in the list. 

### Hash Map

The HashMap data structure is simply a membership Hash Table --- unlike a truly generic HashMap that stores key, value pairs, this table returns `True` if an items is stored in the data structure and `False` otherwise. Put another way, it's a HashMap that maps a string value to `True`. The HashMap you will implement only needs to store strings. It has the following member functions:

* `add(string) -> void` : add a string to the HashMap
* `contains(string) -> boolean` : check to see if a string is in the HashMap, return `True` if present, else `False`. 

The HashMap should be implemented as a hash table with *separate chaining*. This means that when two elements collide at an index, you add the item on to that spot, using a Linked List. 

Following that model, your HashMap should have an array (or buckets) of Linked Lists. After achieving the hash value for a given string (modulo the range of buckets), you `add()` that string onto the Linked List at that index associated with the hash value. Critically, the performance of the HashMap depends on the length of the lists of each bucket  --- if the lists get too long, then the look up operation could become O(n)! That would be quite slow ...

The *load* on a hash table is defined as the number of items stored in the table divided by the number of buckets. High loads means longer lists at each bucket and worse performance. To keep performance steady, once the load reaches 0.75, you have to resize the hash table by doubling the number of buckets and reinserting all the items into their new hash locations. **YOU MUST IMPLEMENT A RESIZE ROUTINE -- YOU CANNOT SIMPLY SET YOUR NUMBER OF BUCKETS TO A LARGE VALUE!!** 

> A quick aside: Since the HashMap only maps to true/false we could also describe this as an implementation of a set. That is, we are only concerned with set membership. Is the item in the set, or not?

### Data Structure Implementation

The crucial part of this project is the data structure implementations. 

#### Linked List

The file `linked_list.py` defines a `ListItem` (aka. a node) as:

```python
class ListItem:
    def __init__(self):
        self.data = None
        self.next = None
```

There are two methods that operate on LinkedList, shown below. In `linked_list.py` you implement these methods. 

```python
    def add(self, item):
        """
        Method to add a new item to the *front* of the linked list.
        :param item: The item to add to the list.
        """
        # TODO: Your code goes here.
```
and
```python
    def contains(self, item):
        """
        Method to determine if an item is contained in the list.
        :param item: The item to check if it is contained in the list.
        :return: boolean, True if item is in the list. False otherwise.
        """

        # TODO: Your code goes here.
```

### Hash Map

The HashMap data structure is defined in `hash_map.py`.

There are four methods that operate on `HashMap`, shown below. In `hash_map.py` you implement these methods. 

The resize method.
```python
    def resize(self):
        """
        Method to resize the hash table.

        Called by the add method if the number of items in the hash map
        divided by the number of buckets is greater than the maximum load factor.
        """
        # TODO: Your code goes here.
```

The add method.
```python
    def add(self, value):
        """
        Method to add a value to this HashMap.

        NOTE: This method should call the resize method
        if the number of items in the hash map divided by the number of buckets
        is greater than the maximum load factor.

        :param value: The string value to add to the HashMap.
        """
        # TODO:  Your code goes here.
```

The contains method.
```python
    def contains(self, value):
        """
        A method to check if the value is contained within this HashMap.
        :param value: The value to check.
        :return: boolean, True if the value is contained in the HashMap, False otherwise.
        """
        # TODO: Your code goes here.

```

The convert to linked list method.

```python
    def to_linked_list(self):
        """
        Method to convert the HashMap to a LinkedList.
        :return: A linked list containing all items in this HashMap.
        """
        # TODO: Your code goes here.
```


### Spell Checker (40 points)

To help test your `HashMap` and `LinkedList` implementation, we've provided a simple interactive spell checker program that allows the user to type phrases (without punctuation) and it will spell check it. Here's some sample inputs and outputs, along with the compilation. 

```
$ python spell_check.py 
spellcheck > spellcheck all these words at once
SPELLCHECK -> not a word
ALL -> WORD
THESE -> WORD
WORDS -> WORD
AT -> WORD
ONCE -> WORD
spellcheck > or
OR -> WORD
spellcheck > one
ONE -> WORD
spellcheck > at
AT -> WORD
spellcheck > a
A -> WORD
spellcheck > time
TIME -> WORD
spellcheck > this adfasdfasdf is not a word
THIS -> WORD
ADFASDFASDF -> not a word
IS -> WORD
NOT -> WORD
A -> WORD
WORD -> WORD
spellcheck > nor !!! 
NOR -> WORD
!!! -> not a word
spellcheck > 
$ # type ^D to insert EOF to exit
```


### Boggle Solver (60 points)

Now that your `HashMap` and `LinkedList` are working, let's use them to do something a bit more interesting --- finding all the words on a Boggle board! 

The Boggle game structure and functions are defined in `boggle.py` and you will do all of your work in `boggle.py`. A boggle instance is defined as a 5x5 grid of dice, where each dice displays a different character. 

```python
        # Store the dictionary for later use.
        self.dictionary_hash_map = dictionary_hash_map

        # Initialize an empty boggle board as a two dimensional array of size boggle dimension.
        self.boggle_board = np.empty((BOGGLE_DIMENSION, BOGGLE_DIMENSION), dtype='object')

```

When printed the board looks like
```
.-----------.
| S N T A Y |
| W N T E I |
| N QuI H I |
| N F O S U |
| E E H N L |
'-----------'
```

The goal is to find as many words (at least three letters long) by traversing from one dice to another in all directions (left, right, up, down, and diagonal) without using a dice more than once. So for example `QUIT` is a word found on the board, and so is  `QUITE`. (You get a free 'U' for your 'Q'.)

A number of functions are implemented and provided for you in `boggle.py`, your main work will be completing the `boggle_all_words()` function, which will search the Boggle board for all words 3 letters to 8 letters in length. 

This is a recursive method that will explore outwards from a letter tile using **depth first search**. The idea is that you start a tile, like `S` and then try all neighbors (via a recursive call), outward, adding letters as you go and checking to see if you found a word. At somepoint you either search off the board or descended too far (checking a 9 letter word), and the recursion returns to explore another path. An algorithmic description is provided in a comment within `boggle.py` --- see there for more details.

Once you complete, you can run the `one_player_boggle.py` program at a given random seed, like the two examples below:

```
$ python one_player_boggle.py 10
.-----------.
| U E R N C |
| L G T M E |
| T U R T A |
| T H S I H |
| X A I L E |
'-----------'
TEN
LET
HAILS
TENT
SAIL
TEA
RILE
LEI
SHRUG
LEG
MEATS
TUG
AISLE
RUST
HAIR
LUG
HAIL
RUSH
AMEN
GUST
MEAT
SAX
LISTEN
SAT
GUSH
GRITS
MET
LUTE
MAIL
THRU
STAMEN
MEN
SHUT
LITHE
MATTE
AILS
HITTER
LUST
CENT
THAT
HATTER
GRIST
LUSH
GERM
TAX
STILE
TAM
NET
MAILS
EMAIL
HIT
HIS
ETA
TRUTHS
HIE
NEATH
GRIT
STIR
SHAT
SITE
SLIT
HIRSUTE
HASTEN
MAT
HITS
TRITE
THEIR
ERG
EAT
HATS
GET
STEAM
ENTRUST
GEL
AIR
HATE
STAIR
GUT
AIL
MATT
ITEM
MATS
SURGE
ASTIR
MATH
HUGER
MATE
RULE
RITE
HUT
GELT
HEIR
HUG
RULER
STEM
TAME
MATTER
SIT
SIR
ENTER
HAIRS
TILE
LITE
HUGE
THIS
LIST
SHUTTLE
TUSH
HIATUS
ITS
SITTER
CENTRIST
HAT
HAS
TASTE
LIT
NETS
HAM
ELITE
ATE
RUT
STRUT
TIE
TERN
TERM
HASTE
AIRS
LIE
RUG
LEIS
MATRIEL
TEAM
THEIRS
THRUST
EMAILS
ASH
CENTER
THE
TAIL
HEIST
AIRMEN
TRUTH
GLUT
ENTRE
SLITTER
URGE
TRUST
GLUE
HEIRS
NEAT
LITTER
HURTS
ISLE
EATS
THUS
HURT
THUG
TAILS

Total Points: 251

```

```
$ python one_player_boggle.py 12
.-----------.
| H U A E H |
| E U D N Y |
| E L R G E |
| P T E D T |
| P W QuS A |
'-----------'
TEN
LET
LES
DEW
TEE
ELEGY
LEG
DEN
PETER
LEE
LED
TEND
ANGER
ANGEL
HEAD
GETS
WEDS
DUH
REST
DUE
EDGY
TERNED
ANY
DELUDE
HURTLE
SAT
DREW
EDGE
TADS
PLEDGE
HURDLE
AND
SAD
HEADREST
URNED
WEST
DATE
EEL
PELTED
PLED
HURDLES
LEST
ADULT
DUELED
ELUDE
TRUE
DEANED
HURDLED
HURTLES
LUAU
NET
LURE
HURTLED
URGES
TAD
RESTED
ETA
URGED
GENRE
PEEL
URN
GENRES
GRUELED
DREDGE
ENDURES
WET
HELP
SATE
LEPT
DRUDGE
ERG
ENDURED
GET
WED
HELD
GEL
TRUDGE
SERGE
PETREL
GENE
DUET
SEDATE
PET
RULE
HEY
PEELED
DUEL
GRUEL
HEN
PEE
HEDGES
GELT
HURLED
SATED
QUESTED
HEDGED
GREW
HUE
RULES
WELT
GELD
RULED
YET
WELD
YEN
QUEST
END
YEA
TESTED
ENDURE
EGRET
WEDGE
TEST
SEDGE
ADS
WESTED
ENDUE
TRUDGES
TRUDGED
DRUDGES
NETS
ATE
RED
DEAN
TERN
HEEL
RUE
LURES
EYED
LURED
SEW
SET
PELT
URGE
EDGES
EDGER
EDGED
DANGER
EYE
HURT
LEGEND
DENY
LEDGE
HYENA
HURL
HEDGE
RUDE
HEELED
REDS

Total Points: 281
```


> Note that the words are not alphabetical because hash tables are not ordered data structures.


## Bonus: Ordered Output (15 points)


Update your data structure (perhaps using a BST?) such that the output of the words from your boggle solver is in alphabetical order.



