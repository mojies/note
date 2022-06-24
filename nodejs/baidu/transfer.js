const https = require( 'https' );
const url = require('url');
const fs = require('fs')
var crypto = require('crypto');


var _SHAREURL_ = 'https://pan.baidu.com/share/list?uk=2627974806&shareid=27036616852&showempty=0&web=1&page=1&num=100&dir=/sharelink2627974806-606796177741645/13.马牛+Android第二期&dp-logid=57982000176960430029'
var _COOKIE_ = 'XFI=c42ecf8e-083b-da17-a6f4-00d509d5874e; XFCS=8AAAAF18CE5F6B30D040ABB2FCBBA2BF631A1938BFBB1E14C6DA1C63D91A4EAE; BIDUPSID=76F3D1375D89FA2D2A945D1C0E0085BF; PSTM=1615951412; __yjs_duid=1_1a5393ae0b4607c9c8099e76b26e2f661618904685283; PANWEB=1; pan_login_way=1; csrfToken=4HslkOHlpzL8GL3pGfWygMoR; secu=1; H_WISE_SIDS=110085_127969_174442_179345_184716_188744_189755_190621_194085_194511_194519_194530_197242_197711_198263_199023_199177_199580_201193_202651_203310_203518_203525_204122_204713_204715_204864_204904_205218_205485_205838_205909_206007_206196_206929_206992_207236_207716_207830_207864_207895_208113_208268_208686_208721_208816_208971_209395_209437_209512_209568_209707_209748_209842_209944_209957_209980_210099_210125_210163_210307_210359_210440_210566_210585_210614_210642_210653_210669_210732_210736_210891_210892_210894_210900_210907_211114_211170_211181_211242_211302_211313_211441_211457_211580_211733_211756_211783_211924_211958_212416; BDUSS=jBCMnhlM1o5dzI5UEhFMjc5NkRUNUxRMDJyfkxNRlQxQmxPT0JRY21-QlJScTFpSVFBQUFBJCQAAAAAAAAAAAEAAAAU0KQN8vzo7rartqsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFG5hWJRuYViM; BDUSS_BFESS=jBCMnhlM1o5dzI5UEhFMjc5NkRUNUxRMDJyfkxNRlQxQmxPT0JRY21-QlJScTFpSVFBQUFBJCQAAAAAAAAAAAEAAAAU0KQN8vzo7rartqsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFG5hWJRuYViM; BDSFRCVID=A-tOJeC629Mvb1rDrqifJFvNmmmCl0oTH6f3JiR2ZMkMzwFkToLEEG0PSU8g0Kubwo9jogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=JbAtoKD-JKvMeJjzqRQaq4tehHR8JT39WDTm_Doy040bexbeyh3Oy-De-l5uJjJZQmnN-pPKKR7ZDpotXx5-0b8TX-bAKP6L3mkjbpvyfn02OPKzMM8We-4syPRr2xRnWTRiKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hI0Cjj8bj5PhM2TqhtQX-KIX3b7Efbvo8h7_bf--DRLdKJQB-f3ZWgTP-R6d-CbkMxQNQJ5xy5K_hU7U2pOIb2JB_xtayxbUOUoHQT3myP5bbN3i3xr40KoyWb3cWKOJ8UbSjh3PBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eG_fq6_eJJFsL-35HtO2Htocqtn25KCShUFX5-Cs5G6C2hcH0KLKEpvxDtbCQMIn5-vP2xvDJNAq2hjHWfb1MRjvMh5MjPDrhGQ3qpj-5DrqWp5TtUJcJKnTDM4Mqq_EeqjyKMnitKv9-pP2LpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj50hjT5QeH8saJc32PoKQbcVKRA_fb7xepQh0M4pbt-qJftLJCbwBqbubbA-SqOa365V2bJ-5HJnBT5ht2CLah5O5xb-shCljtrbLp_kQN3TWnkO5bRiLlCaJJ_-Dn3oyTbJXp0njb3ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJAj_ILXfIt-bP365ITt5tAjhMrMan32ato2WDvpH4bcOR5Jj6KBXJKVDq5RbJo05eQlLqrEaR6TDKJv3MA-b6tpMJKHXfrWB6QfKJvmahRpsq0x0hble-bQypoa--482DOMahkb5h7xOKbMQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_tTKDtbRP; BDSFRCVID_BFESS=A-tOJeC629Mvb1rDrqifJFvNmmmCl0oTH6f3JiR2ZMkMzwFkToLEEG0PSU8g0Kubwo9jogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvMeJjzqRQaq4tehHR8JT39WDTm_Doy040bexbeyh3Oy-De-l5uJjJZQmnN-pPKKR7ZDpotXx5-0b8TX-bAKP6L3mkjbpvyfn02OPKzMM8We-4syPRr2xRnWTRiKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hI0Cjj8bj5PhM2TqhtQX-KIX3b7Efbvo8h7_bf--DRLdKJQB-f3ZWgTP-R6d-CbkMxQNQJ5xy5K_hU7U2pOIb2JB_xtayxbUOUoHQT3myP5bbN3i3xr40KoyWb3cWKOJ8UbSjh3PBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eG_fq6_eJJFsL-35HtO2Htocqtn25KCShUFX5-Cs5G6C2hcH0KLKEpvxDtbCQMIn5-vP2xvDJNAq2hjHWfb1MRjvMh5MjPDrhGQ3qpj-5DrqWp5TtUJcJKnTDM4Mqq_EeqjyKMnitKv9-pP2LpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuj50hjT5QeH8saJc32PoKQbcVKRA_fb7xepQh0M4pbt-qJftLJCbwBqbubbA-SqOa365V2bJ-5HJnBT5ht2CLah5O5xb-shCljtrbLp_kQN3TWnkO5bRiLlCaJJ_-Dn3oyTbJXp0njb3ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJAj_ILXfIt-bP365ITt5tAjhMrMan32ato2WDvpH4bcOR5Jj6KBXJKVDq5RbJo05eQlLqrEaR6TDKJv3MA-b6tpMJKHXfrWB6QfKJvmahRpsq0x0hble-bQypoa--482DOMahkb5h7xOKbMQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_tTKDtbRP; BAIDUID=DB639EAF14D43C1C21B54F5A2B52C116:SL=1:NR=20:FG=1; delPer=0; PSINO=7; BAIDUID_BFESS=7F4AC5CB9ED771284A80C88876A25683:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ZD_ENTRY=google; RT="z=1&dm=baidu.com&si=3s8hzf58924&ss=l4nm48be&sl=0&tt=0&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=eu&ul=1aii9v&hd=1aiib6"; STOKEN=2eafdb2b5cadf3107e88cc01b429761ba1dbb4900c824db1fcc18b5c1f6eb92d; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1655870316; BDCLND=lizd5rAAD5B7O6AoBdJtDYzNsDSDz8xHyYRHWmqHZGY=; Hm_lvt_fa0277816200010a74ab7d2895df481b=1655880172; Hm_lpvt_fa0277816200010a74ab7d2895df481b=1655880172; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1655913522; ndut_fmt=E675C43CF1184A8E1B719A97927C478265A60B0DA3B46D47A0A2D8FA7F58E4BC; ab_sr=1.0.1_ODQ3NGNhZmM5MjYwZWFhNDdkMjBkMjQ5N2RhYmNjNjJjY2FlN2QyMDM4YjM3Yzc5MzQ0MjkxYTYzYWFiODdjMTQ3MTg0ZTAyYjdlODcyODY2YzIzMjcyNmExMGU3ZTQ4ZWVkZGRiMjVkNTBhZDc3ZmQyM2M0MzIzZGNiOGI4MWY1YzgxYzZlNWM1ZDg0MTIwNTllNmY5ODhjZmYwZTkzZA==; H_PS_PSSID=36550_36462_36506_36454_36666_36453_36424_36167_26350_36469_22160; BA_HECTOR=8lal80842l20a5050k1hb6fp215; ZFY=A7li9mhgdnv:An4nI7p8FJ8uFonWNhVukztv4weFv:AZc:C; PANPSC=1791027686946209517:WhZG6HNMmFpNlDw3XjWtW1cS2d9ns3O5xVrlVHpNQtfyuQVqVBPOzWT/MK3iZvOoBm6rqQ5QdYKnxd6x6fgcph7LGPr5Gu0v4i2i1JdCg+Q3uGXWluwqDpS/fHPAnK/XIermaD9w8EPWHyYIIPcWSQa1N2Fbvw47tmG6JOMhdEynUE78w4JYB+qLq/KLYkvEnk07pVeJTA6E3yEvfHd7u6dQTvzDglgH6our8otiS8SeTTulV4lMDo8H55OGUR6+'
var _B_TARGET = '/教材/码牛'

