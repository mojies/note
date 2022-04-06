#include <stdio.h>
#include <ctype.h>
#include "mdebug.h"

unsigned debug_level = MDEBUG_DEF_LEVEL;

static unsigned char hex_charset[] = "0123456789ABCDEF";
void mdebug_print_hex( unsigned char *buf, int len ){
    int r_len;
    int i,j;

    if( len%16 == 0 )
        r_len = len;
    else
        r_len = (((len>>4)+1)<<4);

    for( i = 0; i < r_len; ){
        if( i < len )
            printf( "%c%c ", hex_charset[ ( buf[i]&0xF0 ) >> 4 ],
                    hex_charset[ buf[i]&0x0F ] );
        else
            printf( "   " );

        i++;
        if( i !=0 && i%8 == 0 ) printf( "    " );

        if( (i%16 == 0) && (i != 0) ){
            printf( "          " );
            for( j=i-16; j<i; j++ ){
                if( j < len ){
                    if( isprint(buf[j]) )
                        printf("%c", buf[j]);
                    else
                        printf(".");
                }
            }
            printf( "\n" );
        }
    }
    printf( "\n" );
}

#ifdef MD_SUPPORT_CJSON
int showCjson( cJSON *ipData ){
    DLLOGW( "----------------------------" );
    DLLOGV( "next -> %p", ipData->next );
    DLLOGV( "prev -> %p", ipData->prev );
    DLLOGV( "child -> %p", ipData->child );

    switch( ipData->type ){
    case cJSON_False:
        DLLOGV( "type -> cJSON_False" );
    break;
    case cJSON_True:
        DLLOGV( "type -> cJSON_True" );
    break;
    case cJSON_NULL:
        DLLOGV( "type -> cJSON_NULL" );
    break;
    case cJSON_Number:
        DLLOGV( "type -> cJSON_Number" );
    break;
    case cJSON_String:
        DLLOGV( "type -> cJSON_String" );
    break;
    case cJSON_Array:
        DLLOGV( "type -> cJSON_Array" );
    break;
    case cJSON_Object:
        DLLOGV( "type -> cJSON_Object" );
    break;
    case cJSON_IsReference:
        DLLOGV( "type -> cJSON_IsReference" );
    break;
    case cJSON_StringIsConst:
        DLLOGV( "type -> cJSON_StringIsConst" );
    break;
    default: break;
    }

    DLLOGV( "valuestring -> %s", ipData->valuestring );
    DLLOGV( "valueint -> %d", ipData->valueint );
    DLLOGV( "valuedouble -> %lf", ipData->valuedouble );
    DLLOGV( "string -> %s", ipData->string );

    return 0;
}
#endif

