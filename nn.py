p = [pi for pi in range(22,54)]
for re in range(2,6):
    p.append(re)
led = [l for l in range(1,37)]
combo=[]
for y in range(1,7):
    for x in range(1,7):
        combo.append(str(f"{y}{x}"))

for index in range(36):
    code = "{if(switch"+str(led[index])+"==0)"+"{digitalWrite("+str(p[index])+",HIGH); switch"+str(led[index])+"=1;}else{digitalWrite("+str(p[index])+",LOW); switch"+str(led[index])+"=0;}}"
    print(f"int switch{led[index]}=0; if(serialData==\"{combo[index]}\"){code}")
    print("")
print(p)
for i in range(1,37):
    print(f"switch{i}",end=", ")