﻿
include "cpc464.ccz80";
array byte Aguila = { 14, 7, 8, 56,
    #22, #33, #33, #33, #22, #00, #00, #00, #33, #3C, #3C, #3C, #39, #11, #22, #00,
    #11, #39, #36, #33, #3C, #63, #93, #00, #33, #3C, #3C, #3C, #39, #11, #22, #00,
    #22, #33, #33, #33, #22, #00, #00, #00, #00, #11, #00, #11, #00, #00, #00, #00,
    #00, #33, #22, #33, #22, #00, #00, #00, #11, #11, #33, #33, #33, #00, #00, #00,
    #11, #36, #3C, #3C, #3C, #22, #33, #00, #00, #36, #33, #39, #36, #39, #C3, #22,
    #11, #36, #3C, #3C, #3C, #22, #33, #00, #11, #11, #33, #33, #33, #00, #00, #00,
    #00, #00, #22, #00, #22, #00, #00, #00, #00, #11, #33, #11, #33, #00, #00, #00
};


byte t;
mode(1);
ink(1, 24, 24);
ink(2, 9, 9);
ink(3, 6, 6);
window(21, 40, 13, 25);
paper(3);
cls();
prints(" Window number 0");
stream(1);
window(1, 20, 1, 12);
paper(2);
cls();
prints(" Window number 1");
              // while (1)
              // {
              stream(0);
              locate(1, 6);
              prints(" Red window (0)  ");
              stream(1);
              locate(1, 6);
              prints(" Green window (1)");
              // for (t = 1; t <= 20; ++t) frame(); // Delay
              windowswap(0, 1);
              prints("hola");
              windowswap(0, 1);
              prints("sadfasdfas");
              windowswap(1, 0);
              // }