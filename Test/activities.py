def eat(food, is_healthy):
	ending = "Because YOLO!"
	if is_healthy:
		ending = "Because my body is a temple"
	return f"I'm eating {food}, {ending}"

def nap(num_hours):
	if num_hours >= 2:
		return f"Ugh!! I over slept.."
	return f"I'm feeling refreshed after my {num_hours} nap"