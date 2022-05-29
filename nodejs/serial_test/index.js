const { SerialPort } = require('serialport')
const { Buffer } = require( 'buffer')
// or



// get serial port list
l_sys_comms = []
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

/*
uint16_t ModbusCRC(uint8_t *ptr,uint16_t len)
{
	uint8_t i;
	uint16_t j,crc=0xffff;
	
	i=i;	
	for(int n=0;n<len;n++)
	{
		crc=ptr[n]^crc;
		for(int i=0;i<8;i++)
		if(crc&0x01)
		{
			crc=crc>>1;
			crc=crc^0xa001;
		}
		else
			crc=crc>>1;	
				
	}
	j=crc>>8;
	j=j|(crc<<8);
	return j;
}
*/


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

port.on( "open", ()=>{
	// console.log( "opened -> ", get_change_sample_rate_cmd( 1000 ) )
	port.write( get_change_sample_rate_cmd( 1000 ) )
} )
/*
// Read data that is available but keep the stream in "paused mode"
port.on('readable', function () {
  console.log('Data:', port.read())
})
// Pipe the data into another stream (like a parser or standard out)
const lineStream = port.pipe(new Readline())
*/

function calc_acceleration( hi_b, low_b ){
	if( hi_b&0x80 ){
		val = (hi_b << 8) + low_b - 0x10000
	}else{
		val = (hi_b&0x7F << 8) + low_b
	}
	val /= 20.5
	return val
}


count = 0;
// Switches the port into "flowing mode"
port.on('data', function (data) {
  // console.log('Data:', data.length)
  console.log('Data:', data.length)
  x = calc_acceleration( data[4], data[3] )
  y = calc_acceleration( data[6], data[5] )
  z = calc_acceleration( data[8], data[7] )

	count += data.length/11;
	console.log( "count -> ", count );
	
  console.log('X:', x, "Y:", y, "Z:", z)
})

