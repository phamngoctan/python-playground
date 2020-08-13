import queue
deck = queue.Queue()

while (True):
  n = int(input())
  if (n == 0):
    break;
  
  for i in range(1, n + 1):
    deck.put(i)
  # print(list(deck.queue))
  
  discarded_cards = []
  while deck.qsize() >= 2:
    discarded_cards.append(deck.get())
    deck.put(deck.get())
  
  print('Discarded cards: ' if discarded_cards else 'Discarded cards:', end='')
  print(*discarded_cards, sep=', ')
  print("Remaining card: {}".format(deck.get()))