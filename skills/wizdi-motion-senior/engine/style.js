/* TON STYLE — par défaut, le film se construit depuis WIZ_FILM.scenes avec la grammaire pop (pop.js).
   Un senior écrit ici SA chorégraphie : soit en ajoutant des gestes après POP.build(), soit en remplaçant POP.build()
   par un montage à la main avec les briques de window.POP et window.WZ, par exemple :

     const k = "s2", th = POP.TH.navy;
     POP.wipe(WZ.T0(k) + 0.2, th, "iris");                                    // volet sur le temps
     POP.kl({ words: [[WZ.words(k)[0].w, WZ.WT(k, 0), true]], y: 600, size: 240, th });   // mot VERBATIM sur plaque, au mot
     const s = POP.sticker({ name: "play-map", x: 540, y: 1180, w: 980, t0: 3.2, t1: 6 }); // vrai écran en sticker
     POP.enter(s, 3.2, "rise"); POP.felt(s, [1093, 130, 259, 398], 4.0, 5.6, "#1E1B4B");   // écran entier -> feutre
     POP.piece(s, [1093, 130, 259, 398], 4.3, 5.6, { x: 800, y: 1450, w: 259, rot: -3 });   // -> le morceau sort
     WZ.sfx(4.3, "pop", 0.6);                                                  // repère sonore -> tools/mix.py

   Mises en page par format : POP.LAY (zones sûres déjà respectées) ; WZ.FMT, WZ.W, WZ.H, WZ.SAFE. */
(() => {
  "use strict";
  WZ.run(() => {
    POP.build();
  });
})();
