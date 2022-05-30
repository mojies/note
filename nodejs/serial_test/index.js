const { SerialPort } = require('serialport')
const { Buffer } = require( 'buffer')
const fs = require( 'fs' )
const process = require( 'process' )
// or

if( process.argv.length != 3 ){
	console.error( 'Please specify file name to storage ...' )
	process.exit()
}
console.log( 'G Sensor data save in: ', process.argv[2] )

function calc_and_set_crc( buf, size ){
	crc = 0xFFFF
	
	for( var i = 0; i < size; i++ ){
		crc = buf[i] ^ crc
		for( var j = 0; j < 8; j++ ){
			if( crc&0x01 ){
				crc = crc>>1;
				crc=crc ^ 0xA001;
			}else{
				crc = crc >> 1;
			}
		}
	}
	buf[ size ] = crc & 0xFF
	buf[ size + 1 ] = (crc & 0xFF00)>>8
}


// 00 06 00 ff 07 d0 bb 87
// 0x00, 0x06, 0x00, 0xFF, 0x00, 0xC8, 0xb9, 0xbd -- 10Hz
// 0x00, 0x06, 0x00, 0xFF, 0x00, 0x01, 0x79, 0xEB -- 2000hZ
function get_change_sample_rate_cmd( sample_rate ){
	rate = parseInt( 2000/sample_rate )
	cmd = new Buffer.from([
		0x00, 0x06, 0x00, 0xFF, 0x00, 0xC8, 0xb9, 0xbd ]);
	cmd[4] = (rate&0xFF00)>>8;
	cmd[5] = rate&0xFF;
	
	calc_and_set_crc( cmd, 6 )
	return cmd
}

/*
// Read data that is available but keep the stream in "paused mode"
port.on('readable', function () {
  console.log('Data:', port.read())
})
// Pipe the data into another stream (like a parser or standard out)
const lineStream = port.pipe(new Readline())
*/

function calc_acceleration( hi_b, low_b, precision ){
	if( hi_b&0x80 ){
		val = (hi_b << 8) + low_b - 0x10000
	}else{
		val = (hi_b&0x7F << 8) + low_b
	}
	val /= 20.5
	if( precision )
		val = val.toFixed( precision );
	return val
}

/*
remain = []
found_head = false
function save_serial_data( fd, data ){
	if( l_save_fd == null )	return
	
	// find head
	if( found_head == false ){
		for( var i = 0; i < data.length - 3; i++ ){
			if( data[i ] != 0x00 ||
				data[i + 1] != 0x03 ||
				data[i + 2] != 0x06 ){
					continue;
				}
			if( i != 0 )
				data = data.subarray( i )
			found_head = true
			break;
		}
		if( found_head == false )
			return
	}

	// save pos
	buf_data = remain.length + data.length
	batch_size = parseInt( buf_data / 11 )*11;
	remain_size = buf_data % 11
	data_valid_size = data.length - remain_size

	console.log( ' data: ', data.length, ' remain:', remain.length, ' batch:', batch_size ); 

	var x, y, z
	for( var i = 0 ; i <  data_valid_size; ){
		if( remain.length > 0 ){
			var cp_size = 11 - remain.length
			for( var j = 0; j < cp_size; j++ )
				remain.push( data[i] );

			x = calc_acceleration( remain[4], remain[3], 2 )
			y = calc_acceleration( remain[6], remain[5], 2 )
			z = calc_acceleration( remain[8], remain[7], 2 )

			console.log( "remain :: ", remain )
			remain = []
			i += cp_size;
		}else{
			if( data[i ] != 0x00 ||
				data[i + 1] != 0x03 ||
				data[i + 2] != 0x06 ){
					console.log( "data err :: ", i )
				}
			x = calc_acceleration( data[i + 4], data[i + 3], 2 )
			y = calc_acceleration( data[i + 6], data[i + 5], 2 )
			z = calc_acceleration( data[i + 8], data[i + 7], 2 )
			
			i += 11;
		}
		
		str = x + ', ' + y + ', ' + z + '\n';
		fs.write( fd, str, 0, str.length, ( err, bytesWritten, buffer )=>{
			if( err )
				console.log( err )
		});
	}
	
	for( var i = data.length - remain_size; i < data.length; i++ )
		remain.push( data[ i ] );	
}
*/

l_save_fd = null
l_sys_comms = []

fs.open( process.argv[2], 'a+', (err, fd) => {
	if( err ){
		console.log( err )
		return;
	}
	l_save_fd = fd;
} )

// get serial port list
SerialPort.list().then((data) => {
	console.log( data )
	l_sys_comms = data
} )

// open serial port list
// 460 800
const port = new SerialPort({
	path: "COM4",
	baudRate: 460800
})

port.open( (err) => {
	if( err ){
		console.log( err )
		return
	}
	// port.write
} )

port.on( "open", ()=>{
	// console.log( "opened -> ", get_change_sample_rate_cmd( 1000 ) )
	port.write( get_change_sample_rate_cmd( 1000 ) )
} )



// Switches the port into "flowing mode"
port.on('data', function (data) {
	// console.log('Data:', data)
	// save_serial_data( l_save_fd, data )
	fs.write( l_save_fd, data, 0, data.length, ( err, bytesWritten, buffer )=>{
		if( err )
			console.log( err )
	});
})

