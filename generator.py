
import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['hackathon']
collection = db['politician']

robert = {
    'name': "Robert Francis Novak J.R.",
    'party': "Democrat",
    'years': "2010-2014",
    'title': "President of Rob's America",
    'summary': "Wants to make people run on hamster wheels for energy",
    'fun_fact': "Over hypes the drum solo to  'In The Air Tonight' by Phil Collins"
}

cindy = {
    'name': "Cindy Elanore Ochoa",
    'party': "Wall Builders United",
    'years': "1996-2014",
    'title': "Currator of Atomic Object",
    'summary': "Listens to short songs so she can get to the end",
    'fun_fact': "Can out rap and produce Kanye"
}

moose = {
    'name': "Mustafa Amir Jebara",
    'party': "Yes",
    'years': "2011-2019",
    'title': "Owner of Mufasa the Cat",
    'summary': "Makes really bad puns for fun",
    'fun_fact': "Lost every pushup contest hes ever been in"
}

# collection.insert(robert)
# collection.insert(cindy)
# collection.insert(moose)

collection = db['topic']

t1 = {
    'title': "Whats The Donald Up To",
    'keywords': ["Donald", "Trump"],
    'category': "President"
}

t2 = {
    'title': "Will Rocket Man Blow Up The World",
    'keywords': ["Kim", "Jung", "Un", "Rocket", "Man", "Elton", "John"],
    'category': "Defence"
}

t3 = {
    'title': "How Fake is Kim Kardashian's Ass?",
    'keywords': ["Kim", "Kardashian", "Fake", "Butt"],
    'category': "Future Leaders"
}

# collection.insert(t1)
# collection.insert(t2)
# collection.insert(t3)

collection = db['stories']

s1t1 = {
    'name': "Donald Trump Owns This Shutdown",
    'topic': "President",
    'content': "https://www.thenation.com/article/donald-trump-owns-this-shutdown/"
}

s2t1 = {
    'name': "Here Are the Promises President Trump Kept and Broke in His First Year",
    'topic': "President",
    'content': "http://time.com/5106302/donald-trump-first-year-promises/"
}

s3t1 = {
    'name': "The Donald Trump Show Wraps Up First Season",
    'topic': "President",
    'content': "https://www.huffingtonpost.com/entry/donald-trump-first-year_us_5a6232fae4b074ce7a07faaf"
}

s1t2 = {
    'name': "Making North Korea Great Again. How realistic are Kim's new year plans?",
    'topic': "Defence",
    'content': "http://www.cnn.com/2018/01/19/asia/kim-jong-un-speech-intl/index.html"
}

s2t2 = {
    'name': "North Korea cancels plans to send Kim Jong-un’s ex-lover to South Korea for diplomatic talks about Winter Olympics",
    'topic': "Defence",
    'content': "https://www.thesun.co.uk/news/5381355/north-korea-cancels-plans-kim-jong-un-ex-lover-south-korea-winter-olympics-talks/"
}

s3t2 = {
    'name': "Kim Jong Il's birthday poses propaganda opportunity",
    'topic': "Defence",
    'content': "http://www.dailynk.com/english/read.php?num=14957&cataId=nk01500"
}

s1t3 = {
    'name': "Kim Kardashian and Kanye West name newborn baby 'Chicago'",
    'topic': "Future Leaders",
    'content': "https://www.fox4now.com/entertainment/kim-kardashian-and-kanye-west-name-newborn-baby-chicago-"
}

s2t3 = {
    'name': "Kanye West ‘Dead Set Against’ Kim Kardashian Getting Butt Reduction Surgery",
    'topic': "Future Leaders",
    'content': "http://hollywoodlife.com/2018/01/17/kanye-west-against-kim-kardashian-butt-reduction-surgery/"
}

s3t3 = {
    'name': "Kim Kardashian Reveals Reason behind Huge Indent on her Butt!",
    'topic': "Future Leaders",
    'content': "https://www.albawaba.com/entertainment/kim-kardashian-reveals-reason-behind-huge-indent-on-her-butt%21-1066706"
}

collection.insert(s1t1)
collection.insert(s1t2)
collection.insert(s1t3)

collection.insert(s2t1)
collection.insert(s2t2)
collection.insert(s2t3)

collection.insert(s3t1)
collection.insert(s3t2)
collection.insert(s3t3)