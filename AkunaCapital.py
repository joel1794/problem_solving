import json


class MarkingPositionMonitor:
    def __init__(self):
        self.orders = {}

    def on_event(self, message):
        message = json.loads(message)
        symbol = ''
        if message['order_id'] in self.orders:
            symbol = self.orders[message['order_id']]['symbol']
        if message['type'] == 'NEW':
            self.orders[message['order_id']] = {
                'symbol': message['symbol'],
                'side': message['side'],
                'curr': 0,
                'last_op': message,
                'remaining': 0,
                'cancelled': False
            }
            symbol = message['symbol']
            if message['side'] == 'SELL':
                self.orders[message['order_id']]['curr'] = message['quantity']
        elif message['type'] == 'ORDER_ACK':
            pass
        elif message['type'] == 'ORDER_REJECT':
            self.orders[message['order_id']]['curr'] = 0
        elif message['type'] == 'CANCEL':
            pass
        elif message['type'] == 'CANCEL_ACK':
            if self.orders[message['order_id']]['side'] == 'BUY':
                pass
                # self.orders[message['order_id']]['curr'] = self.orders[message['order_id']]['remaining']
            else:
                self.orders[message['order_id']]['curr'] = self.orders[message['order_id']]['remaining']
            self.orders[message['order_id']]['cancelled'] = True

        elif message['type'] == 'CANCEL_REJECT':
            pass
        elif message['type'] == 'FILL':
            if not self.orders[message['order_id']]['cancelled']:
                if self.orders[message['order_id']]['side'] == 'BUY':
                    self.orders[message['order_id']]['curr'] += message['filled_quantity']
                elif self.orders[message['order_id']]['side'] == 'SELL':
                    self.orders[message['order_id']]['remaining'] += message['filled_quantity']

        out = 0
        for key in self.orders.keys():
            if self.orders[key]['symbol'] == symbol:
                if self.orders[key]['side'] == 'BUY':
                    out += self.orders[key]['curr']
                else:
                    out -= self.orders[key]['curr']
        return out