var _USER_AGENT_ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

var _B_clienttype = "0"
var _B_app_id = "250528"
/*
{
  errno: 0,
  result: {
    bdstoken: 'fce0a86463671f45bb1844bd94799bf1',
    token: '7011fybfwftEPR9dDMI+H7WDsBCJKXsmvATnaQJJ2MPg+si0cjIjuZvGkFIZawTl3+sQL/neNZvQwmzHQc3iRcynkVTkwLx/g4j3Bkpd+d1jbP/WbYXHHElpktkAS3bHLMO1ZAVtM3DijLL1HJW+VbNorQWV2d0zCUA2MPr2ngnh2AqJt0ojkleVyofnJ2DZI4prj+shWNT9CpeyzRndgVhzCjRydrbrcieaIrxf8pw7QVsVtn9uqdDlJ0lvK6o/HYx
1MA7E6v6Xk6QDP8y/cTLUFHLmBT2BvU9CxiWtH5S0Tu80zOQ',
    uk: 3490273915,
    isdocuser: 1,
    servertime: 1655913243
  },
  request_id: 553498254131866240
}
*/
var _B_share = null
var _B_templatevariable = {}
// _B_templatevariable.result.bdstoken

var _HIS_FILE_NAME = './' + crypto.createHash('md5').update( _SHAREURL_ + _B_TARGET ).digest('hex');

