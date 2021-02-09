world = []
mutation = 0
m = 0
genes = []
import random
def create(n,p):
    pop = p/n
    for idx in range(0,n):
        world.append([])
    for item in world:
        item.append(pop)


def virus(i,l,population,inf):
    counter = 0
    for idx in range(0,100):
        inf*=i+1
        total_uninfectable = population-inf
        i = total_uninfectable/population
        i-= ((l+1)**2)-1
        print(inf)
        num = int(inf)
    for idx in range(0,num):
        r1 = random.randint(0, 10) 
        if r1 == 1:
                counter+=1
    print(counter)
    
def mutate(c):
    for idx in range(0,c):
        up = random.randint(1,2)
        up1 = random.randint(1,2)
        mutationl = round(random.random(),2)
        mutationi = round(random.random(),2)
        if up > 1:
                genes.append([-mutationl,mutationi])
        if up1 > 1:
                 genes.append([mutationl,-mutationi])

            
        
        
        
   
        
    
    
        
        
create(5,50000)
virus(0.5,0.02,10000,2)
print(len(world))
mutate(3)
print(genes)
