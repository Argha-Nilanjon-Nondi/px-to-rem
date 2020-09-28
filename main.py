unit="px"
class Converter:
 
    def __init__(self,style,rem=10):
        self.style=style
        self.rem=rem
        
    def extract_value(self):
        """
        ["2px solid red","2px"]
        """
        value=[]
        text=""
        for i in self.style:
            text+=i
            if(i==":"):
                text=""
            if(i==";"):
                 value.append(text)
                 text=""
        return value
    
    def extract_px(self):
                 """
                 ["200px","344px","900px"]
                 """
                 unit="px"
                 px=[]
                 value=self.extract_value()
                 for i in value:
                     i=i.replace(";","")
                     if(" " in i):
                         for j in i.split(" "):
                             if(unit in j):
                                 px.append(j)
                     elif(unit in i):
                          px.append(i)
                          
                 return px
                
    def px_to_num(self):
           """
           ["124px","90px","900px"] --> [900,124,90]
           """
           px=self.extract_px()
           num=[]
           for i in px:
                 i=i.replace(unit,"")
                 i=int(i)
                 num.append(i)
           num=set(num).intersection(set(num))
           num=list(num)
           num.sort()
           num.reverse()
           return num
           
    def px_rem_num(self):
            """
            {"px"[],"rem":[]}
            """
            px_int=self.px_to_num()
            px_strlist=[]
            rem_strlist=[]
            for i in px_int:
                  pxstr=str(i)+"px"
                  px_strlist.append(pxstr)
                  rem_num=i/self.rem
                  rem_str=str(rem_num)+"rem"
                  rem_strlist.append(rem_str)
            data={"px":px_strlist,"rem":rem_strlist}
            return data
     
    def converted_style(self):
               px_rem_list=self.px_rem_num()
               px= px_rem_list["px"]
               rem=px_rem_list["rem"]
               for i in range(len(px)):
                     self.style=self.style.replace(px[i],rem[i])
               return self.style
                         
                         
        
css="""
   body{
    background:url("0.png");
    background-size:cover;
    background-repeat:no-repeat;
    background-position:center;
    background-attachment:fixed;
   }
   
   #device{
   background-color:grey;
   width:700px 200px;
   padding:30px;
   margin:40% auto;
   border:2px solid black;
   border-radius:20px;
   }
"""        
obj = Converter(css)
print(obj.converted_style())