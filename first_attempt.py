#funciona mas é uma bagunça pura que nem eu entendo  que cada coisa faz

clear()

Plants = {Entities.Grass,Entities.bush,Entities.tree,Entities.carrot,Entities.sunflower,Entities.pumpkin,Entities.dead_pumpkin}
map= 22
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
x1_1 = 0
x2_1 = 0
broba = Entities.Pumpkin
f_broba = Entities.Dead_Pumpkin
cenora = Entities.Carrot
girassol = Entities.Sunflower

def map_todo():
	while get_pos_x() != 11 and get_pos_y() != 11:
		print(get_pos_x())
		print(get_pos_y())
		if get_pos_y() == 11:
			for i in range(map):
				move(East)
				break
		else:
			for i in range(map):
				move(East)
		move(North)
		
		
def ta_arado():
	if get_ground_type() != Grounds.soil:
		for i in range(map):
			till()
			move(East)
			
def regar():
	if get_entity_type() == cenora or girassol:
		for i in range(map):
			use_item(Items.water)
			move(East)

def miku():
	while get_entity_type() == None:
		if get_pos_x() == 0:
			break
		if get_entity_type() == None:
			move(East)
		
def agrotoxic():
	for i in range(map):
		use_item(Items.Fertilizer)
		move(East)
	for i in range(map):
		if num_items(Items.Weird_Substance) >= 10000:
			use_item(Items.Weird_Substance, 1000)
			move(East)	
									
def colhe_devagar():
	if can_harvest():
		harvest()
		move(East)
	if can_harvest() == False:
		if get_entity_type() == Entities.dead_pumpkin:
				harvest()
				move(East)
		elif can_harvest() == False:
			if get_entity_type() == None and get_entity_type() != Entities.dead_pumpkin:
				miku()
				while get_entity_type() == None:
					if get_pos_x() == 0:
						break
					elif get_entity_type() == None:
						move(East)
		while can_harvest() == False and get_entity_type() != None and get_entity_type() != f_broba:
			do_a_flip()
		harvest()
		move(East)
			

def checar():
	if get_pos_x() == 0:
		move(North)
	else:
		while get_pos_x() != 0:
			move(East)
			if get_pos_x() == 0:
				move(North)

def colhe_esq():
	for i in range(map):
		harvest()
		move(West)		
	
def arvre():
	get_pos_x()
	get_pos_y()
	if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 1:
		return True
	else:
		return False

def gira_o_sol():
	global x1
	global x2
	global x3
	global x4
	global x1_1
	global x2_1
	for i in range(1):
		regar()
	for i in range(map):
		measure()
		if measure() == 15:
			x1 = get_pos_x()
		elif measure() == 15 and x1 != 0:
			x1_1 = get_pos_x()
		if measure() == 14:
			x2 = get_pos_x()
		elif measure() == 14 and x2 != 0:
			x2_1 = get_pos_x()
		if measure() == 13:
			x3 = get_pos_x()
		if measure() == 12:
			x4 = get_pos_x()
		move(East)
		for i in range(1):
			if x1 != 0:
				while get_pos_x() != x1:
					move(East)
					if get_pos_x() == x1:
						while can_harvest() == False:
							do_a_flip()
						if can_harvest():
							harvest() 
				x1 = 0
			if x1_1 != 0:
				while get_pos_x() != x1_1:
					move(East)
					if get_pos_x() == x1_1:
						while can_harvest() == False:
							do_a_flip()
						if can_harvest():
							harvest() 
				x1_1 = 0

			if x2 != 0:
				while get_pos_x() != x2:
					move(East)
					if get_pos_x() == x2:
						while can_harvest() == False:
							do_a_flip()
						if can_harvest():
							harvest() 
				x2 = 0
				
			if x2_1 != 0:
				while get_pos_x() != x2_1:
					move(East)
					if get_pos_x() == x2_1:
						while can_harvest() == False:
							do_a_flip()
						if can_harvest():
							harvest() 
				x2_1 = 0
				
