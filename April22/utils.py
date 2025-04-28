def txt_file(input_fname, output_fname):
    
    file1 = open(input_fname,'r')
    file3 = open(output_fname, 'w')    
    
    output = []

    print(file1)
    line = file1.readline()
    
    while line != '':
        output.append(line)
        line = file1.readline()
        
    
    names= []
    scores = []
    
    for line in output:
        parts = line.strip().split(";")  # ['rene', '9']
        
        name = parts[0] # get the name
        score = int(parts[1]) # get the score
    
        names.append(name)
        scores.append(score)
        
    results = []
    
    for score in scores:
        if score < 3:
            r= "Fail"
        else: 
            r= "Pass"
            
        results.append(r)
        
    
    for i in range(len(names)):
        file3.write(names[i] + ";" + str(scores[i]) + ";" + results[i] + "\n")
        
    file3.close()
    file1.close()
    
def saludos():
    
    print('hola')
