#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def main():
  for i in range(len(picture)):
    pos = ''
    for j in range(len(picture[i])):
      # print(picture[i][j])
      pos = pos + ('*' if picture[i][j] else ' ')
      # if picture[i][j]:
      #   pos = pos + '*'
      # else:
      #   pos = pos + ' '
    print(pos)

if __name__ == '__main__':
  main()
