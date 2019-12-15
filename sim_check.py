
import numpy as np
import math


def main():
   file = "data-valid-all-5000.txt"

    #index of the best set found
   best = 0

    #index of set to check
   check = 3

   sets = 0;
   elements = 0;

   f= open(file,"r")

    #open file
    #set sets to number of rows
    
   for x in f:
      sets += 1
    #set elements to number of elements
    
   f.seek(0)
        
   while 1:
       char = f.read(1)
       if char == "\n": break
       else: elements += 1
   
   
   query = np.zeros(elements)
   sim = np.zeros(sets-1)
   
   for i in range(sets-2):
      f.readline()
      
   k = 0
   
   while 1:
      char = f.read(1)
      if char == '': break
      else: query[k] = int(char)
      k += 1
      
   #print(query)
   #print(sim)
   
   #print(sets)
   #print(elements)
   
   f.seek(0)
   
   total = 0
   overlap = 0
   
   for j in range(sets-1):
      x = f.readline()
      for i in range(elements):
         char = x[i]
         if query[i] == 1:
            total +=1
            if int(char) == 1:
               overlap +=1
         elif int(char) == 1:
            total +=1
         
      sim[j] = overlap/total
      overlap = 0
      total = 0

   #print(sim)

   best = np.argmax(sim)
   print("similiarity for set to check", check, sim[check-1])
   print("similiarity for actual best set", best+1, sim[best])
   
   f.close()
   
   f = open("sim_results.txt", "w+")
   
   for i in range(sets-1):
      f.write("{}\n".format(sim[i]))
      #f.write(str(sim[i]))
      #f.write("\n")
      
if __name__ == "__main__":
    main()