/*
{
    from
    to
    from_id
}
*/
var _COPY_LIST = []


function parse_share_url(){
    tmp = url.parse( _SHAREURL_ )
    split_qury = tmp.query.split('&')
    _B_share = {}
    split_qury.forEach( (e)=>{
        kv = e.split('=')
        _B_share[ kv[0] ] = kv[1]
    } )
    console.log( '_B_share -> ', _B_share )
}
// --------------------> parse share url
parse_share_url()

// --------------------> load config
console.log( _HIS_FILE_NAME )
// process.exit();

function load_config(){
    if( fs.existsSync( _HIS_FILE_NAME ) ) {
        _COPY_LIST = JSON.parse( fs.readFileSync( _HIS_FILE_NAME, {encoding:'utf8', flag:'r'}) )
    }
}

function save_config(){
    fs.writeFileSync( _HIS_FILE_NAME, JSON.stringify( _COPY_LIST ) )
}

// ===============================================================================================
function build_url( pathname, query ){
    query.clienttype = _B_clienttype
    query.app_id = _B_app_id
    query.web = 1
    // query[ 'dp-logid' ] = _B_share['dp-logid']
    query[ 'dp-logid' ] = '57982000176960430034'

    query_str = ''
    Object.keys( query ).forEach( (k)=>{
        query_str += k + '=' + query[ k ] + '&'
    } )

    query_str = query_str.slice(0,query_str.length-1)
    return url.format( {
          protocol: 'https:',
          host: 'pan.baidu.com',
          // search: '?clienttype=0&app_id=250528&web=1&dp-logid=43730200987295310039&order=name&desc=0&dir=/教材/码牛/01&num=100&page=1',
          //       ?clienttype=0&app_id=250528&web=1&dp-logid=43730200987295310040 &a=commit&bdstoken=fce0a86463671f45bb1844bd94799bf1
          search: '?' + query_str,
          pathname: pathname,
    } )
}

function build_get_basic_info_url(){
    query = {
        fields: '["bdstoken","token","uk","isdocuser","servertime"]',
    }

    u1 = build_url( '/api/gettemplatevariable', query )
    console.log( u1 )
    return u1
}

function build_get_share_dir_content_url( dir, page ){
    query = {
        uk: _B_share.uk,
        shareid: _B_share.shareid,
        showempty: _B_share.showempty,
        page: page,
        num: _B_share.num,
        dir: dir,
    }

    u1 = build_url( '/share/list', query )
    console.log( u1 )
    return u1
}

