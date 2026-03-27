#isso controla a bagunça do first_attempt
import main
from main import *
plants = 1
while True:
	if plants == 1:
		brobas()
		if num_items(Items.Power) >= 1500:
			plants += 1
		else:
			gira_o_sol_all()
			colheita_toda()
	if plants == 2:
		if num_items(Items.Carrot) <= 75000:
			plants += 1
		else:
			brobas()
	if plants == 3:
		if num_items(Items.Carrot) >= 150000:
			plants -= 1
		else:
			cenoura()
	if plants == 4:
		trigo()
		plants += 1
	if plants == 5:
		bustos()
		