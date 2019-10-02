import random

##Farm Fresh You-Won’t-Believe-It's-Not-Organic Dog Paste
##The snack that smiles back!
##13% satisfaction guarantee!

# ^^ you will not beleive it isn't organic!

nouns = ['blood','knives','gluten', 'feet', 'dairy', 'BBQ sauce', 'friendships', 'your hopes and dreams']
verbs = ['kill', 'energize', 'improve', 'create', 'dissolve', 'ruin', 'fix', 'bite', 'eat','fear']
firstnames = ['Abraham', 'Donald', 'Hillary', 'George', 'Taylor']
lastnames = ['Einstein', 'Tesla', 'Gates', 'Bezos']

def makeBaseWord():
    firstwords = ['Cheese',
                  'Computer',
                  'Animal',
                  'Vegetable',
                  'Car',
                  'Shoe',
                  'Foot',
                  'Toilet',
                  'Ear',
                  'Dog',
                  'Eye',
                  'Rust',
                  'Termite',
		  'Lettuce']
    
    secondwords = ['Slime',
                   'Spray',
                   'Dust',
                   'Paste',
                   'Spread',
                   'Pebbles',
                   'Mix',
                   'Paste',
                   'Residue',
                   'Crust',
                   'Rust',
		   'Bars ',
		   'Bricks']
    
    word = random.choice(firstwords) + ' ' + random.choice(secondwords)
    return word

def createWord():
    word = makeBaseWord()
    word = addPrefixes(word)
    word = addSuffixes(word)
    return word

def addPrefixes(word):
##    w = word
##    while True:
##        if random.randint(0, 2):
##            return w
##        else:
##            s = ['DIY-',
##                 'Organic ',
##                 'Canned ',
##                 'Freshly Baked ',
##                 'Farm Fresh ',
##                 "You-Won’t-Believe-It's-Not-",
##                 'Moisturizing ',
##                 'Original ',
##                 'Cheesy ']
##            w =  random.choice(s) + w
    s = ['DIY-',
         'Organic ',
         'Canned ',
         'Freshly Baked ',
         'Farm Fresh ',
         "You-Won’t-Believe-It's-Not-",
         'Moisturizing ',
         'Original ',
         'Cheesy ',
         'Crumbly ']
    if random.randint(0, 2):
        return word
    else:
        return random.choice(s) + word
        
def addSuffixes(word):
##    w = word
##    while True:
##        if random.randint(0, 2):
##            return w
##        else:
##            s = [' Maker',
##                 ' Replacer',
##                 ' Kit']
##
##            w = w + random.choice(s)
##        w = word
    s = [' Maker',
         ' Replacer',
         ' Kit']
    if random.randint(0, 2):
        return word
    else:
        return word + random.choice(s)

def getNoun():
    return random.choice(nouns)

def getVerb():
    return random.choice(verbs)

def getName():
    return firstnames[random.randint(0, len(firstnames)-1)] + ' ' +lastnames[random.randint(0, len(lastnames)-1)]

def getQuote():
    name = getName()
    quote = random.choice(['I use mine everyday!',
                           'Great product!',
                           'Don\'t buy this.',
                           'The best of it\'s kind!',
                           'Groundbreaking!',
                           'Yum' + random.choice(['.', '!', '?']),
                           'A true origonal.',
                           'Interesting...',
                           "It's ok I guess...",
                           "Full of surprises",
                           "Wait, am I suposed to say it's great?",
                           "I don't use this",
                           str(random.randint(0, 10)) + ' stars',
                           "Tastes like a combination of " + getNoun() + " and " + getNoun()])
    return "\"" + quote + "\" -" + name