function build_copy_url(){
    query = {
        from: _B_share.uk,
        shareid: _B_share.shareid,
        'async': '1',
        ondup: 'newcopy',
        bdstoken: _B_templatevariable.result.bdstoken,

        // sekey: encodeURIComponent('lizd5rAAD5B7O6AoBdJtDYzNsDSDz8xHyYRHWmqHZGY='),
        // channel: 'chunlei',
        // logid: 'REI2MzlFQUYxNEQ0M0MxQzIxQjU0RjVBMkI1MkMxMTY6U0w9MTpOUj0yMDpGRz0x',
    }

    u1 = build_url( '/share/transfer', query )
    console.log( u1 )
    return u1
}

function build_copy_content( fsid, dest_path ){
    str = 'fsidlist=' + encodeURIComponent( '[' + fsid + ']' ) 
        + '&path=' + encodeURIComponent( dest_path )
    console.log( str )
    return str
}


function build_create_dir_url(){
    l_search = 'a=commit&bdstoken=fce0a86463671f45bb1844bd94799bf1'
    query = {
        bdstoken: _B_templatevariable.result.bdstoken,
        // a: 'commit',
    }

    u1 = build_url( '/api/create', query )
    console.log( u1 )
    return u1
}

// ===============================================================================================
function build_header( method, content ) {
    var opt = {
        method: method,
        headers: {
            'Cookie': _COOKIE_,
            'User-Agent': _USER_AGENT_,
            'Accept': 'application/json, text/plain, */*',
        },
    }
    opt.headers[ 'Host' ] = 'pan.baidu.com';
    opt.headers[ 'Origin' ] = 'https://pan.baidu.com';
    opt.headers[ 'Referer' ] = 'https://pan.baidu.com/s/1Bkz8zKMPWgOK4DN0R9OmDw?pwd=7Nvg';
    // opt.headers[ 'X-Requested-With' ] = 'XMLHttpRequest'
    
    if( content != null ){
        opt.headers[ 'Content-Type' ] = 'application/x-www-form-urlencoded; charset=UTF-8';
        opt.headers[ 'Content-Length' ] = content.length;
    }
    return opt
}

/*
 * cb( err, json_data )
 */
function http_query( url, opt, content, cb ){
    if( cb == null ) cb = (err,data)=>{};

    if( content != null && content.length != 0 ){
        opt.headers[ 'Content-Type' ] = 'application/x-www-form-urlencoded; charset=UTF-8';
        opt.headers[ 'Content-Length' ] = content.length;
    }
    // console.log( 'request head -> ', opt )

    var data = null

    setTimeout(function(){
        req = https.request( url, opt,
        (res) => {
            console.log('http_query statusCode -> ', res.statusCode);
            console.log('http_query headers -> ', res.headers);

            res.on('data', (d) => {
                if( data == null )
                    data = d
                else data += d

            });
            res.on('end', () => {
                var tmp = JSON.parse( data )
                if( tmp.errno != 0 ){
                    console.error( 'ERR http_query 1--> ', tmp );
                    cb( true, tmp )
                }else{
                    cb( false, tmp )
                }
            });
        });
        req.on('error', (e) => {
            console.error( 'ERR http_query --> ', e );
            cb( true, e )
            return
        });
        if( content != null && content.length != 0 ){
            // console.log( 'write data: ', content )
            req.write( content )
        }
        req.end();
    }, 1000);
}

// ===============================================================================================
// pan.baidu.com/api/gettemplatevariable?clienttype=0&app_id=250528&web=1&dp-logid=85286100145914230004&
function get_basic_info( cb ){
    http_query( build_get_basic_info_url(), build_header( 'GET' ), null, ( err, data ) => {
        if( err ) return;
        _B_templatevariable = data
        console.log( '_B_templatevariable -> ', _B_templatevariable )
        if( cb != null ) cb()
    } )
}

function get_share_dir( path, sublist, page, cb ){
    if( cb == null )
        cb = ( err, data )=>{}

    if( _B_share == null )
        return;
    if( sublist == null ){
        sublist = []
        page = 1
    }

    http_query(
    build_get_share_dir_content_url( path, page ),
    build_header( 'GET' ), null, ( err, data ) => {
        if( err ){
            console.log( 'get dir file list failed: ', copy_item.path );
            cb( true, err )
            return;
        }

        if( data.errno != 0 ) {
            console.log( 'Get dir file list resp error -> ', data );
            cb( true, data )
            return;
        };

        if( data.list.length == 0 ){
            cb( false, sublist )
            return;
        }

        data.list.forEach( (e) => {
            sublist.push( e )
        } )

        if( data.list.length == _B_share.num ){
            get_share_dir( path, sublist, page + 1, cb );
        }else{
            cb( false, sublist )
        }
    } )
}

