function generateIndexLine( parent, index, innerContent ){
    var subIndex;
    var subIndexList;

    subIndex = document.createElement("a");
    // subIndex.setAttribute("style" , "text-decoration:none;margin:0;" );
    subIndex.setAttribute("href" , index );
    subIndex.innerHTML = innerContent;

    subIndexList = document.createElement("li");
    subIndexList.setAttribute("style" , "list-style-type:none;margin:0;" );
    subIndexList.appendChild( subIndex );
    parent.appendChild( subIndexList );
    return subIndexList;
}

function randomString(e) {    
    e = e || 32;
    var t = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz1234567890",
    a = t.length,
    n = "";
    for (i = 0; i < e; i++) n += t.charAt(Math.floor(Math.random() * a));
    return n
}

function autoCreateIndex(){
    var index_0 = document.getElementById("main_index");
    if( !index_0 ) return;
    var index_1 = 0;
    var idCount = 0;

    var tagDivs = document.getElementsByTagName("div");
    var i, j, k;
    var ol_head2, ol_head3;

    for( i = 0; i < tagDivs.length; i++ ){
        if( tagDivs[i].getAttribute("class") == "head head_1" ){
            j = 0;
            // idStr = randomString( 16 )
            idStr = 'MM_' + idCount; idCount++;
            tagDivs[i].setAttribute("id" , idStr );
            index_1 = generateIndexLine( index_0, "#"+idStr, tagDivs[i].innerHTML );

        }else
        if( tagDivs[i].getAttribute("class") == "head head_2" ){
            k = 0;
            if( j == 0 ){
                ol_head2 = document.createElement( "ol" );
                ol_head2.setAttribute("style" , "padding-left:1.5em;" );
                index_1.appendChild( ol_head2 );
                j++;
            }
            idStr = 'MM_' + idCount; idCount++;
            // idStr = randomString( 16 )
            tagDivs[i].setAttribute("id" , idStr );
            index_1 = generateIndexLine( ol_head2, "#"+idStr, tagDivs[i].innerHTML );
        }else
        if( tagDivs[i].getAttribute("class") == "head head_3" ){
            if( k == 0 ){
                ol_head3 = document.createElement( "ol" );
                ol_head3.setAttribute("style" , "padding-left:1.5em;" );
                index_1.appendChild( ol_head3 );
                k++;
            }
            idStr = 'MM_' + idCount; idCount++;
            // idStr = randomString( 16 )
            tagDivs[i].setAttribute("id" , idStr );
            index_1 = generateIndexLine( ol_head3, "#" + idStr, tagDivs[i].innerHTML );
        }
    }
}

function externalLinks(){
    if (!document.getElementsByTagName) return;
    var anchors = document.getElementsByTagName("a");
    for( var i=0; i<anchors.length; i++) {
        if( anchors[i].className != "NoExternal" ){
            anchors[i].setAttribute("target", "_blank" );
            // anchors[i].setAttribute("style", "text-decoration:none;");
        }
    }
}

function CreateBackToTop(){
    var vBackToTop = document.createElement("a");
    vBackToTop.innerHTML="To Top";
    vBackToTop.setAttribute("style","position:fixed;width:60px;height:30px;right:60px;bottom:60px;padding:15px 5px 5px 15px;background-color:#EE5500; border-radius:50px;");
    vBackToTop.setAttribute("href","#main_index");
    document.body.appendChild(vBackToTop);
}


function autoGenSideIndex(){
    tvSideIndexObj = document.getElementById("side_index");
    if( ! tvSideIndexObj ) return;
    tvDynamicStyleObj = document.getElementById("style_area");

    tvHead1UL = document.createElement( 'ul' );

    tvHeadSet = document.getElementsByClassName( 'head' )
    tvHead_1Set = document.getElementsByClassName( 'head_1' )
    findIndex = (set, e ) => {
        for( j = 0; j < set.length; j++ ){ if( set[j] == e ) return j; } return -1;
    }

    var tvInputObj = null;
    var tvLabelObj = null;
    var tvHead_2UlObj;

    console.log( tvHeadSet.length )
    console.log( tvHead_1Set.length )
    for( i = 0; i < tvHeadSet.length; i++ ){
        tvHeadSet[i].id = `index_${i}`
        if( findIndex( tvHead_1Set, tvHeadSet[ i ] )  > 0 ){
            if( tvLabelObj ){
                tvDynamicStyleObj.innerHTML = `${tvDynamicStyleObj.innerHTML}
.side_index input[type='radio']:checked + label[id='${tvLabelObj.id}'] {
height: ${40+30*tvHead_2UlObj.children.length}px;
background: rgb( 100, 100, 100, 0.618 );
text-indent: 4px;
transition-property: height;
transition-duration: 0.6s;
-webkit-transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
}`

                tvHead1ContentDiv = document.createElement( 'div' );
                tvHead1ContentDiv.className = 'side_index_content'
                tvHead1ContentDiv.appendChild( tvHead_2UlObj );

                tvLabelObj.appendChild( tvHead1ContentDiv );

                tvLabelObj.appendChild( tvHead1ContentDiv );
                tvSideIndexObj.appendChild( tvLabelObj );
            }

            tvInputObj = document.createElement( 'input' );
            tvInputObj.id = `side_index_${i}`;
            tvInputObj.name = 'radio';
            tvInputObj.type = 'radio';
            tvSideIndexObj.appendChild( tvInputObj );

            tvLabelObj = document.createElement( 'label' );
            tvLabelObj.id = `side_index_label_${i}`;
            tvLabelObj.htmlFor = tvInputObj.id;

            tvHead_1AObj = document.createElement( 'a' );
            tvHead_1AObj.href = `#${tvHeadSet[ i ].id}`;
            tvHead_1AObj.innerHTML = tvHeadSet[ i ].innerHTML;
            tvSpanObj = document.createElement( 'span' );
            tvSpanObj.appendChild( tvHead_1AObj )

            tvLilArrowDiv = document.createElement( 'div' );
            tvLilArrowDiv.className = 'lil_arrow'

            tvBarDiv = document.createElement( 'div' );
            tvBarDiv.className = 'bar'

            tvLabelObj.appendChild( tvSpanObj );
            tvLabelObj.appendChild( tvLilArrowDiv );
            tvLabelObj.appendChild( tvBarDiv );

            tvHead_2UlObj = document.createElement( 'ul' );
            continue;
        }else{
            tvHead_2LiObj = document.createElement( 'li' );
            tvHead_2LiObj.innerHTML = tvHeadSet[i].innerHTML;

            tvHead_2AObj = document.createElement( 'a' );
            tvHead_2AObj.href = `#${tvHeadSet[i].id}`;
            // tvHead_2AObj.target="_blank"
            tvHead_2AObj.appendChild( tvHead_2LiObj );

            if( tvHead_2UlObj )
                tvHead_2UlObj.appendChild( tvHead_2AObj );
        }

    }
    if( tvLabelObj ){
        tvHead1ContentDiv = document.createElement( 'div' );
        tvHead1ContentDiv.className = 'side_index_content'

        tvHead1ContentDiv.appendChild( tvHead_2UlObj );

        tvLabelObj.appendChild( tvHead1ContentDiv );

        tvLabelObj.appendChild( tvHead_2UlObj );
        tvSideIndexObj.appendChild( tvLabelObj );
    }

}

