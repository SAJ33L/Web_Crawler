# Unit 2: Programming Fundamentals — Building a Search Engine

**Course:** BSCS/BSDS/MCS-EA 1st  
**Instructor:** Muhammad Ateeq, Asst. Prof. of CS @ The IUB  

*Source material credits: Dave Evans and Udacity*

---

## WHAT: In the previous unit we learned how to extract the first link from a webpage. In this unit
we will be writing a program to extract all the links from a given web page.

## Storing Code in a File
So far we have been using the IDLE to write code directly line-by-line. However, we can better
place our code in a separate file and execute it all at once. This makes it easy to write and
manage larger chunks of code (which we shall be doing now). The process is simple:
    1. Open IDLE
    2. Go to File  New File [This will open a new window]
    3. Write your desired code in this new editor window and save it at a suitable location.
As an example we store the code we wrote to extract the first link from a webpage in a file and
save it by name ‘extractor.py’. Remember, all python code files are generally saved with ‘.py’
extension.

## Procedures and Control
In Unit 1, you wrote a program to extract the first link from a web page. The next step towards
building your search engine is to extract all of the links from a web page. In order to write a
program to extract all of the links, you need to know these two key concepts:
        1. Procedures - a way to package code so it can be reused with different inputs.
        2. Control - a way to have the computer execute different instructions depending on the
        data (instead of just executing instructions one after the other).

