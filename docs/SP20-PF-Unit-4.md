# Unit 4: Programming Fundamentals — Building a Search Engine

**Course:** BSCS/BSDS/MCS-EA 1st  
**Instructor:** Muhammad Ateeq, Asst. Prof. of CS @ The IUB  

*Source material credits: Dave Evans and Udacity*

---

## WHAT: In the previous units we learned how to extract the first link, and then all the links from a
webpage, and completed the web crawler. In unit 4 you are going to learn how to finish the code for your
search engine and how to respond to a query when someone wants the (available) web pages that
correspond to a given keyword.

## Introduction
The main new computer science idea you will learn is how to build complex data structures. You
will learn how to design a structure that you can use so that you can respond to queries without
needing to rescan all the web pages every time you want to respond to a query. The structure you
will build for this is called an index. The goal of an index is to map a keyword and where that
keyword is found. For example, in the index of a book you can see a page number which serves as a
map to where a term or concept can be found. The key ideas in index will allow us to find references
to what we want. With a search engine the index gives you a way for a keyword to map to a list of
web pages, which are the urls where those particular web pages appear. Once you have done the
work of building an index, then the look-ups are really fast.

### Q-1: Quiz (Data Structures)
Deciding on data structures is one of the most important parts of building software. As long as you
pick the right data structure, the rest of the code will be a lot easier to write.
Which of these data structures would be a good way to represent the index for your search engine?

    a. [<keyword1>, <url1, 1>, <url1, 2>, <keyword2>, …]

    b. [[<keyword1>, <url1, 1>, <url1, 2>], [<keyword2>, <url2, 1>, …]

    c. [[<url1, 1>, [<keyword1>, <keyword23>, … ]], [<url2, 1>, [<keyword2>, …]]

    d. [[<keyword1>, [<url1, 1>, <url1, 2>]], [<keyword2>, [<url2, 1>]], …]

The best choice is d, and b is a close runner up. Choices a and c would be really difficult. Here's why:

a - Hard to read because everything is all in one list. This structure will also make it hard to loop
over the keywords.

b - This option is okay, but not as good as d. The structure of b is such that there is a list, where each
element of the list is a list, and the element lists are themselves lists. The big advantage to this

Credits: Dave Evans and Udacity                                                                          1

---

structure is that it is easy to tell the keywords from the urls, the keyword is always the first element
of the list. It is also easier to go through the keywords because for each list you just have to look to
the first element, check to see if it is the keyword you are looking for, and if not, move on to the next
one. The only downfall to this structure is that the distinction between the keywords and the urls
could be even more clear.

c – While this has more structure, but it does not make it easy to look up the pages where a
keyword appears. To look for a particular keyword you would have to look in each entry, look in the
second part of the entry, scan it to see if the keyword appears, if it does then you want the url in
your result, and if it doesn't then that url is not in the result. This option is not the best because you
would have to scan through all the pages, which would take too much time.

d- In this structure there are just two elements in the inner list; the keyword followed by a list of urls.
This is the best option because it makes a very clear separation between the keyword and the list of urls.
It also means that if you decide you want to keep track of something else, like the number of times
someone searches for each keyword, you can easily do that by adding an extra element. This is
something that would be more difficult to do with the structure of option b.

Credits: Dave Evans and Udacity                                                                          2

---

## Add to Index
### Q-2: Quiz (Add to Index)
Define a procedure, add_to_index, that takes three inputs:
      - an index [[<keyword>, [<url>, …]], …]
      - a keyword string
      - a url string
If the keyword is already in the index, add the url to the list of urls associated with that keyword.
If the keyword is not in the index, add an entry to to the index: [keyword, [url]]
For example:
     index = []
     add_to_index(index, 'udacity', 'http://udacity.com')
     add_to_index(index, 'computing', 'http://acm.org')
This code starts with the empty list index. After the two lines of code the empty list will contain
two lists beginning with the keywords, udacity and computing.
      index = []
      add_to_index(index, 'udacity', 'http://udacity.com')
      add_to_index(index, 'computing', 'http://acm.org')
      add_to_index(index, 'udacity', 'http://npr.org')
In this code, udacity is already in the index and you don't want to add a new entry to the index
itself. Since udacity is already in the index, what you want to do is add the new url to the list
already associated with that keyword.

So here is how it goes:
def add_to_index(index, keyword, url):
       for entry in index: # loop through the elements of index, giving
       each one the name entry
               if entry [0] == keyword: # test to see if the value at position 0
               of entry identical to the keyword that's passed in
                        entry[1].append(url) # if it is equal you want to append
                        the url to the list of urls associated with that entry
                        return # stop the loop
               #not found, add new entry
If the keywords are not found, you want to add a new entry. The new entry is going to have as its
value a list containing two elements, the keyword and the second element will be a list containing
the urls that were found that have that keyword. So far, there is only one url that was passed in to
index. To do this, add to your code:
def add_to_index(index, keyword, url):
      for entry in index:
            if entry [0] == keyword:

Credits: Dave Evans and Udacity                                                                         3

---

                      entry[1].append(url)
                      return # stop the loop
          index.append([keyword, [url]])
Let’s test the procedure with the procedure calls given above.

## Lookup Procedure
### Q-3: Quiz (Lookup)
Define a procedure, lookup, that takes two inputs:
     -    An index: A list where each element of the list is a list containing a keyword and a list as its
          second element. The second list element is a list of urls where that keyword appears.
     -    The keyword to lookup
The output should be a list of the urls associated with the keyword. If the keyword is not in the
index, the output should be an empty list.
For example:
         lookup(index, 'udacity') → ['http://udacity.com', 'http://npr.org']
Here it is:
         def lookup(index, keyword): # two parameters
           for entry in index: # loop through the entries in the index
             if entry [0] == keyword:
                 return entry [1] # if found then return the urls associated
                                   with that entry
           return [] # if no keyword is found, then return empty list
Try this in the interpreter:
        def lookup(index, keyword):
                 for entry in index:
                        if entry [0] == keyword:
                              return entry [1]
                 return []
Trying this procedure on our pre-buit index will result in:
          print(lookup(index, 'udacity'))
          ['http://udacity.com', 'http://npr.org']

## Building the Web Index
To build your web index you want to find a way to separate all the words on a web page. It is
possible to use the concepts you've already seen to build a procedure to do this, however, Python
has a built-in operation that will make this much simpler.
Split. When you invoke the split operation on a string the output is a list of the words in the string.
      <string>.split()
      [<word>, <word>, … ]
For example,
         quote = " Programs must be written for people to read, and only
         incidentally for machines to execute. --- Harold Abelson"
         print(quote.split())

Credits: Dave Evans and Udacity                                                                           4

---

      ['Programs', 'must', "be", 'written', 'for', 'people', 'to', 'read,',
          "and", 'only', 'incidentally', 'for', 'machines', 'to', 'execute.',
          '---', 'Harold', 'Abelson']
This operation does a pretty good job of separating out the words in the list so that they will be
useful. However, in the case of 'read,'which was followed by a comma in the quote, for the
keyword you would not want to include the comma. While this isn't perfect, it is going to good
enough for now.

Here is another example of how split works, using triple quotes ("""). Using the triple quotes you
can define one string over several lines:
      quote = """
             Walking on water and developing software from a
             specification are easy if both are frozen.
                   (Edward V. Berard)
                   """
      print(quote.split())
      ["Walking", 'on', 'water', 'and', 'developing', 'software',
      'from', 'a', 'specification', 'are', 'easy', 'if', 'both', 'are',
      'frozen.', '(Edward', 'V.', 'Berard)']
This still has similar problems to the first example, where the parentheses are included in the
word '(Edward'.

### Q-4: Quiz (Add Page to Index)
Define a procedure, add_page_to_index, that takes three inputs:
    - index
    - url (string)
    - content (string)
It should update the index to include all of the word occurrences found in the page content by
adding the url to the word's associated url list.
For example:
      index = []
      add_page_to_index(index, 'fake.test', "This is a test")
      print(index)
      [['This', ['fake.test']], ['is', ['fake.test']], ['a',
      ['fake.test']], ['test', ['fake.test']]]
Printing at index[0] :
      print(index[0])
      ['This', ['fake.test']]
Printing at index[1] :
      print(index[1])
      ['is', ['fake.test']]

Now, add a page called real.test, after fake.test:

      index = []

Credits: Dave Evans and Udacity                                                                      5

---

      add_page_to_index(index, 'real.test', "This is not a test")
      print(index)
      [['This', ['fake.test', 'real.test']], ['is', ['fake.test',
      'real.test']], ['a', ['fake.test']], ['test', ['fake.test',
      'real.test']], ['not', ['real.test']]]
Have a look at the entries when you index[1]:

      print(index[1])
      ['is', ['fake.test', 'real.test']]
Have a look at the entries when you index[4]:
      print(index[4])
      ['not', ['real.test']]
You have already defined a procedure for responding to a query, so check out if it works on this
index, searching for the keyword 'is':
      index = []
      add_page_to_index(index, 'fake.test', "This is a test")
      add_page_to_index(index, 'real.test', "This is not a test")

      print(lookup(index, 'is')) # you should expect to see that this
      keyword appears on both pages
      ['fake.test', 'real.test']
Now try searching for a keyword, 'udacity,' that is not in either of the urls:
      print(lookup(index, 'udacity')) # you should expect to see an empty
      list []
Well, that was successful! Try to define this procedure.
The goal is to define a procedure, add_page_to_index, which takes in three inputs, the index, the
url and the content at that url. This takes two steps:
    1. split the page into its component words,
    2. then add each word along with the url to the index.

The split method divides the content into its component words, while the procedure,
add_to_index adds a word and a url to the index. However, this is not sufficient to satisfy the
second step. You still need to do this for each of the words found during the first step. A for loop
will take care of this. Remember that the point of this procedure is to modify the index, so there will
be no return results.

This is how you can put the code together using this structure. Use the split method to divide
the content into its component words and store them in the words variable.
      def add_page_to_index(index,url,content):
          words=content.split()
Go through each of the words in words, which we can do using a for loop, and naming the variable
word:

Credits: Dave Evans and Udacity                                                                      6

---

       def add_page_to_index(index,url,content):
             words=content.split()
             for word in words:
adding each of the words to the index by calling add_to_index and passing in the index, the
word and the url.
       def add_page_to_index(index,url,content):
             words=content.split()
             for word in words:
                  add_to_index(index, word, url)
Note that if a word occurs more than once on the same page, we’re going to keep adding it to the
index each time. This means there might be more than one occurrence of the same url in the list of
urls associated with a keyword. Depending on what we want our search engine to do and how we
want our it to respond to queries, this may or may not be a good thing. It will be discussed further
in a later class.
To try this code in the python interpreter, you’ll need the three procedures from earlier. These are
printed below, followed by a reminder of what each procedure does and then some examples you
can try out for yourself.
       def add_to_index(index,keyword,url):
             for entry in index:
                  if entry[0] == keyword:
                      entry[1].append(url)
                      return
             #not found, add a new entry
             index.append([keyword,[url]])

      def lookup(index,keyword):
          for entry in index:
              if entry[0]==keyword:
                  return entry[1]
          return []

      def add_page_to_index(index,url,content):
          words=content.split()
          for word in words:
              add_to_index(index, word, url)
First, the add_to_index procedure takes in the index, a keyword and a url. It goes through the
entries in the index, checking to see if it already contains the keyword. If it does, it appends the url
to the entry that matches the keyword . If the keyword is not found, the procedure adds a new
entry to the index that is a list of the keyword and the single url: [keyword, [url]] .
Next, the lookup procedure takes an index and a keyword. It looks at each entry [<keyword>,
[<list of urls>]] in the index to see if the keyword you’re looking for is at the first position
of the entry. If it is, it returns the list of urls which corresponds to that keyword.
Finally, add on the add_page_to_index procedure you just defined.
Examples:
1. Here is the same example from before:

Credits: Dave Evans and Udacity                                                                       7

---

      index=[]
      add_page_to_index(index,'fake.test',"This is a test")
      print index

      index=[]
      add_page_to_index(index,'not.test',"This is not a test")
      print index
      [['This', ['fake.test']], ['is', ['fake.test']], ['a',
      ['fake.test']], ['test', ['fake.test']]]
      [['This', ['not.test']], ['is', ['not.test']], ['not',
      ['not.test']], ['a', ['not.test']], ['test', ['not.test']]]

2. To convince yourself that the code is working, here’s a more complex example using a quotation
from Scott Adams on dilbert.com, followed by one from Randy Pausch.

      index=[]
      add_page_to_index(index, 'http://eatthis.com',
                """
                Another strategy is to ignore the fact that you are
                slowly killing yourself by not sleeping and
                exercising enough. That frees up several hours a
                day. The only downside is that you get fat and die.
                 --- Scott Adams on Time Management
                 """)
      add_page_to_index(index, 'http://libquotes.com',
                """
                Good judgement comes from experience, experience
                comes from bad judgement. If things aren't going
                well it probably means you are learning a lot
                and things will go better later.
                    --- Randy Pausch
                """)
      print(index)
      [['Another', ['http://eatthis.com']], ['strategy', ['http://eatthis.com'] ],
      ['is', ['http://eatthis.com', 'http://eatthis.com']], ['to', ['http://
      dilbert.com']], ['ignore', ['http://eatthis.com']], ['the', ['http://
      dilbert.com']], ['fact', ['http://eatthis.com']], ['that', ['http://
      dilbert.com', 'http://eatthis.com']], ['you', ['http://
      dilbert.com', 'http://eatthis.com', 'http://libquotes.com']], ['are',
      ['http://eatthis.com', 'http://libquotes.com']], ['slowly', ['http://
      dilbert.com']], ['killing', ['http://eatthis.com']], ['yourself',
      ['http://eatthis.com']], ['by', ['http://eatthis.com']], ['not', ['http:/
      /dilbert.com']], ['sleeping', ['http://eatthis.com']], ['and', ['http://
      dilbert.com', 'http://eatthis.com', 'http://libquotes.com']], ['exercising',
      ['http://eatthis.com']], ['enough.', ['http:// dilbert.com']], ['That',
      ['http://eatthis.com']], ['frees', ['http:// dilbert.com']], ['up',
      ['http://eatthis.com']], ['several', ['http:// dilbert.com']], ['hours',
      ['http://eatthis.com']], ['a', ['http:// dilbert.com',
      'http://libquotes.com']], ['day.', ['http://eatthis.com']], ['The',

Credits: Dave Evans and Udacity                                                                     8

---

      ['http://eatthis.com']], ['only', ['http://eatthis.com']], ['downside',
      ['http://eatthis.com']], ['get', ['http://eatthis.com']], ['fat',
      ['http://eatthis.com']], ['die.', ['http://eatthis.com']], ['-- -',
      ['http://eatthis.com', 'http://libquotes.com']], ['Scott', ['http://
      dilbert.com']], ['Adams', ['http://eatthis.com']], ['on', ['http://
      dilbert.com']], ['Time', ['http://eatthis.com']], ['Management', ['http:/
      /dilbert.com']], ['Good', ['http://libquotes.com']], ['judgement',
      ['http://libquotes.com']], ['comes', ['http://libquotes.com', 'http://
      randy.pausch']], ['from', ['http://libquotes.com', 'http://libquotes.com']
      ], ['experience,', ['http://libquotes.com']], ['experience', ['http://
      randy.pausch']], ['bad', ['http://libquotes.com']], ['judgement.',
      ['http://libquotes.com']], ['If', ['http://libquotes.com']], ['things',
       ['http://libquotes.com', 'http://libquotes.com']], ["aren't", ['http://
      randy.pausch']], ['going', ['http://libquotes.com']], ['well', ['http://
      randy.pausch']], ['it', ['http://libquotes.com']], ['probably', ['http://
      randy.pausch']], ['means', ['http://libquotes.com']], ['learning',
      ['http://libquotes.com']], ['lot', ['http://libquotes.com']], ['will',
      ['http://libquotes.com']], ['go', ['http://libquotes.com']], ['better',
      ['http://libquotes.com']], ['later.', ['http://libquotes.com']], ['Randy',
      ['http://libquotes.com']], ['Pausch', ['http://libquotes.com']]]

It’s quite big as there were a lot of words in the two quotes. Note that some words appear in both
lists and some in just one.
To take a closer look at what is going on, you can try the following queries (It’s probably best to
remove the print(index) first so you can see the results more clearly):
      print(lookup(index, 'you'))
      ['http://eatthis.com', 'http://eatthis.com', 'http://libquotes.com']
In this result you see that 'you' occurred twice in the eatthis.com quote, but just once in the Randy
Pausch quote.
      print(lookup(index, 'good'))
      []
The word 'good' does not appear in either quote.
      print(lookup(index, 'bad'))
      ['http://libquotes.com']
Bad appears in just the Randy Pausch quote.
Using this code you can look up words in your index and get the urls where they are found. You can
add pages to your index and record all the words in that page in the location they occur. The one
thing left to do is to connect the code here with the code for crawling the web.

Finishing The Web Crawler (Finishing the Web Crawler)
Returning to the code you wrote before for crawling the web, make some modifications to include
the code you’ve just written.
First, a quick recap on how the crawl_web code below works before incorporating the indexing:
      def crawl_web(seed):
          tocrawl = [seed]
          crawled = []

Credits: Dave Evans and Udacity                                                                      9

---

           while tocrawl:
               page = tocrawl.pop()
               if page not in crawled:
                   union(tocrawl, get_all_links(get_page(page)))
                   crawled.append(page)
           return crawled

First, you defined two variables tocrawl and crawled. Starting with the seed page, tocrawl
keeps track of the pages left to crawl, whereas crawled keeps track of the pages that have already
been crawled. When there are still pages left to crawl, remove the last page from tocrawl using the
pop method. If that page has not been crawled yet, get all the links from the page and add the new
ones to tocrawl. Then, add the page that was just crawled to the list of crawled links. When there
are no more pages to crawl, return the list of crawled pages.

Adapt the code so that you can use the information found on the pages crawled. The changed code
is below. First, add the variable index, to keep track of the content on the pages along with their
associated urls. Since you are really interested in the index, this is what we will return.

It is possible to return both crawled and index, but to keep it simple just return index. Next,
add a variable, content to replace get_page(page). This variable will be used twice, once in the
code already there and once in the code to be filled in for the quiz. The procedure get_page(page)
is expensive as it requires a web call, so we don’t want to call it more often than is necessary. Using
the variable content means that the call to the procedure get_page(page) only needs to be
performed once and then the result is stored and can be used over and over without having to go
through the expensive call again.
### Q-5: Quiz (Finishing the Web Crawler)
Fill in the missing line using the variable content.

      def crawl_web(seed):
          tocrawl = [seed]
          crawled = []
          index = []
          while tocrawl:
              page = tocrawl.pop()
              if page not in crawled:
                  content = get_page(page)
                  # FILL IN THE MISSING LINE BELOW HERE

                   union(tocrawl,get_all_links(content))
                   crawled.append(page)
           return index

Understandably, you need to call the procedure add_page_to_index for adding the crawled page to
the search index:

Credits: Dave Evans and Udacity                                                                     10

---

                add_page_to_index(index, page, content)

Startup (Startup)
You now have a functioning web crawler! From a seed you can find a set of pages; for each of these
pages you can add the content from that page to an index, and return that index. Additionally,
since you have already written the code you can do the look-up that will return the pages for that
keyword.

But you're not completely done yet. In unit 5, you will see how to make a search engine faster and in
unit 6 you will learn how to find the best page for a given query rather than returning all the pages.
Before then, you need to understand more about how the Internet works and what happens
when you request a page on the world wide web.

Credits: Dave Evans and Udacity                                                                    11

---

The Internet (The Internet)
Let’s explore our get_page procedure to understand how it works:

      def get_page(url):
          return str(urlopen(url).read())
It is better to do some error handling when we try to read something from the Internet. This
is the python code that does that:
      def get_page(url):
           try:
               import urllib
               return str(urllib.urlopen(url).read())
           except:
               return ""
The table below shows what each line of the code does.

 Code                                        Explanation

 urllib.urlopen(url)
                                             This opens the web page at url
 urllib.urlopen(url).read()
                                             and reads the page requested which is a string.
 return
 urllib.urlopen(url).read()                  That string is then returned.
 import urllib                               Library urllib , so we have to import that.
                                             The code w hich con tains urlope n is in t he

                                             This is an exception handler. It’s called a try
                                             block. We try these things but they might not
 try:                                        always work. There might be an error. The page
 except:                                     might not be returned, or the url might be bad
    return ""                                or the page times out. If we request a url which
                                             we can’t be loaded, it jumps to the except:
                                             block and returns an empty string instead of
                                             producing an error.

Credits: Dave Evans and Udacity                                                                 12

---

Conclusion
Hopefully you understand at a high level what a web browser does when requesting data over the
Internet. There is nothing magic about it. The process is all about sending messages across the
Internet and receiving responses which are text. That text is processed by a browser, or even by
the web crawler you’ve programmed.

The search engine so far works but it isn’t fast or smart. In unit 5, you’ll look at how to make the
search engine scale and respond to queries faster. In unit 6, you’ll see learn how to find the best
response to a query, that is, to respond with the best page rather than all the pages.

Credits: Dave Evans and Udacity                                                                  13

---

---

*End of Unit 4*
