import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
	def test_eat_healthy(self):
		self.assetEqual(
				eat("broccoli", is_healthy=True),
				"I'm eating briccoli, beacuse my body is a temp "
			)
	def test_eat_unhealthy(self):
		self.assertEqual(
				eat("pizza", is_healthy=False),
				"I'm eating pizza, beacuse YOLO!"
			)

def test_short_nap(self):
	self.assetEqual(
			nap(1),
			"I'm feeling refreshed after my 1h nap"
		)

def test_long_nap(self):
	self.assetEqual(
			nap(3),
			"Ugh!! I over slept.."
		)
if __name__ == "__main__":
	unittest.main()