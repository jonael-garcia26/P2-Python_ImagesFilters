# image_og = [[1,2,3],[3,2,1],[2,1,3]]
# image_copy = []

# for i in image_og:
#     row = []
#     for j in i:
#         row.append(j)
#     image_copy.append(row)



# image_copy.append(10)
# print(image_copy)
# print(image_og)



# x = [1,2,3,4,5,6,7]

# x[2] = 10 + x[2]

# print(x)

# new_image2 = [[10,15,20],[25,30,35],[40,45,50]]
# reverse_im = []

# for i in new_image2:
#     i.reverse()
#     reverse_im.append(i)
# print(new_image2)



new_image4 = [  [1,2,3,4],
                [5,6,7,8], 
                [9,10,11,12],
                [13,14,15,16]  ]
newnewIM = []
Lr = len(new_image4)
Lc = len(new_image4[0])

row1 = []
tile1 = []
for r in range(0,Lr,2):
    #row1 = []
    for c in range(0,Lc,2):
        row1.append(new_image4[r][c])
    tile1.append(row1)
  
# tile2 = []
# for r in range(0,Lr,2):
#     row2 = []
#     for c in range(1,Lc,2):
#         row2.append(new_image4[r][c])
#     tile2.append(row2)

# tile3 = []
# for r in (range(1,Lr,2)):
#     row3 = []
#     for c in range(0,Lc,2):
#         row3.append(new_image4[r][c])
#     tile3.append(row3)

# tile4 = []
# for r in (range(1,Lr,2)):
#     row4 = []
#     for c in range(1,Lc,2):
#         row4.append(new_image4[r][c])
#     tile4.append(row4)

# for r in range(len(tile1)):
#     tilesum1 = tile1[r] + tile2[r]
#     newnewIM.append(tilesum1)

# for r in range(len(tile1)):
#     tilesum2 = tile3[r] + tile4[r]
#     newnewIM.append(tilesum2)

#print(newnewIM)
print(tile1)
# print(tile2)
# print(tile3)
# print(tile4)
