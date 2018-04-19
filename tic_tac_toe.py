grid = ['1','2','3','4','5','6','7','8','9']
wins = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

def tic_tac_toe():
  print(grid[0],'|',grid[1],'|',grid[2])
  print("---------")
  print(grid[3],'|',grid[4],'|',grid[5])
  print("---------")
  print(grid[6],'|',grid[7],'|',grid[8])

def turn():
  while True:
    grid[grid.index(input(''))] = input('')
    print(grid[0],'|',grid[1],'|',grid[2])
    print("---------")
    print(grid[3],'|',grid[4],'|',grid[5])
    print("---------")
    print(grid[6],'|',grid[7],'|',grid[8])
    if grid[0] == 'x' and grid[1] == 'x' and grid[2] == 'x':
      print ('X WINS!')
    elif grid[3] == 'x' and grid[4] == 'x' and grid[5] == 'x':
      print ('X WINS!')
    elif grid[6] == 'x' and grid[7] == 'x' and grid[8] == 'x':
      print ('X WINS!')
    elif grid[0] == 'x' and grid[3] == 'x' and grid[6] == 'x':
      print ('X WINS!')
    elif grid[1] == 'x' and grid[4] == 'x' and grid[7] == 'x':
      print ('X WINS!')
    elif grid[2] == 'x' and grid[5] == 'x' and grid[8] == 'x':
      print ('X WINS!')
    elif grid[0] == 'x' and grid[4] == 'x' and grid[8] == 'x':
      print ('X WINS!')
    elif grid[2] == 'x' and grid[4] == 'x' and grid[6] == 'x':
      print ('X WINS!')
    elif grid[0] == 'o' and grid[1] == 'o' and grid[2] == 'o':
      print ('O WINS!')
    elif grid[3] == 'o' and grid[4] == 'o' and grid[5] == 'o':
      print ('O WINS!')
    elif grid[6] == 'o' and grid[7] == 'o' and grid[8] == 'o':
      print ('O WINS!')
    elif grid[0] == 'x' and grid[3] == 'o' and grid[6] == 'o':
      print ('O WINS!')
    elif grid[1] == 'o' and grid[4] == 'o' and grid[7] == 'o':
      print ('O WINS!')
    elif grid[2] == 'o' and grid[5] == 'o' and grid[8] == 'o':
      print ('O WINS!')
    elif grid[0] == 'o' and grid[4] == 'o' and grid[8] == 'o':
      print ('O WINS!')
    elif grid[2] == 'o' and grid[4] == 'o' and grid[6] == 'o':
      print ('O WINS!')

tic_tac_toe()
turn()