import os
import numpy as np
import matplotlib.pyplot as plt

FIX_FILE = './fix.raw'
NORMAL_FILE = './normal.raw'
BOX_FILE = './box1.raw'


def check_entry_crc( buf, pos ):
    if buf[ pos ] != 0x00 or buf[ pos + 1 ] != 0x03 or buf[ pos + 2 ] != 0x06:
        return False
    crc = 0xFFFF
    for i in range( 11 - 2 ):
        crc = crc ^ buf[ pos + i ]
        for j in range(8):
            if ( crc & 0x01 ) == 0x01:
                crc = crc>>1;
                crc = crc ^ 0xA001;
            else:
                crc = crc >> 1;
    # print( 'calc_crc:%04x, buf_crc:%02x %02x'%( crc, buf[pos+9], buf[pos+10] ) )
    if buf[ pos + 9 ] != (crc & 0xFF) or buf[ pos + 10 ] != ((crc & 0xFF00)>>8):
        return False
    else:
        return True

def conv_sensor_2_real_val( hi_b, low_b, precision ):
    val = 0
    if( hi_b&0x80 ):
        val = (hi_b << 8) + low_b - 0x10000
    else:
        val = (hi_b&0x7F << 8) + low_b
    val /= 20.5
    if( precision != None ):
        return round( val, precision)
    return val

def parse_G_x_y_z( buf, pos ):
    return [
        conv_sensor_2_real_val( buf[pos + 4], buf[pos + 3], 3 ),
        conv_sensor_2_real_val( buf[pos + 6], buf[pos + 5], 3 ),
        conv_sensor_2_real_val( buf[pos + 8], buf[pos + 7], 3 )
    ]

def find_start( file_path ):
    with open( file_path, 'rb' ) as fd:
        want_read = 11

        buf = fd.read( want_read );
        rlen = len( buf )
        start_i = 0

        for i in range(rlen):
            if buf[ i ] != 0x00 or buf[ i+1 ] != 0x03 or buf[ i+2 ] != 0x06:
                continue
            start_i = i
            break

        fd.close()
    return start_i



def get_G_x_y_z( file_path, offset ):
    file_size = os.stat(file_path).st_size
    count = 0

    gxyz = [ ]
    remain = []

    with open( file_path, 'rb' ) as fd:
        want_read = 11*1000
        fd.seek( offset )

        while True:
            if fd.tell() == file_size:
                break
            buf = fd.read( want_read );
            print( 'buf -> ', len(buf) )

            if len( remain ) > 0:
                buf = list(buf)
                for i in range( len( remain ) ):
                    buf.insert( 0, remain[i] )

            rlen = len(buf)
            pos = 0
            
            while pos < rlen:
                if (rlen - pos) < 11:
                    while pos < rlen:
                        remain.append( buf[pos] )
                        pos += 1
                    break;

                if check_entry_crc( buf, pos ) == False:
                    pos += 1
                    continue

                [ x, y, z ] = parse_G_x_y_z( buf, pos )
                # gxyz[ 'x' ].append(x)
                # gxyz[ 'y' ].append(y)
                # gxyz[ 'z' ].append(z)
                gxyz.append( [x, y, z] )
                
                pos += 11

                count += 1
                if count%100 == 0:
                    print( "(%d) -> x:%.02f y:%.02f z:%.02f "%(count, x, y, z ) )

        fd.close()

    return gxyz

def get_G_xyz_avg( G_xyz ):
    return np.mean( G_xyz, 0 )

# print( 'start_i: %d'%( find_start() ) )
fix_arr = get_G_x_y_z( FIX_FILE, 0 )
normal_arr = get_G_x_y_z( NORMAL_FILE, 0 )
box_arr = get_G_x_y_z( BOX_FILE, 0 )

fix_avg = get_G_xyz_avg( fix_arr )
fix_avg[2] = fix_avg[2] - 1

normal_fixed = np.subtract( normal_arr, fix_avg )
normal_x = normal_fixed[:,0]
normal_y = normal_fixed[:,1]
normal_z = normal_fixed[:,2]
normal_range = range( len( normal_x ) )

box_fixed = np.subtract( box_arr, fix_avg )
box_x = box_fixed[:,0]
box_y = box_fixed[:,1]
box_z = box_fixed[:,2]
box_range = range( len( box_x ) )


# =========================================================================
# -------------------------------------------------------------------------
plt.subplot(3,2,1)
plt.title('refer.x')
plt.plot( normal_range, normal_x );

plt.subplot(3,2,3)
plt.title('refer.y')
plt.plot( normal_range, normal_y );

plt.subplot(3,2,5)
plt.title('refer.z')
plt.plot( normal_range, normal_z );

# -------------------------------------------------------------------------
plt.subplot(3,2,2)
plt.title('box.x')
plt.plot( box_range, box_x );
plt.subplot(3,2,4)
plt.title('box.y')
plt.plot( box_range, box_y );
plt.subplot(3,2,6)
plt.title('box.z')
plt.plot( box_range, box_z );

plt.show()


