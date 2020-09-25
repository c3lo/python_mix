import math

def taupunkt(temperatur_in_celsius: float, relative_feuchte: float) -> float:
	""" Diese Näherung gilt nur für den Temperaturbereich von -45 bis 60 Grad Celsius"""
	K_1 = 17.62
	K_2 = 243.12 # Grad Celsius 

	assert relative_feuchte <= 1.0
	assert relative_feuchte >= 0.0

	try: 

		if temperatur_in_celsius <= 60.0 and -45.0 <= temperatur_in_celsius:
		
			return K_2 * ((K_1*temperatur_in_celsius)/(K_2 + temperatur_in_celsius) + math.log(relative_feuchte)) / ((K_1*K_2)/(K_2 + temperatur_in_celsius) - math.log(relative_feuchte))
		else:
			raise ValueError

	except AssertionError:
		print("Luftfeuchtigkeit muss ein Wert von 0 bis 1 sein!")
