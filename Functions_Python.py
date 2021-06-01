text = "london is a capital of Great Britain"
a = text.capitalize()
print (a)

text = "SpOrT Is OuR lIfE!"
b = text.casefold()
print(b)

text = "I love you"
c = text.center(50)
print(c)

text = "My name is Andrey. My mom's name is Luda, My brother's name is Anton"
d = text.count("My")
print(d)

text = "My car is green"
e = text.encode()
print(e)

text = "Home number 43"
f = text.endswith("43")
print(f)

text = "B\tu\te\tB\tu\te"
g =  text.expandtabs(2)
print(g)

text = "Everyone sees the world in one’s own way"
h = text.find("world")
print(h)

text = "It costs {price:.2f} rubles"
print(text.format(price = 49))

point = {'a':2,'b':-1}
print('{a} {b}'.format_map(point))

text = "Never look back.!."
i = text.index("!")
print(i)

text = "Number13"
j = text.isalnum()
print(j)

text = "TeslaXXX"
k = txt.isalpha()
print(k)

text = "127"
l = text.isdecimal()
print(l)

text = "1502a"
m = text.isdigit()
print(m)

text = "Andrey"
n = text.isidentifier()
print(n)

text = "big brother"
o = text.islower()
print(o)

text = "3026511"
p = text.isnumeric()
print(p)

text = "Hey, are you a new in class 8c?"
q = text.isprintable()
print(q)

text = " "
r = text.isspace()
print(r)

text = "My Dream IS A NEW Computer"
s = text.istitle()
print(s)

text = "LIFE IS SUPPER"
t = text.isupper()
print(t)

my_friends = ("Artem", "Vlad", "Dimasik")
u = ", ".join(my_friends)
print(u)

text = "My dog"
v = text.ljust(45)
print(v, "is my best friend!")

text = "ALL ShoulD be SmaLL"
w = text.lower()
print(w)

text = " monkeys "
x = text.lstrip()
print("the funnies animal are", x, " and I like them ")

text = "My Life — my rules."
my_table = text.maketrans("L", "w")
print(text.translate(my_table))

text = "Everyone is the creator of one’s own fate"
y = text.partition("of")
print(y)

text = "Love is the movement."
z = text.replace("Love", "Run")
print(z)

text = "No news are good news."
aa = text.rfind("news")
print(aa)

text = "to be or not to be that is the question"
bb = text.rindex("to")
print(bb)

text = "After"
cc = text.rjust(40)
print(cc, "a storm comes a calm.")

text = "An hour in the morning is worth two in the evening."
dd = text.rpartition("in ")
print(dd)

text = "good, better, best"
ee = text.rsplit(", ")
print(ee)

text = "than"
ff = text.rstrip()
print("Better late", ff, "never")

text = "The sun will shine on our side of the fence"
gg = text.split()
print(gg)

text = "To live a \ncat and dog life"
hh = text.splitlines()
print(hh)

text = "No gain without pain."
ii = text.startswith("No")
print(ii)

text = "   than   "
jj = text.strip()
print("Better save", jj, "sorry")

text = "I wIlL bE bAcK!"
kk = text.swapcase()
print(kk)

text = "I prefer live near by ocean"
ll = text.title()
print(ll)

my_dict = {83:  80}
text = "Hi Sergey!"
print(text.translate(my_dict))

text = "May the force be with you!"
mm = text.upper()
print(mm)

text = "lol"
nn = text.zfill(15)
print(nn)
