clear()
Plants = [Entities.Grass,Entities.bush,Entities.tree,Entities.carrot,Entities.sunflower,Entities.pumpkin,Entities.dead_pumpkin]
MapSize = 22
dir = [North,South,West,East]
esc_plant = 2
n = get_pos_x()
		

def colher():
	for i in range(MapSize):
		for j in range(MapSize):
			harvest()
			move(dir[3])
		move(dir[0])
	

def arar(esc_terra):
	if esc_terra == 0:
		if get_ground_type() == Grounds.soil:
			for i in range(MapSize):
				for j in range(MapSize):
					till()
					move(dir[3])
				move(dir[0])
	if esc_terra == 1:
		if get_ground_type() == Grounds.Grassland:
			for i in range(MapSize):
				for j in range(MapSize):
					till()
					move(dir[3])
				move(dir[0])
	
	
def trigo():
	arar(0)
	for i in range(MapSize):
		for j in range(MapSize):
			harvest()
			move(dir[3])
		move(dir[0])
	
def arbusto():
	arar(1)
	for i in range(MapSize):
		for j in range(MapSize):
			plant(Plants[1])
			move(dir[3])
		move(dir[0])
	for i in range(MapSize):
		for j in range(MapSize):
			harvest()
			move(dir[3])
		move(dir[0])
	
def arveres_imp(n):
	global pos
	n = get_pos_x()
	pos = n % 2 
	return pos

def arveres():
	for i in range(1):
		if pos == 0:
			for j in range(1):
				plant(Plants[2])
				move(dir[3])
		if pos != 0:
			for j in range(1):
				plant(Plants[1])
				move(dir[3])

def cenora():
	arar(1)
	for i in range(MapSize):
		for j in range(MapSize):
			plant(Plants[3])
			move(dir[3])
		move(dir[0])
	for i in range(MapSize):
		for j in range(MapSize):
			harvest()
			move(dir[3])
		move(dir[0])
	
		
def plantar():
	if esc_plant == Plants[0]:
		trigo()
	if esc_plant == Plants[1]:
		arbusto()
	if esc_plant == Plants[2]:
		for i in range(MapSize):
			for j in range(MapSize):
				arveres_imp(n)
				arveres()
			move(dir[0])
	if esc_plant == Plants[3]:
		cenora()
		
				
while(True):
	esc_plant = Plants[0]
	for i in range(1):
		plantar()
	esc_plant = Plants[1]
	for i in range(1):
		plantar()
	esc_plant = Plants[2]
	for i in range(1):
		plantar()
		colher()
	esc_plant = Plants[3]
	for i in range(1):
		plantar()