
start = 'Subje'
mid = 'Binar'
end = ' '
time = 'python'
const = 0
var = 0
reslist = []

for ROUNDS in range(2,5):
    filename="new_best_diff_future_" + str(ROUNDS)+  ".lp"
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if start in line:
               # print( 'found at line:', num)
                temp1 = num + 1
            if mid in line:
                #print( 'found at line:', num)
                temp2 = num
        #print( 'found at line:', num)
        temp3 = num
    
    filename2="time" + str(ROUNDS)+  ".txt"
    with open(filename2) as myFile2:
        for num in myFile2:
            if time in num:
                words = num.split(' ')
                restime = words[3].split('.')[0]
                #print(restime)
                #print( 'found at line:', num)

            
    const = (temp2 - temp1)
    var = (temp3 - temp2)
    reslist.append(str(ROUNDS)  + ' & '+ str(var)   +' & ' + str(const) +' & ' + str(restime))
    myFile.close()
    
f= open("new_parameters.txt","w+")
for i in range (3):
    f.write(reslist[i])
    f.write('\n')
    
f.close()

    

    

            