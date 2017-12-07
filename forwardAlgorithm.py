states = ('Rainy', 'Sunny')
 
observations = ('walk', 'shop', 'clean')
 
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
 
transition_probability = {
   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
   'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
}
 
emission_probability = {
   'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
   'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
}

# Implementing the forward algorithm to calculate the p(xt | y1:t)
# xt is the state, y1:t are the observations
# Define at(xt) = (yt|xt) * sum(p(xt|xt-1)*p(xt-1|y1:t-1)) **sum means sum all the possibility of xt-1
# In this case is Sunny or Rainy

def forward(evidences):

	n_iteration = len(evidences)
	y1 = evidences[0]

	Sunny = start_probability['Sunny'] * emission_probability['Sunny'][y1]
	Rainy = start_probability['Rainy'] * emission_probability['Rainy'][y1]
	curValue = (Rainy, Sunny)

	for i in range(1,n_iteration):
		yi = evidences[i]
		xiSunny = emission_probability['Sunny'][yi] * (transition_probability['Sunny']['Sunny'] * curValue[1] +
														transition_probability['Sunny']['Rainy'] * curValue[0])
		xiRainy = emission_probability['Rainy'][yi] * (transition_probability['Rainy']['Sunny'] * curValue[1] +
														transition_probability['Rainy']['Rainy'] * curValue[0])
		curValue = (xiRainy, xiSunny)

	res = (curValue[0]/(curValue[0] + curValue[1]), curValue[1]/(curValue[0] + curValue[1]))

	return res


if __name__ == '__main__':

	p = forward(['clean','clean','clean'])
	print(p)
	print("The probability of rainy is: %.2f" %(p[0]))
	print("The probability of sunny is: %.2f" %(p[1]))