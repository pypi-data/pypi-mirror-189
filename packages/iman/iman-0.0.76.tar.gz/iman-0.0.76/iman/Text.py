from iman import *
import re

def getd(replist):
   mwords=[]
   words=[]
   ph=[]

   with open(replist , encoding='utf-8') as fr:
      for line in fr:
          t = line.split('\t')
          mwords.append(t[0])
          words.append(t[1])
          ph.append(t[2].strip())
   return(mwords,words,ph)       
   
   
class normal():
  def __init__(self,replist='c:\\Replace_List.txt'):
    self.replist=replist
    self.mwords,self.words,self.ph = getd(replist) 
    
  def rep(self , _str):
     for i in range(len(self.words)):
       if (self.words[i] in _str):
           pattern = "(^|\s)" + self.words[i] + "($|\s)"
           _str = re.sub(pattern ," " + self.mwords[i] + " " ,  _str)
       if (self.ph[i] in _str):
           pattern = "(^|\s)" + self.ph[i] + "($|\s)"
           _str = re.sub(pattern ," " + self.mwords[i] + " " ,  _str)
     return(_str.strip())  

  def from_file(self , filename ,file_out=None):

   matn  = Read(filename)

   if (file_out==None):
       file_out= PN(filename) + '_normal' + PE(filename)
   fid = open(file_out , 'w',encoding='utf-8')
   fid.write(self.rep(matn)) 
   fid.close()    



        