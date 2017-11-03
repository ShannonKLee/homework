# Name-markup pairs for each type
TYPE_MARKUPS = {
	"pharmaceutical": 0.075,
	"food": 0.013,
	"electronic": 0.02,
}

FLAT_MARKUP = 0.05
PERSON_MARKUP = 0.012

def calculate_marked_up_price(base_price, num_people, type):
	""" Calculate the marked up value of an item.

	Price packager will first calculate the flat mark up rate of 5%
	and then the persons markup of 1.2% per person and the type markup 
	respectively, if they exist.

	Parameters
	----------
	base_price : float
		The initial price of the item
	num_people : int
		The number of people that worked on the item
	type : str
		The category the item falls under. Each type has its own markup.

	Returns
	-------
	float
		The final price of the item after mark up calculations

	Examples
	--------
	>>> calculate_marked_up_price(1299.99, 3, 'food')
	1591.58
	"""
	
