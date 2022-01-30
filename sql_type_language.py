import pickle as p
#file=open("table.dat", "wb+")
DATATYPES=[str,int,list,tuple,None]
CONDITIONS=['unique','!null','!space']
close='close'
out='out'
class Table:
    a={}
    b={}
    #tname=''
    def __init__(self, tname, **kwargs):
        self.tname=tname
        for i in kwargs:
            Table.a[i]=[]
            Table.b[i]=kwargs[i]
    def addrow(self, arr):
        self.ind=0
        if len(arr)<len(Table.a):
            for i in range(len(Table.a)-len(arr)):
                arr.append(None)
        print(len(arr))

        if self.errorcheck(arr)==1:
            try:
                for z in Table.a:
                    Table.a[z]+=[arr[self.ind]]
                    self.ind+=1
            except IndexError:
                for i in range(len(Table.a)-len(arr)):
                    Table.a[z].append(None)
        else:
            print("datatype mismatch")
    def addcol(self, cname, datatype, arc):
        if len(arc) == len(list(Table.a.values())[0]):
            Table.a[cname]=arc
            Table.b[cname]=[datatype]
        else:
            print("column lenght error")
    def add_(self,c_name):
        try:
            return sum(Table.a[c_name])
            print(sum(Table.a[c_name]))
        except:
            print("strings in column")
    def col_operations(self, operations, *cnam):
        self.coln='1'
        mlen=len(list(Table.a.values())[0])
        indi=0
        p=[]
        if operations == '+':
            while indi < mlen:
                res=0
                for cn in cnam:
                    res += Table.a[cn][indi]
                else:
                    p+=[res]
                indi+=1
            self.addcol('add', int, p)
        if operations == '*':
            while indi < mlen:
                res=1
                for cn in cnam:
                    res *= Table.a[cn][indi]
                else:
                    p+=[res]
                indi+=1
            self.addcol('op'+self.coln, int, p)
        self.coln=str(int(self.coln) + 1)
    def edit(self, rowname, coloumnname,element):
         inde=''
         array=[]
         for i in Table.a:
              if rowname in Table.a[i]:
                  inde=Table.a[i].index(rowname)
         Table.a[coloumnname][inde]=element             
    def select(self,*cname):
        #-------------
        largest=0
        for i in Table.a:
            for j in Table.a[i]:
                if len(str(j))-1>largest:
                        largest=len(str(j))
        #-------------

        nc=len(cname)
        if nc!=0:
            for i in range(0,len(Table.a[list(cname)[0]])):
                print(("{} |"*(nc)).format(*list(str(Table.a[came][i])+(' '*(largest-len(str(Table.a[came][i])))) for came in cname)))
        else:
            nc=len(Table.a)
            cname=Table.a.keys()
            for i in range(0,len(Table.a[list(cname)[0]])):
                print(("{} |"*(nc)).format(*list(str(Table.a[came][i])+(' '*(largest-len(str(Table.a[came][i])))) for came in cname)))
    def errorcheck(self, element):
        column = list(x for x in Table.b)
        inds=0
        ret=0
        for col in column:
            if Table.b[col][0] in DATATYPES:
                dtype=Table.b[col][0]
                if type(element[inds])==dtype or element[inds] == None:
                    ret+=1
            else:
                print("please give valid datattype")
            inds+=1
        else:
            if ret == len(element):
                return 1
            else: return 0
    def help(self):
        print("hello coder this is pqql help assistant\n\nour developers commitee thanks you for choosing pyql and we hope we can provide you with the easiest querry language\n\nso in pyql we have the following querries:\n\nTable('table_name', column_name1=[datatype,conditions(like !null for not null and !space for no space),column_name2...]):for making table\n\n\
mem.addrow([value for column1 , value for column2 , ...]) for adding row {note : the vales should be according to their corresponding tablle datatype and coditions}\n\nmem.addcol('column_name', <datatype>, [value for row1, value for row2, ...]) add a new column to the table\n\nmem.col_operations('operator',<columns on which operation is to be performed>) do the particular operations on the table\n\nmem.select('column1','column2') display table[if nothing entered displays the complete table]\n\nmem.edit(any row element of the particular row where item to be edited is present,column_name,new_element) used for editing any particular value\n\nmem.help() for help :-)")
                
#'''
print("type <help> for recieving help and <'close'> for stopping")
while True:
    mem = eval(input('>>> '))
    while mem!=help and mem!='close':
        amem = input('>>> ')
        if amem == 'out':
            print('coming out of table: {}'.format(mem.tname))
            break
        amem = 'mem.'+amem if 'mem.' not in amem else amem
        eval(amem)
    else:
        if mem=='close':
            break
        else:
            print("hello coder this is pqql help assistant\n\nWe thanks you for choosing pyql and we hope we can provide you with the easiest querry language\n\nso in pyql we have the following querries:\n\nTable('table_name', column_name1=[datatype,conditions(like !null for not null and !space for no space)],column_name2...):for making table\n\n\
mem.addrow([value for column1 , value for column2 , ...]) for adding row {note : the vales should be according to their corresponding tablle datatype and coditions}\n\nmem.addcol('column_name', <datatype>, [value for row1, value for row2, ...]) add a new column to the table\n\nmem.col_operations('operator',<columns on which operation is to be performed>) do the particular operations on the table\n\nmem.select('column1','column2') display table[if nothing entered displays the complete table]\n\nmem.edit(any row element of the particular row where item to be edited is present,column_name,new_element) used for editing any particular value\n\nmem.help() for help :-)\n HINT YOU CAN ALSO USE PYTHON WITH exex() FUNCTION")


'''
mem=Table('student', srid=[int], name=[str], marks=[int])
mem.addrow([1,'siddharth',94])
mem.addrow([2,'dhiman',90])
mem.addrow([3,'chirag',92])
mem.addrow([4,'parth',65])
mem.addcol('age', int, [17,17,17,17])
mem.col_operations('+','srid','marks','age')
mem.col_operations('*','srid','marks','age')
mem.select()
mem.edit('parth','name','suman')
mem.select()
'''
