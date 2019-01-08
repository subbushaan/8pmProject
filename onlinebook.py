class bookstore:
    def assign(self,bno,bname,btitle,bauthor,qntybooks,price):
        self.bno=bno
        self.bname=bname
        self.btitle=btitle
        self.bauthor=bauthor
        self.qntybooks=qntybooks
        self.price=price
        self.bamount=(qntybooks*price)
    def display(self):
        print("The Book number=",self.bno)
        print("The Book name=",self.bname)
        print("The Book Title=",self.btitle)
        print("The Book Author=",self.bauthor)
        print("The Number of Books=",self.qntybooks)
        print("The Book price=",self.price)
        print("The Bill Amount=",self.bamount)
b1=bookstore()
b1.assign(101,"VIJETHA","Panchayiti-Secratary","subhani",2,450)
b1.display()