/**
 * {
 *      "head": [ 1,2 ],
 *      "data": [
 *          [ 1, 2 ],
 *          [ 3, 4 ]
 *      ],
 *      "attr":[
 *          [ 0, 1, 'colspan', 2 ] // row 0, col 1, colspan = 2
 *          [ 0, 0, 'rowspan', 3 ] // row 0, col 0, colspan = 3
 *      ]
 * }
 * 
 * ---->
 * 
 *  |   |   2   |
 *  | 1 | 1 | 2 |
 *  |   | 3 | 4 |
 * 
 * @returns 
 */
function formate_table(){
    tbs = document.getElementsByClassName('tb_format')
    console.log( '---> 0 ', tbs.length )
    for( var i = 0; i < tbs.length; i++ ){
        p = tbs[i]
        tb_txt = p.innerHTML
        if( tb_txt == null ) return;
        js_body = JSON.parse( tb_txt )
        if( js_body == null ) return;
        tb = document.createElement('table')
        // add head
        if( js_body.head != null && js_body.head.length != 0 ){
            head = js_body.head
            tb_tr = document.createElement('tr')
            for( var j = 0; j < head.length; j++ ){
                tb_th = document.createElement('th')
                tb_th.innerHTML = head[j];
                tb_tr.appendChild( tb_th )
            }
            tb.appendChild( tb_tr )
        }
        // add data
        if( js_body.data != null && js_body.data.length != 0 ){
            data = js_body.data
            for( var j = 0; j < data.length; j++ ){
                tb_tr = document.createElement('tr')
                for( var k = 0; k < data[j].length; k++ ){
                    tb_td = document.createElement('td')
                    tb_td.innerHTML = data[j][k];
                    tb_tr.appendChild( tb_td )
                }
                tb.appendChild( tb_tr )
            }
        }
        // add attr
        if( js_body.attr != null && js_body.attr.length != 0 ){
            attr = js_body.attr
            for( var j = 0; j < attr.length; j++ ){
                if( attr[j].length != 4 ) continue;
                row_n = attr[j][0]
                col_n = attr[j][1]
                attr_k = attr[j][2]
                attr_v = attr[j][3]
                // console.log( "attr_k ", attr_k )
                // console.log( "attr_v ", attr_v )

                // console.log( "tb.children.length ", tb.children.length )
                if( row_n < tb.children.length ){
                    // console.log( "tb.children[ row_n ].children.length ", tb.children[ row_n ].children.length )
                    if( col_n < tb.children[ row_n ].children.length ){
                        tb.children[ row_n ].children[ col_n ].setAttribute( attr_k, attr_v )
                    }
                }
            }
        }
        p.innerHTML = null
        p.appendChild( tb )
    }
}
function format_math_fomula(){
    if( typeof(katex) == "undefined" ) return;
    id_prefix = 'latex_str_'
    id_count = 0
    e_fomula = document.getElementsByClassName( 'latex_str' )
    for( var i=0; i<e_fomula.length; i++ ){
        e = e_fomula[i]
        e.id = id_prefix + i
        katex.render( e.innerHTML, e )
    }
}

function format_function_seq_diagram(){
    if( typeof(Diagram) == "undefined" ) return;
    fsd_eles = document.getElementsByClassName( 'fsd' );
    if( fsd_eles ){
        for( var i = 0; i < fsd_eles.length; i++ ){
            e = fsd_eles[ i ]
            estr = e.innerText
            estr = estr.replace('; ','\n')
            e.innerText = "";
            console.log( estr )
            var d = Diagram.parse( estr );
            // var options = {theme: 'hand'};
            var options = {theme: 'simple'};
            d.drawSVG(e, options);
        }
    }
}


externalLinks();
autoCreateIndex();
formate_table();
format_math_fomula();
format_function_seq_diagram();

// var e = document.getElementById('diagram')
// var d = Diagram.parse("A->B: Does something");
// var options = {theme: 'simple'};
// d.drawSVG(e, options);
