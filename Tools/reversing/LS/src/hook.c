//
//======================================================================
// 
//    88888888
//   88      888                                         88    88
//  888       88                                         88
//  788           Z88      88  88.888888     8888888   888888  88    8888888.
//   888888.       88     88   888    Z88   88     88    88    88   88     88
//       8888888    88    88   88      88  88       88   88    88   888
//            888   88   88    88      88  88888888888   88    88     888888
//  88         88    88  8.    88      88  88            88    88          888
//  888       ,88     8I88     88      88   88      88   88    88  .88     .88
//   ?8888888888.     888      88      88    88888888    8888  88   =88888888
//       888.          88
//                    88    www.synetis.com
//                 8888  Consulting firm in management and information security
// 
// Fabien DROMAS - Security Consultant @ Synetis | 0xbadcoded
//
//--
//SYNETIS | 0xbadcoded
//CONTACT: www.synetis.com | ww.0xbadcoded.com
//======================================================================
//

#include <stdio.h>
 
int strcmp(const char *s1, const char *s2) {
    printf("[Hook strcmp]\n");
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    return 0;
}

int strncmp(const char *s1, const char *s2, size_t n) {
    printf("[Hook strncmp]\n");
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    return 0;
}