Recall this code from then end of Unit 1:
        page = ...contents from some web page
        start_link = page.find('<a href=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        print(url)

This finds and prints the first link on the page. To keep going, we could update the value of page
to be the characters from the end_quote, and repeat the same code again:
        page = page[end_quote:]
        start_link = page.find('<a href=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        print(url)
        page = page[end_quote:]
        start_link = page.find('<a href=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)

---

        url = page[start_quote + 1:end_quote]
        print(url)

This code will print out the next two links on the web page. Clearly, this is tedious work. The
reason we have computers is to avoid having to do tedious, mechanical work! In addition to
being tedious, repeating the same code over and over again like this won’t work well because
some pages only have a few links while other pages will have more links than the number of
repetitions.
In this unit, you will learn three important programming constructs: procedures, if statements,
and while loops. Procedures, also known in Python as “functions,” enable you to abstract code
from its inputs; if statements allow you to write code that executes differently depending on the
data; and while loops provide a convenient way to repeat the same operations many times. You
will combine these to solve the problem of finding all of the links on a web page.

## Procedural Abstraction
Procedural abstraction is a way to write code once that works on any number of different data
values. By turning our code into a procedure, we can use that code over and over again with
different inputs to get different behaviors.
                Any webpage                                           Extracted links
                                   Link Extracting Procedure

## Procedures (Introducing Procedures)
A procedure takes in inputs, does some processing, and produces outputs.
For example, the + operator is a procedure where the inputs are two numbers and the output is
the sum of those two numbers. The + operator looks a little different from the procedures we
will define since it is built-in to Python with a special operator syntax. In this unit you will learn
how to write and use your own procedures.

Here is the Python grammar for writing a procedure:
        def <name>(<parameters>):
                <block>
The keyword def is short for “define”.
<name> is the name of a procedure. Just like the name of a variable, it can be any string that
starts with a letter and followed by letters, number and underscores.
<parameters> are the inputs to the procedure. A parameter is a list of zero or more
names separated by commas: <name>, <name>,... Remember that when you name your
parameters, it is more beneficial to use descriptive names that remind you of what they mean.
Procedures can have any number of inputs. If there are no inputs, the parameter list is an empty
set of closed parentheses: ().
After the parameter list, there is a : (colon) to end the definition header.
The body of the procedure is a <block>, which is the code that implements the procedure. The
block is indented inside the definition. Proper indentation tells the interpreter when it has
reached the end of the procedure definition.
Let’s consider how to turn the code for finding the first link into a get_next_target procedure
that finds the next link target in the page contents. Here is the original code:

---

        start_link = page.find('<a href=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
Next, to make this a procedure, we need to determine what the inputs and outputs are.

### Q-1: Quiz (Procedure Code)
What are the inputs for the procedure, get_next_target?
       a. a number giving position of start of link
       b. a number giving position of start of next quote
       c. a string giving contents of the rest of the web page
       d. a number giving position of start of link and a string giving page contents

### Q-2: Quiz (Output)
What should the outputs be for get_next_target?
       a. a string giving the value of the next target url (url)
       b. url, page
       c. url, end_quote
       d. url, start_link

## Return Statement
To make the get_next_target procedure, we first add a procedure header and indent our
existing code in a block:
        def get_next_target(page):
                start_link = page.find('<a href=')
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)
                url = page[start_quote + 1:end_quote]
We can change the name of the parameter page to s. This is more descriptive since the
procedure can work on any string. After we rename the parameter, we also need to change the
name wherever it is used in the block:
        def get_next_target(s):
                start_link = s.find('<a href=')
                start_quote = s.find('"', start_link)
                end_quote = s.find('"', start_quote + 1)
                url = s[start_quote + 1:end_quote]

To finish the procedure, we need to produce the outputs. To do this, introduce a new Python
statement called return. The syntax for return is:
        return <expression>, <expression>, ...
A return statement can have any number of expressions. The values of these expressions are the
outputs of the procedure.

A return statement can also have no expressions at all, which means the procedure procedures
no output. This may seem silly, but in fact it is quite useful. Often, we want to define procedures
for their side-effects, not just for their outputs. Side-effects are visible, such as the printing done
by a print statement, but are not the outputs of the procedure.

---

### Q-3: Quiz (Return Statment)
Complete the get_next_target procedure by filling in the return statement that
produces the desired outputs.
      def get_next_target(s):
              start_link = s.find('<a href=')
              start_quote = s.find('"', start_link)
              end_quote = s.find('"', start_quote + 1)
              url = s[start_quote + 1:end_quote]
              return ________

## Using Procedures
In order to use a procedure, you need the name of the procedure, followed by a left parenthesis,
a list of the procedure’s inputs (sometimes called operands or arguments), closed by right
parenthesis:
        <procedure>(<input>,<input>, …)
For example, consider the rest_of_string procedure defined as:
        def rest_of_string(s):
                return s[1:]
To use this procedure we need to pass in one input, corresponding to the parameter s:
        print(rest_of_string('audacity'))
        udacity
We can see what is going on by adding a print statement in the procedure body:
        def rest_of_string(s):
                print('Here I am in rest_of_string!')
                return s[1:]
        print(rest_of_string('audacity'))
        Here I am rest_of_string!
        udacity

You can do anything you want with the result of a procedure, for example you can store it in a
variable.
        def rest_of_string(s):
                 print('Here I am in rest_of_string!')
                 return s[1:]
        s = rest_of_string('audacity')
        print(s)
        Here I am rest_of_string!
        udacity

Think of procedures as mapping inputs to outputs. This is similar to a mathematical function.
Indeed, many people call procedures in Python like the ones we are defining “functions”. The
reason I prefer to call them procedures is that they are quite different from mathematical
functions. The main differences are:
       ● A mathematical function always produces the same output given the same inputs. This
       is not necessarily the case for a Python procedure, which can produce different outputs
       for the same inputs depending on other state (we will see examples in Unit 3).
       ● A mathematical function is a pure abstraction that has no associated cost. The cost of

---

        executing a Python procedure depends on how it is implemented. (We will discuss how
        computer scientists think about the cost of procedures in Unit 5.)
        ● A mathematical function only maps inputs to outputs. A Python procedure can also
        produce side-effects, like printing.
Procedures are a very important concept and the core of programming is breaking problems
into procedures, and implementing those procedures.

### Q-4: Quiz (Inc Procedure)
What does the inc procedure defined below do?
      def inc(n):
               return n + 1
      a. Nothing
      b. Takes a number as input, and outputs that number plus one
      c. Takes a number as input, and outputs the same number
      d. Takes two numbers as inputs, and outputs their sum

### Q-5: Quiz (Sum Procedure)
What does the sum procedure defined below do?
      def sum(a, b):
               a=a+b
      a. Nothing
      b. Takes two numbers as its inputs, and outputs their sum
      c. Takes two strings as its inputs, and outputs the concatenation of the two strings
      d. Takes two numbers as its inputs, and changes the value of the first input to be the sum
      of the two number
However, see what happens here:
      print(a)
      Traceback (most recent all last):
      File "<pyshell#11>", line 1, in <module>
      print(a)
      NameError: name 'a' is not defined
An error is returned because the variable a is not defined outside the block of the procedure.

### Q-6: Quiz (Sum Procedure with a Return Statement)
What does the sum procedure defined below do?
        def sum(a,b):
                a=a+b
                return a
a. Takes two numbers as its inputs, and outputs their sum.
b. Takes two strings as its inputs, and outputs the concatenation of the two strings.
c. Takes two numbers as its inputs, and changes the value of the first input to be the sum of
the two number.

### Q-7: Quiz (Square)
Define a procedure, square, that takes one number as its input, and outputs the square of that
number (result of multiplying the number by itself). For example,

---

        print(square(5)) [also try print(square(square(5)))]
        25

### Q-8: Quiz (Sum of Three)
Define a procedure, sum3, that takes three inputs, and outputs the sum of the three input numbers.
        print(sum3(1, 2, 3)) → 6

### Q-9: Quiz (Abbaize)
Define a procedure, abbaize, that takes two strings as its input, and outputs a string that is the first
input followed by two repetitions of the second input, followed by the first input.
        abbaize('a', 'b') → 'abba'
        abbaize('dog', 'cat') → 'dogcatcatdog'

### Q-10: Quiz (Find Second)
Define a procedure, find_second, that takes two strings as its inputs: a search string and a target
string. It should output a number located at the second occurrence of the target string within the
search string. Example:
         danton = "De l'audace, encore de l'audace, toujours de l'audace."
         print(find_second(danton, 'audace'))
         25

## Making Decisions (Equality Comparisons)
Everything so far has been limited. So far, your programs are only able to do the same thing on
all data and you cannot do anything that depends on what the data is. Now, let’s figure out a way
to make code behave differently based on decisions. To do so we want to find a way to make
comparisons, which will give you a way to test and ultimately allow your program to decide what to
do.

### Comparison Operators
Python provides several operators for making comparisons:
                                 <     less than
                                 >     greater than
                                 <= less than or equal to
                                 == equal to
                                 != not equal to
All of these operators act on numbers, for example:
                 <number> <operator> <number>
The output of a comparison is a Boolean: True or False.
Here are some examples:
         print(2 < 3)
         True
         print(21 < 3)
         False
         You can also make comparisons using expressions:
         print(7 * 3 < 21)
         False
         print(7 * 3 != 21)
         False
         Note the equality is done using two equals signs (double ==), not a single =:

---

       print(7 * 3 == 21)
       True

### Q-11: Quiz (Equality Comparisons)
Why is the equality comparison done using == instead of =?
       a. Because = means approximately equal.
       b. Because not equal uses two characters !=.
       c. Because Guido (van Rossum, the creator of Python) really likes = signs.
       d. Because = means assignment.
       e. It doesn’t matter, we can use either == or =.

## If Statements (If Statements)
An if statement provides a way to control what code executes based on the result of a test
expression. Here is the grammar of the if statement:
                        if <TestExpression>:
                                <block>
In this statement, the code in the <block> runs only if the value of the test expression is True.
Similar to procedures, the end of the if statement block is determined by the indentation.
Here is an example where we use an if statement to define a procedure that returns the absolute
value of its input:
                        def absolute(num):
                                if num < 0:
                                       num = -num
                                return num

### Q-12: Quiz (If Statements)
Define a procedure, bigger, that takes in two numbers as inputs, and outputs the greater of the
two inputs.
                      bigger(2, 7) → 7
                      bigger(3, 2) → 3
                      bigger(3, 3) → 3

Else Expressions (Is Friend)
You can use an else clause in addition to an if statement to provide alternative code that will
execute when the test expression is false. The test expression determines whether to execute
the block inside the if statement or the block inside the else statement:

                       if <TestExpression>:
                               <block>
                       else:
                               <block>
Using else, we can define bigger in a more symmetrical way:
                        def bigger(a, b):
                                if a > b:
                                         return a
                                else:
                                         return b

### Q-13: Quiz (Is Friend)

---

Define a procedure, is_friend, that takes a string as its input, and outputs a Boolean indicating if the
input string is the name of a friend.
Assume I am friends with everyone whose name starts with D and no one else.
                              print(is_friend('Diane'))        → True
                              print(is_friend('Fred'))         → False

### Q-14: Quiz (More Friends)
Define a procedure, is_friend, that takes a string as its input, and outputs a Boolean indicating if the
input string is the name of a friend.
Assume I am friends with everyone whose name starts with either D or N,
but no one else.
                               print is_friend('Diane')       → True
                               print is_friend('Ned')         → True

Or Expressions (Or)
An or expression gives the logical or (disjunction) of two operands. If the first expression
evaluates to True, the value is True and the second expression is not evaluated. If the value of
the first expression evaluates to False then the value of the or is the value of the second
expression.
                       <Expression> or <Expression>
Here are a few examples:
                      print(True or False)
                      True
                      print(False or True)
                      True
                      print(True or True)
                      True
                      print(False or False)
                      False
An important difference between an or expression and other operators is that an or expression
does not necessarily evaluate both of its operand expressions. For example:
                         print(True or this_is_an_error)
                         True
Even though this_is_an_error would produce an error because the variable is not defined, the
or expression does not produce an error! This is because the second operand expression of an
or is only evaluated if the first expression evaluates to False. When the first operand expression
evaluates to True, the output of the or expression must be True regardless of the value of the
second operand expression. The Python rules of evaluation require that the second operand
expression is not even evaluated in cases where the value of the first operand is True.
### Q-15: Quiz (Biggest)
Define a procedure, biggest, that takes three numbers as inputs, and outputs the greatest of the
three numbers.
                               biggest (6, 2, 3) → 6
                               biggest (6, 2, 7) → 7
                               biggest (6, 9, 3) → 9

---

You have now learnt about arithmetic comparisons, procedures, and if statements.
  You now know enough (in theory) to write every possible computer program.

## While Loops (While Loops)
Loops are a way of executing something over and over. The syntax for the while loop is very
similar to the if statement:
                                 while <TestExpression>:
                                         <Block>
In contrast to an if statement where the block executes either 0 or 1 times depending on
whether the test expression is True or False, a while loop executes any number of times,
continuing as long as the test expression is True.
In a if statement if the test expression is True, the block executes once and then continues to the
following statment. If the test expression is False, execution jumps over the block and continues
with the following statement.
If the test expression for a while loop is True, the block is executed. Then, execution continues
by going back to the test expression again. If it still evaluates to True, the block is executed
again, and execution continues by going back to the test expression one more time. This
continues as long as the test expression evaluates to True. and again as many times as you need.
Once the test expression is False, execution jumps to the next statement. There is no guarantee
that the test expression eventually becomes False, however. The loop could keep running
forever, which is known as an infinite loop.
Here is an example while loop:
                                 i=0
                                 while i < 10:
                                         print(i)
                                         i=i+1
This code will execute the inner block as long as the test expression, while i < 10, is True.
Inside the block, it prints i and then adds 1 to i. In this example, the while loop repeats 10 times,
printing the numbers from 0 to 9. At the end of the loop, the value of i is 10.

### Q-16: Quiz (While Loops)
What does this program do?
                                  i=0
                                  while i != 10:

---

                                          i=i+2
                                          print(i)
        a. Produce an error
        b. Print out 2, 4, 6, 8, 10.
        c. Print out 0, 2, 4, 6, 8.
        d. Print out 0, 2, 4, 6, 8, 10.
        e. Run forever

### Q-17: Quiz (While Loops-2)
What does the following code do?
                                  i=1
                                  while i != 10:
                                           i=i+2
                                           print(i)
      a. Produce an error.
      b. Print out 2, 4, 6, 8.
      c. Print out 1, 3, 5, 7, 9.
      d. Print out 3, 5, 7, 9.
      e. Run forever.

### Q-18: Quiz (Print Numbers)
Define a procedure, print_numbers, that takes as input a positive whole number, and prints out
all the whole numbers from 1 up to and including the input number.
                print_numbers(3)
                1
                2
                3

Baby Blocks (Factorial)
Suppose we have four blocks and a baby. We want to know how long the baby can play with the
blocks without getting bored. The baby wants to try all of the different ways of arranging the
blocks by stacking them in a tower.

Think about the baby’s choices for the first block, she has four. Let’s say she reaches for the red
block first. When she reaches for the second block she is down to just three choices. If she stacks
the green block on top of the red block, she has two choices left, the blue block and the purple

---

block. Next, the baby picks the purple one. Therefore, for her fourth block, the baby only has one
choice, the blue one.
To figure out the total number of choice we want to multiply the number of choices for the first
block by the number of choices for the second block, by the number of choices for the third
block, all the way to the fourth block. The function that you are computing is factorial. For any
input n, you compute the factorial, which is the number of ways of arranging n items.
                        factorial(n) = n · (n-1) · (n-2) · … · 2 · 1

### Q-19: Quiz (Factorial)
Define a procedure, factorial, that takes one number as its input and outputs the factorial of that
number.

Break (Break)
Break gives us a way to break out of a loop, even if the test condition is true. The typical
structure of the loop with a break looks like this:
                while <TestExpression>:
                       <Code>
                       if <BreakTest>:
                                break # stop executing the while loop
                       <More Code>
                <After While>
The break statement jumps out of the loop to <After While>.
Here is an example showing how we could rewrite print_numbers using break:
               def print_numbers(n):
                       i=1
                       while True:
                              if i > n:
                                        break
                              print(i)
                              i=i+1
This has the same behavior as the previous implementation, except now the test condition for
the while loop is True. This is a bad example: if there is a way to write a loop without using
break, it is usually best to avoid it. We will see soon an example where it is more difficult to
write the loop without using break, since it is not clear before executing part of the block if the
loop should continue repeating.

### Q-20: Quiz (Break)
Which of the following are always equivalent to:
               while <T>:
                       <S>

       a. while <T>:
               if False:
                        break
               <S>
       b. while <T>:

---

                <S>
                break
        c. while True:
                if <T>:
                          break
                <S>
        d. while <T>:
                <S>
                if <T>:
                          <S>
                else:
                          break

Multiple Assignment (Multiple Assignment)
So far we have defined a procedure to eliminate writing tedious code:
        def get_next_target(page):
                start_link = page.find('<a href=')
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)
                url = page[start_quote + 1:end_quote]
                return url, end_quote
Although you have not yet used a procedure that returns two things, it is pretty simple to do.
You can do this by having two values on the left side of an assignment statement.
Assigning multiple values on the left side of an assignment statement is called multiple
assignment. To write a multiple assignment you can put any number of names separated by
commas, an equal sign and then any number of expressions separated by commas. The number
of names and the number of expressions has to match so that the value of the first expression
can be assigned to the first name and so on.
                <name1>, <name2>, … = <expression1>, <expression2>, …
Example:
                a, b = 1, 2
Therefore, in order to get the two values, (url, end_quote) to return from the procedure above,
you will need to have the two variables on the left side and the procedure on the right. Here is
the syntax to do that:
                url, endpos = get_next_target(page)

### Q-21: Quiz (Multiple Assignments)
What does this do?
      s, t = t, s
                a. Nothing
                b. Makes s and t both refer to the original value of t
                c. Swaps the values of s and t
                d. Error

No Links (No Links)

---

There is one concern with the get_next_target procedure that has to be fixed before tackling
the problem of outputting all of the links, which is:
What should happen if the input does not have another link?
Test the code in the interpreter using a test link to print get_next_target:
        def get_next_target(page):
                start_link = page.find('<a href=')
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)
                url = page[start_quote + 1:end_quote]
                return url, end_quote
          print(get_next_target('this is a <a href="http://udacity.com">link!</a>'))
          ('http://udacity.com', 37)
When you run this code you get both outputs as a tuple, that is, the link followed by the position
of the end quote. A tuple is an immutable list, meaning it cannot be modified. In the same way a
list is enumerated with brackets, a tuple definition is bounded by parentheses.
Or you can write this using a double assignment to return just the url:
        def get_next_target(page):
                start_link = page.find('<a href=')
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)
                url = page[start_quote + 1:end_quote]
                return url, end_quote
        url, endpos = get_next_target('this is a <a href="http://udacity.com">link!</a>')
        print(url)
        http://udacity.com
