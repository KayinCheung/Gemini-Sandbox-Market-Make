#Universal constants
REQUIRED_VOL = 1
MINIMUM_ROWS_TO_CHECK = 3

class OrderBook:
	def __init__(self, data):
		
		self.BUY_total_vol = 0
		self.SELL_total_vol = 0
		self.buy_rows_checked = 0
		self.sell_rows_checked = 0
		self.buy_vol_at_limit = 0
		self.sell_vol_at_limit = 0

		for row in data["bids"]:
 
			self.BUY_total_vol += float(row["amount"])
			self.buy_rows_checked +=1

			if self.buy_rows_checked >= MINIMUM_ROWS_TO_CHECK:
				if self.BUY_total_vol >= REQUIRED_VOL:
					self.buy_limit_price = float(row["price"])
					self.buy_vol_at_limit = float(row["amount"])
					break


		for row in data["asks"]:
		
			self.SELL_total_vol += float(row["amount"])
			self.sell_rows_checked +=1
			
			if self.sell_rows_checked >= MINIMUM_ROWS_TO_CHECK:
				if self.SELL_total_vol >= REQUIRED_VOL:
					self.sell_limit_price = float(row["price"])
					self.sell_vol_at_limit = float(row["amount"])
					break
