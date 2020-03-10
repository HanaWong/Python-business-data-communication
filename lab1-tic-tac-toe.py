# ''' TIC TAC TOE '''

geam_orig = {'1': '-' , '2': '-' , '3': '-', 
   '4': '-' , '5': '-' , '6': '-',
   '7': '-' , '8': '-' , '9': '-'}
def Board(Updated_Board):
  print( Updated_Board['1'] + " " + Updated_Board['2'] + ' ' + Updated_Board['3'] )
  print( Updated_Board['4'] + " " + Updated_Board['5'] + ' ' + Updated_Board['6'] )
  print( Updated_Board['7'] + " " + Updated_Board['8'] + ' ' + Updated_Board['9'] )
turn = 'A'

while True:
  Board(geam_orig)
  if '-' not in geam_orig.values():
    print(" It's a Draw")
    break
  print( '1 = Top Left \n2 = Top Middle \n3 = Top Right')
  print( '4 = Middle Left \n5 = Middle Middle \n6 = Middle Right') 
  print( '7 = Bottom Left \n8 = Bottom Middle \n9 = Bottom Right')
  pos = input( turn + "'s turn. \n Enter the position where you want to insert:\n")
  if geam_orig.get(pos,'-')!='-':
    print('The position is already Filled. Please enter another position \n')
    continue
  if geam_orig.get(pos,0):
    geam_orig[pos]=turn
  else:
    print('\n\nEnter Valid input')
    continue
    
  if turn == 'A':
    if (geam_orig['1'] == geam_orig['2'] == geam_orig['3']!='-' or 
      geam_orig['4'] == geam_orig['5'] == geam_orig['6']!='-' or 
      geam_orig['7'] == geam_orig['8'] == geam_orig['9']!='-' or  
      geam_orig['1'] == geam_orig['5'] == geam_orig['9']!='-' or 
      geam_orig['3'] == geam_orig['5'] == geam_orig['7']!='-' or 
      geam_orig['1'] == geam_orig['4'] == geam_orig['7']!='-' or 
      geam_orig['2'] == geam_orig['5'] == geam_orig['8']!='-' or 
      geam_orig['3'] == geam_orig['6'] == geam_orig['9']!='-'):
      print( "'"+turn + '\' Wins')
      Board(geam_orig)
      break
    turn = 'B'

  else: 
    if(geam_orig['1'] == geam_orig['2'] == geam_orig['3']!='-' or 
      geam_orig['4'] == geam_orig['5'] == geam_orig['6']!='-' or 
      geam_orig['7'] == geam_orig['8'] == geam_orig['9']!='-' or  
      geam_orig['1'] == geam_orig['5'] == geam_orig['9']!='-' or 
      geam_orig['3'] == geam_orig['5'] == geam_orig['7']!='-' or 
      geam_orig['1'] == geam_orig['4'] == geam_orig['7']!='-' or 
      geam_orig['2'] == geam_orig['5'] == geam_orig['8']!='-' or 
      geam_orig['3'] == geam_orig['6'] == geam_orig['9']!='-'):
      print("\n\n '"+turn + '\' Wins')
      Board(geam_orig)
      break
    turn = 'A'
