class Parent():
    def __init__(self,l_name,e_color):
        print "Parent constructor called"
        self.last_name = l_name
        self.eye_color = e_color

class Child(Parent):
    def __init__(self,l_name,e_color,num_toys):
        print ("Child constructor called")
        Parent.__init__(self,l_name,e_color)
        self.number_of_toys = num_toys


billy_de = Parent("BOya","blue")
print (billy_de.last_name)

milo = Child("mileo","blue",7)
print (milo.last_name)
print (milo.number_of_toys)