What happens if we pass in a page that doesn’t have a link at all?
      def get_next_target(page):
              start_link = page.find('<a href=')
              start_quote = page.find('"', start_link)
              end_quote = page.find('"', start_quote + 1)
              url = page[start_quote + 1:end_quote]
              return url, end_quote
        url, endpos = get_next_target('good')
        print(url)
        goo
The program returns, “goo” because when the find operation does not find what it is looking for
it returns -1. When -1 is used as an index, it eliminates the last character of the string. Compare
with a string that includes double quotes:
        def get_next_target(page):
                start_link = page.find('<a href=')
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)

---

                url = page[start_quote + 1:end_quote]
                return url, end_quote
        url, endpos = get_next_target('Not "good" at all!')
        print(url)
        Not
In the end, the code above is not very useful. It is going to be very hard to tell when you get to
the last target because maybe Not could be a valid url, but we don’t know that.

### Q-22: Quiz (No Links)
Think about making get_next_target more useful in the case where the input does not contain
any link. This is something you can do! Here is a hint:
        def get_next_target(page):
                start_link = page.find('<a href=') # HINT: put something into the code here
                start_quote = page.find('"', start_link)
                end_quote = page.find('"', start_quote + 1)
                url = page[start_quote + 1:end_quote]
                return url, end_quote
        url, endpos = get_next_target('Not "good" at all!')
        print(url)
