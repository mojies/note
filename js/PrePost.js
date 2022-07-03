function generateIndexLine( parent, index, innerContent ){
    var subIndex;
    var subIndexList;

    subIndex = document.createElement("a");
    subIndex.setAttribute("style" , "text-decoration:none;" );
    subIndex.setAttribute("href" , index );
    subIndex.innerHTML = innerContent;

    subIndexList = document.createElement("li");
    subIndexList.setAttribute("style" , "list-style-type:none;" );
    subIndexList.appendChild( subIndex );
    parent.appendChild( subIndexList );
    return subIndexList;
}

function autoCreateIndex(){
    var index_0 = document.getElementById("main_index");
    if( !index_0 ) return;
    var index_1 = 0;

    var tagDivs = document.getElementsByTagName("div");
    var index_count = 1
    var i, j, k;
    var ol_head2, ol_head3;

    for( i = 0; i < tagDivs.length; i++ ){
        if( tagDivs[i].getAttribute("class") == "head head_1" ){
            j = 0;
            tagDivs[i].setAttribute("id" , "subTitle_head1_"+index_count.toString() );
            index_1 = generateIndexLine( index_0, "#subTitle_head1_"+index_count.toString(), tagDivs[i].innerHTML );
            index_count++;
        }else
        if( tagDivs[i].getAttribute("class") == "head head_2" ){
            k = 0;
            if( j == 0 ){
                ol_head2 = document.createElement( "ol" );
                ol_head2.setAttribute("style" , "padding-left:1.5em;" );
                index_1.appendChild( ol_head2 );
                j++;
            }
            tagDivs[i].setAttribute("id" , "subTitle_head2_"+index_count.toString() );
            index_1 = generateIndexLine( ol_head2, "#subTitle_head2_"+index_count.toString(), tagDivs[i].innerHTML );
            index_count++;
        }else
        if( tagDivs[i].getAttribute("class") == "head_3" ){
            if( k == 0 ){
                ol_head3 = document.createElement( "ol" );
                ol_head3.setAttribute("style" , "padding-left:1.5em;" );
                index_1.appendChild( ol_head3 );
                k++;
            }
            tagDivs[i].setAttribute("id" , "subTitle_head3_"+index_count.toString() );
            index_1 = generateIndexLine( ol_head3, "#subTitle_head3_"+index_count.toString(), tagDivs[i].innerHTML );
            index_count++;
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


externalLinks();
autoCreateIndex();
formate_table();
format_math_fomula();

