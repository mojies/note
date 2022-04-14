import cv2
import numpy as np



PEER_INC = [
    [-1,-1], [-1,0], [-1,1],
    [ 0,-1],         [ 0,1],
    [ 1,-1], [ 1,0], [ 1,1] ]

def infect_to_dark( img, pos, threshold ):
    pos_buf = []
    pos_buf.append( pos )
    h_max = img.shape[0]
    w_max = img.shape[1]
    count = 0

    # print( "x-> %d, y -> %d"%( pos[0], pos[1] ) );    
    img[ pos[0] ][ pos[1] ] = 0
    while len(pos_buf) > 0:
        # set to dark
        count += 1
        (x, y) = pos_buf.pop()
        
        # print( "pos buf len -> %d"%(len(pos_buf)) )
            
        for i in range(len(PEER_INC)):
            h = x + PEER_INC[i][0]
            w = y + PEER_INC[i][1]
            if h < 0 or h >= h_max:
                continue;
            if w < 0 or w >=  w_max:
                continue;
            if img[ h ][ w ] < threshold:
                continue;
            img[ x ][ y ] = 0
            pos_buf.append( ( h, w ) )
    
    # cv2.imshow( "haha", img )
    # cv2.waitKey(0)
    return count

def find_room( img_bin, mean, min_area ):
    w = img_bin.shape[1]
    h = img_bin.shape[0]

    rooms = []

    for hi in range(h):
        for wi in range(w):
            if img_bin[hi][wi] > mean:
                count = infect_to_dark( img_bin, (hi, wi), mean )
                if count > min_area:
                    rooms.append( (hi, wi) )
    # cv2.imshow( "haha", img_bin )
    # cv2.waitKey(0)
    return rooms
# print( "img_bin shape -> ", img_bin.shape )
# rooms = find_room( img_bin.copy(), mean, BOX[0] * BOX[1] )


find_border_tentacle = [
                [ -1, 0 ],
    [ 0, -1 ],              [ 0, 1 ],
                [ 1, 0],

]

find_border_direct = [
                [ 1, 0 ],
    [ 0, 1 ],              [ 0, -1 ],
                [ -1, 0],

]


def find_border( img, dir_vector ):
    border = []
    pos_buf = []
    pos_buf.append( ( 0, 0 ) )

    x_max = img.shape[0]
    y_max = img.shape[1]

    flag = np.zeros( img.shape )
    flag[0][0] = 1

    count = 0
    while len( pos_buf ) > 0:
        for i in range( len( pos_buf ) ):
            count += 1
            # print( "count -> %d %d"%( y_max*x_max, count ) );
            (x, y)  =  pos_buf.pop(0)

            black_count = 0
            black_pos = None
            for i in range( len( find_border_tentacle ) ):
                x_n = x + find_border_tentacle[i][0]
                y_n = y + find_border_tentacle[i][1]
                # print( "x-> %d, y -> %d"%( x_n, y_n ) );
                if x_n >= x_max or y_n >= y_max:
                    continue
                if x_n < 0 or y_n < 0:
                    continue

                if img[x][y] != 0 and img[ x_n ][ y_n ] == 0:
                    black_count += 1
                    black_pos = i

                if flag[x_n][y_n] == 1:
                    continue;

                pos_buf.append( ( x_n, y_n ) )
                flag[x_n][y_n] = 1


            if black_count > 0:
                border.append( (x, y) )
                if black_count == 1:
                    dir_vector[x][y] = [ find_border_direct[black_pos][0], find_border_direct[black_pos][1] ]

    return border

PEERS = [
    [ -1, -1 ], [ -1, 0 ], [ -1, 1 ],
    [  0, -1 ],            [  0, 1 ],
    [  1, -1 ], [  1, 0 ], [  1, 1 ],
]