def colheita_toda():
	global map
	for i in range(map):
		for j in range(map):
			if get_pos_x() == 0 and get_pos_y() == 0:
				do_a_flip()
			if can_harvest():
				harvest()
				move(East)
			elif can_harvest() == False:
				if get_entity_type() == Entities.dead_pumpkin:
					harvest()
					move(East)
				elif can_harvest() == False:
					if get_entity_type() == None and get_entity_type() != Entities.dead_pumpkin:
						miku()
						while get_entity_type() == None:
							if get_pos_x() == 0:
								break
							elif get_entity_type() == None:
								move(East)
				while can_harvest() == False and get_entity_type() != None and get_entity_type() != f_broba:
					do_a_flip()
		move(North)
	
def colheita_toda_cac():
	global map
	for i in range(map):
		harvest()
		move(East)
		for i in range(1):
			move(South)
			for i in range(1):
				colhe_esq()
				move(South)
	
def colheita_f_broba():
	global map
	for i in range(map):
		for j in range(map):
			if get_entity_type() == broba:
				move(East)
			while get_entity_type() == Entities.dead_pumpkin:
				harvest()
				plant(broba)
				do_a_flip()
				if get_entity_type() != Entities.dead_pumpkin:
					move(East)
			if can_harvest() == False:
				if get_entity_type() == None and get_entity_type() != Entities.dead_pumpkin:
					miku()
					while get_entity_type() == None:
						if get_pos_x() == 0:
							break
						elif get_entity_type() == None:
							move(East)
			while can_harvest() == False and get_entity_type() != None and get_entity_type() != f_broba:
				do_a_flip()
			if get_pos_x() == 0 and get_pos_y() == 0:
				do_a_flip()
		move(North)

def colheita_brobas():
	for i in range(map):
		for j in range(map):
			harvest()
			move(East)
		move(North)

def brobas():
	for i in range(map):
		for j in range(1):
			ta_arado()
			for k in range(map):
				plant(broba)
				move(East)
		move(North)
	for i in range(2):
		colheita_f_broba()
	colheita_brobas()


def trigo():
	clear()
	colheita_toda()


def arveres():
	clear()
	for i in range(map):
		for j in range(map):
			plant(Entities.Tree)
			move(East)
			plant(Entities.bush)
			move(East)
		move(North)
	for i in range(1):
		colheita_toda()

def bustos():
	clear()
	for i in range(map):
		for j in range(map):
			plant(Entities.bush)
			move(East)
		move(North)
	for i in range(map):
		for j in range(1):
			agrotoxic()
		move(North)

		
def cenoura():
	for i in range(map):
		for j in range(1):
			ta_arado()
			for k in range(map):
				plant(cenora)
				move(East)
		move(North)
	for j in range(1):
		colheita_toda()
		
def meas_dir():
	for i in range(map):
		measure()
		measure(North)
		measure(East)
		measure(West)
		measure(South)
		if measure(North) < measure():
			swap(North)
		if measure(East) < measure():
			swap(East)
		if measure(West) > measure():
			swap(West)
		if measure(South) > measure():
			swap(South)
		move(East)

def meas_esq():
	for i in range(map):
		measure()
		measure(North)
		measure(East)
		measure(West)
		measure(South)
		if measure(North) < measure():
			swap(North)
		if measure(East) < measure():
			swap(East)
		if measure(West) > measure():
			swap(West)
		if measure(South) > measure():
			swap(South)
		move(West)
	
def cactu():
	for i in range(map):
		for j in range(1):
			ta_arado()
			for k in range(map):
				plant(Entities.Cactus)
				move(West)
		move(North)
	for k in range(4):
		for i in range(1):
			for i in range(map):
				for j in range(1):
					meas_dir()
					for l in range(1):
						meas_esq()
				move(South)
		for i in range(map):
			move(North)
	for i in range(1):
		colheita_toda_cac()
		
				