/*
POST
pan.baidu.com
/share/transfer
?
    clienttype=0&
    dp-logid=57982000176960430034

    shareid=27036616852&
    from=2627974806&
    web=1&
    app_id=250528&

    bdstoken=fce0a86463671f45bb1844bd94799bf1&
    async=1&
    ondup=newcopy&

    sekey=lizd5rAAD5B7O6AoBdJtDYzNsDSDz8xHyYRHWmqHZGY=&
    channel=chunlei& ???
    logid=REI2MzlFQUYxNEQ0M0MxQzIxQjU0RjVBMkI1MkMxMTY6U0w9MTpOUj0yMDpGRz0x& ???

fsidlist=%5B897054675545398%5D&path=%2F%E6%95%99%E6%9D%90%2F%E7%A0%81%E7%89%9B%2F01
fsidlist: [897054675545398]
path: /教材/码牛/01
*/
function copy_share_dir_2_my_dir( fsid, dest_path, cb ){
    if( _B_share == null )
        return;

    opt = build_header( 'POST' )

    http_query( build_copy_url(), opt,
    build_copy_content( fsid, dest_path ), ( err, data ) => {
        if( err ){
            cb( true, data )
            return
        };
        console.log( 'share dir data -> ', data )
        if( cb != null ) cb( false, data )
    } )
}

function create_path( path, cb ){
    if( _B_share == null )
        return;

    path = encodeURIComponent(path)
    content = 'path=' + path + '&isdir=1&block_list=%5B%5D'

    opt = build_header( 'POST', content )

    http_query( build_create_dir_url(), opt, content, ( err, data ) => {
        if( err ){
            console.log( 'create dir failed: ', path )
            cb( true, data )
            return;
        }
        // console.log( 'create dir data -> ', data )
        console.log( 'create dir success: ', path )
        if( cb != null ) cb( false, data )
    } )
}

function batch_copy_progress(){
    if( _COPY_LIST.length == 0 ) return;

    var copy_item = _COPY_LIST.pop()
    save_config();

    copy_share_dir_2_my_dir( copy_item.fs_id, copy_item.to, ( err, data ) => {
        if( err == false ){
            batch_copy_progress();
            return;
        }
        if( copy_item.isdir != 1 ){
            if( (data.errno == 12) || (data.errno == 4) ){
                _COPY_LIST.unshift( copy_item )
                save_config();
                setTimeout( ()=>{
                    batch_copy_progress();
                }, 10000)
            }
            return;
        }

        path_arr = copy_item.path.split( '/' )
        var l_target_path = copy_item.to + '/' + path_arr[ path_arr.length - 1 ]

        create_path( l_target_path, ( err, data ) => {
            if( err )return;

            get_share_dir( copy_item.path, [], 1, ( err, data ) => {
                // console.log( 'SHARE:', copy_item.path, ' resp.data -> ', data );
                if( err ){
                    console.log( 'get dir file list failed: ', copy_item.path );
                    return;
                }

                data.forEach( (e) => {
                    e.to = l_target_path
                    _COPY_LIST.push( e )
                } )
                save_config()
                console.log( '_COPY_LIST -> ', _COPY_LIST.length )
                batch_copy_progress()
            } )

        } )
    } )
}

get_basic_info( () => {
    if( _COPY_LIST.length == 0 ){
        get_share_dir( _B_share.dir, [], 1, ( err, data ) => {
            console.log( 'share base data -> ', data );
            if( err ){
                console.log( 'get share base data failed ...' );
                return;
            }
            data.forEach( (e) => {
                e.to = _B_TARGET
                _COPY_LIST.push( e )
            } )
            save_config();
            batch_copy_progress()
        } )
    }else{
        batch_copy_progress()
    }

    // copy_share_dir_2_my_dir( '897054675545398', '/教材/码牛/01' );
} )

// build_get_share_dir_content_url( '/sharelink2627974806-606796177741645/13.马牛+Android第二期', 1 )


// create_path( '/教材/码牛/01/testmojies' )
