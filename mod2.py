# method 1
# import modulename
# modulename.attribute

# import mod1
# mod1.msg()
# mod1.add(5,6)
# print(mod1.x)



#method 2
#from modulename import attribute
#attributename


# from mod1 import msg,add
# msg()
# add(5,6)


# #import aliasing
# import mod1 as m
# m.msg()
# m.add(5,6)





#####################  ABCD PACKAGE IMPORTING  ##########################################

##creating package from ABCD
# from ABCD import mod5
# mod5.msg()


from ABCD.mod5 import msg
msg()