def createSlogan():
    templates = {1:'Now with {}% {} {}',
                 2:'New look same great {}',
                 3:'Scientifically proven to {} {}', 
                 4:'{} great with {}',
                 5:'{} FREE',
                 6:'Just add water',
                 7:'Just add {}',
                 8:'{}/5 {} recommend',
                 9:'{} stars on {}',
                 10:'As seen {}',
                 11:'{}', 
                 12:'The perfect snack{}!', 
                 13:'The snack that {}s back!',
                 14:'The perfect gift for {}'}
    things = {1:[str(random.randint(0, 99)), random.choice(['more', 'less']), random.choice([getNoun(), makeBaseWord()])],
              2:[random.choice(['taste', 'smell'])],
              3:[getVerb(), getNoun()],
              4:[random.choice(['Works', 'Tastes', 'Smells']), makeBaseWord()],
              5:[getNoun().upper()],
              6:[],
              7:[getNoun()],
              8:[str(random.randint(-1,6)), random.choice(['Dentists', 'Mathematicians', 'Bioterrorists', 'Doctors', 'Criminal Masterminds', 'Virologists', 'Chemists', 'Lawyers', 'Kids', 'Idiots', 'Politicians', 'NSA employees'])],
              9:[str(random.randint(0, 11)), random.choice(['gMaol', 'gMail', 'Yelp', 'Yahoo', 'Amazon', 'Ebay', 'Etsy', 'Our Website', 'YouTube'])],
              10:[random.choice(['on TV', 'on the internet', 'on YouTube', 'on our billboards', 'on Facebook', 'in stores near you'])],
              11:[getQuote()], 
              12:['' if random.randint(0, 1) else random.choice([' for your kids', ' for the road', ' for armed robberies', ' for your enemies'])],
              13:[random.choice(['smile', 'bite', 'write', 'fight', 'smite', 'frown'])],
              14:[random.choice(['grandma', 'your kids', 'strangers', 'robbers', 'your weird uncle', 'your dog', 'your teacher', 'your accomplice', "your neighbor's first cousin twice removed's bestfrind's uncle in law"])]}
    sloganum = random.randint(1, len(templates))
    slogan = templates[sloganum]
    thing = things[sloganum]
    if sloganum == 5 and thing == ['your hopes and dreams'.upper()]:
        return 'FREE OF YOUR HOPES AND DREAMS'
    x = 0
    while x < len(thing):
        for i in range(len(slogan)-1):
            if slogan[i] == '{' and slogan[i+1] == '}':
                slogan = slogan[:i] + thing[x] + slogan[i+2:]
                x += 1
                break
    return slogan

def createDiscount():
    x = random.randint(1, 8)
    if x == 1:
        return "Buy " + str(random.randint(0, 6)) + " for the price of " + str(random.randint(0, 6)) + "!"
    elif x == 2:
        if random.randint(0, 1):
            return str(random.randint(-10, 50)) + "% off!"
        else:
            return str(random.choice([100, 47.27891, 3000, 167, 42, 0.01])) + "% off!"
    elif x == 3:
        return "Buy " + str(random.randint(0, 6)) + " get " + str(random.randint(0, 6)) + " free!"
    elif x == 4:
        return str(random.randint(0, 70)) + "% satisfaction guarantee!"
    elif x == 5:
        if random.randint(0, 1):
            return "Try it out for free for " + str(random.randint(0, 5)) + " days!"
        else:
            return "Try it out for free for " + str(random.randint(1000, 2000)) + " days!"
    elif x == 6:
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        return 'Get ' + str(x) + ' for free if you buy ' + str(y) + ' at the price of ' + str(x+y + random.randint(1, 3)) + '!'
    elif x == 7:
        return 'Get while supplies last'
    elif x == 8:
        return str(random.randint(-10, 50)) + "% off for our " + random.choice(['Christmas', 'Valentines Day', 'April Fools', 'Blueberry Day', 'National Eye Exam Month', 'National Welding Month', 'World Rat Day', 'Grilled Cheese Sandwich Day', 'Tax Day', 'Bat Appreciation Day']) + " sale"
    
print()

for i in range(9000):
    print(createWord())
    print(createSlogan())
    print(createDiscount())
    print()