PEERS_WEIGHT = [
    1,1,1,
    1,  1,
    1,1,1,
]
def smooth_border( img, border, skip ):
    POS_LEN = len( PEERS )
    x_max = img.shape[0]
    y_max = img.shape[1]

    flag = np.zeros( img.shape )
    arch = np.zeros( img.shape )

    weigths = []
    new_border = []
    count = 0

    for i in range( len( border ) ):
        ( x, y ) = border[i]
        flag[x][y] = 1

    # print( "x_max: ", x_max )
    # print( "y_max: ", y_max )
    print( "len( border ): ", len( border ) )

    # while count < times:
    while len( border ) > 0:
        count += 1
        for i in range( len( border ) ):
            ( x, y ) = border[i]
            sum = 0
            for i in range( POS_LEN ):
                x_peer = int(x + PEERS[i][0])
                y_peer = int(y + PEERS[i][1])
                if x_peer < 0 or y_peer < 0 or x_peer >= x_max or y_peer >= y_max:
                    continue
                # print( "1.1 ", x_peer )
                # print( "1.2 ", y_peer )
                # print( "1 ", img[x_peer][y_peer] )
                # print( "2", PEERS_WEIGHT[i] )

                sum += img[x_peer][y_peer] * PEERS_WEIGHT[i]

            weigths.append( sum )

        print( "border len ", len(border) )
        print( "weight len ", len(weigths) )
        for i in range( len( border ) ):
            ( x, y ) = border[i]

            if ( count <= skip and weigths[ i ] <= (255*4)) or ( count > skip and weigths[ i ] <= (255*8)) :
                img[x][y] = 0
                for j in range( len( PEERS ) ):
                    x_peer = int(x + PEERS[j][0])
                    y_peer = int(y + PEERS[j][1])
                    if x_peer < 0 or y_peer < 0 or x_peer >= x_max or y_peer >= y_max:
                        continue
                    if img[x_peer][y_peer] == 0:
                        continue
                    if flag[x_peer][y_peer] == 1:
                        continue
                    flag[x_peer][y_peer] = 1
                    new_border.append( ( x_peer, y_peer ) )
                if count > skip:
                    print( "i ", i )
                    if weigths[ i ] <= (255*4):
                        arch[x][y] = 255
            else:
                new_border.append( ( x, y ) )
        border = new_border
        new_border = []
        weigths = []

        cv2.imshow( "haha", img )
        cv2.waitKey(0)
    
    cv2.imshow( "arch", arch )
    cv2.waitKey(0)
    

def draw_arch( img, border, skip, score, dir_vector ):    
    img1 = img.copy()
    count = 0

    x_max = img.shape[0]
    y_max = img.shape[1]
    flag = np.zeros( img.shape )

    while len( border ) > 0:
        count += 1
        for i in range( len( border ) ):
            ( x, y ) = border.pop(0)
            x_inc = dir_vector[x][y][0]
            y_inc = dir_vector[x][y][1]

            img1[ x ][ y ] = 0

            if count > skip:
                if x_inc == 0 and y_inc == 0:
                    score[ x ][ y ] = 255

            x_new = int(x + x_inc)
            y_new = int(y + y_inc)
            if x_new < 0 or y_new < 0 or x_new >= x_max or y_new >= y_max:
                continue

            # print( "x_new -> %s, y -> %d"%( x_new, y_new ) )
            if flag[x_new][y_new] == 1:
                dir_vector[ x_new ][ y_new ] = [ 0, 0 ]
            else:
                flag[x_new][y_new] = 1
                border.append( ( x_new, y_new ) )
                dir_vector[ x_new ][ y_new ] = [ x_inc, y_inc ]    
        # cv2.imshow( "haha", img1 )
        # cv2.waitKey(0)


    # cv2.imshow( "haha", score )
    # cv2.waitKey(0)


EXPAND = 1
BOX = [10, 10]

img = cv2.imread( '0.pgm', 0 )
print( img.shape )

# ---------> resize
# img_h = img.shape[0]
# img_w = img.shape[1]
# dim = ( img_w*EXPAND, img_h*EXPAND )
# img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# ---------> convert
# img2 = img1.copy()
# img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# print( img1.shape );
# print( img2.shape );
# print( img2.shape );


mean = int(np.mean(img))
print( "mean -> %d"%( mean ) )
ret, img_bin = cv2.threshold( img, mean, 255, cv2.THRESH_BINARY )
# cv2.imshow( "haha", img_bin )
# cv2.waitKey(0)

score = np.zeros( img.shape )
score[0][0] = 0
direct_vector = np.zeros( (img.shape[0],img.shape[1],2)  )

# ---------> find border
border = find_border( img_bin, direct_vector )
print( "border len -> %d"%(len( border ) ) )
flag = np.zeros( img.shape )
for pos in border:
    flag[ pos[0] ][ pos[1] ] = 255

smooth_border( img_bin, border, 10 )

# # cv2.imwrite( 'out.png', flag)

# ---------> find arch
# draw_arch( img_bin, border, 1, score, direct_vector )


