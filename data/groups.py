# -*- coding: utf-8 -*-

from model.group import Group

testdata = [
    Group(name='1name', header='1header', footer='1footer'),
    Group(name='2name', header='2header', footer='3footer'),
]



#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
    #Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    #for i in range(1)]