def gira_o_sol_all():
	global x1
	global x2
	global x3
	global x4
	global x5
	global x6
	global y1
	global y2
	global y3
	global y4
	global y5
	global y6
	for i in range(map):
		for j in range(1):
			ta_arado()
			for k in range(map):
				plant(girassol)
				measure()
				if measure() == 15 and x1 == 0 and y1 == 0:
					x1 = get_pos_x()
					y1 = get_pos_y()
				if measure() == 15 and x1 != 0 and y1 != 0:
					x2 = get_pos_x()
					y2 = get_pos_y()
				if measure() == 15 and x2 != 0 and y2 != 0:
					x3 = get_pos_x()
					y3 = get_pos_y()
				if measure() == 15 and x3 != 0 and y3 != 0:
					x4 = get_pos_x()
					y4 = get_pos_y()
				if measure() == 15 and x4 != 0 and y4 != 0:
					x5 = get_pos_x()
					y5 = get_pos_y()
				if measure() == 15 and x5 != 0 and y5 != 0:
					x6 = get_pos_x()
					y6 = get_pos_y()
				move(East)
		move(North)
	for i in range(0):
		if x1 != 0 and y1 != 0:
			while get_pos_x() != x1  and get_pos_y() != y1:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x1 and get_pos_y() == y1:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest() 
						move(East)
					move(North)
				x1 = 0
				y1 = 0
							
		if x2 != 0 and y2 != 0:
			while get_pos_x() != x2 and get_pos_y() != y2:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x2 and get_pos_y() == y2:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest()
						move(East)
					move(North)
				x2 = 0
				y2 = 0
		
		if x3 != 0 and y3 != 0:
			while get_pos_x() != x3 and get_pos_y() != y3:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x3 and get_pos_y() == y3:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest() 
						move(East)
					move(North)
				x3 = 0
				y3 = 0
					
		if x4 != 0 and y4 != 0:
			while get_pos_x() != x4 and get_pos_y() != y4:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x4 and get_pos_y() == y4:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest() 
						move(East)
					move(North)
				x4 = 0
				y4 = 0
							
		if x5 != 0 and y5 != 0:
			while get_pos_x() != x5 and get_pos_y() != y5:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x5 and get_pos_y() == y5:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest()
						move(East)
					move(North)
				x5 = 0
				y5 = 0
					
		if x6 != 0 and y6 != 0:
			while get_pos_x() != x6 and get_pos_y() != y6:
				for i in range(map):
					for j in range(map):
						if get_pos_x() == x6 and get_pos_y() == y6:
							while can_harvest() == False:
								break
							if can_harvest():
								harvest()
						move(East)
					move(North)
				x6 = 0
				y6 = 0
		
		
	
			
		
		
	
			
				
while False:		
	for i in range(map):
		colhe_devagar()
	checar()	
	for i in range(map ):
		colhe_devagar()
	checar()
	for i in range(map):
		plant(Entities.bush)
		move(East)
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		ta_arado()
		plant(Entities.carrot)
		move(East)
	for i in range(1):
		regar()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		ta_arado()
		plant(Entities.carrot)
		move(East)
	for i in range(1):
		regar()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	checar()
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	move(South)
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	checar()
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	checar()
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	move(South)
	for i in range(map):
		ta_arado()
		plant(broba)
		move(East)
	move(South)
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		if arvre() == True:
			plant(arvere)
			move(East)
		else:
			ta_arado()
			plant(girassol)
			move(East)
		if get_entity_type() == girassol:
			gira_o_sol()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		if arvre() == True:
			plant(arvere)
			move(East)
		else:
			ta_arado()
			plant(girassol)
			move(East)
		if get_entity_type() == girassol:
			gira_o_sol()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		if arvre() == True:
			plant(arvere)
			move(East)
		else:
			ta_arado()
			plant(girassol)
			move(East)
		if get_entity_type() == girassol:
			gira_o_sol()
	for i in range(map):
		colhe_devagar()
	checar()
	for i in range(map):
		ta_arado()
		plant(girassol)
		move(East)
	if get_entity_type() == girassol:
		gira_o_sol()
	for i in range(map):
		colhe_devagar()
	checar()
	
	