Modify the get_next_target procedure so that if there is a link it behaves as before, but if
there is no link tag in the input string, it outputs None, 0.

Print All Links (Print All links)
At this point you have a piece of code, get_next_target, to replace a formerly tedious program. Here
is where we are so far, with a few modifications:
        page = contents of some web page as a string
        url, end pos = get_next_target(page)
        print(url)
        page = page[endpos:] #replaced end_quote with endpos
        url, endpos = get_next_target(page)
        ...
This code will have to repeat and keep going until the url that’s returned is None.
So far, you have seen a way to keep going, which is a while loop. You have seen a way to test the
url. Now you have everything you need to print all the links on the page!

Getting a Webpage
Instead of supplying the source of a webpage as string, we can directly get a webpage from
internet. For this, we need to import a library urllib.
        import urllib
        from urllib.request import urlopen

Having imported the urllib, we can get a webpage using its url:
        page = str(urlopen(url).read())
The page is read as bytes and we need it in the form of string, therefore, we use str() for conversion.
This works only when you are connected to the Internet. You may use page string otherwise.

---

### Q-23: Quiz (Print All Links)
In the following code, fill in the test condition for the while loop and the rest of the else
statement:
       def print_all_links(page):
               while ________: # what goes as the test condition for the while?
                       url, endpos = get_next_target(page)
                       if url: # test whether the url you got back is None
                                print(url)
                                page = page[endpos:] # advance page to next position
                       else: # if there was no valid url, then get_next_target did not
                       find a link then do something else. What do you need to do?
Let’s go back to the xkcd web page we looked at earlier and try something a little more
interesting. Go to the xkcd.com home page, click view source to find the first link on the page
and notice how many links there are in the source code — quite a few.
Using your print_all_links code, print get_page and try passing in the page url, 'http://
xkcd.com/353'. Your program should return the page's source code when you run it.
        def print_all_links(page):
                while True:
                        url, endpos = get_next_target(page)
                        if url:
                                print(url)
                                page = page[endpos:]
                        else:
                                break
        print(get_page('http://xkcd.com/353'))
Since we do not need the entire source code for what we are looking for, try your print_all_links
procedure to print all of the links on the xkcd.com page to print the links on the page.
       def print_all_links(page):
               while True:
                       url, endpos = get_next_target(page)
                       if url:
                                print(url)
                                page = page[endpos:]
                       else:
                                break
       print_all_links('http://xkcd.com/353')
There are a few links that are not returned, but you will learn about those situations in the
coming units.
Congratulations! You just learned how to print all the links on a web page, every possible
computer program, and are in good shape to continue building your web browser! In the next
unit you will learn how to collect the links from a web page and do something with them.

---

---

*End of Unit 2*
