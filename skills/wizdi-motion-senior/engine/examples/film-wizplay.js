/* EXEMPLE COMPLET — la chorégraphie du film WizPlay pop du 13/10/2026 (22 s, 7 phrases), réécrite pour ce moteur.
   À copier à la place de film.js quand on a : la narration (words.js : s1…s7), les vrais médias du produit
   (tools/media.py add play-trailer|play-map|play-lock|play-place|play-rewards|play-hero|play-dash …) et le kit (tools/brand.py).
   Indices = numéros des mots de la phrase dans words.js ; r = [x, y, w, h] en px de la SOURCE (mesurés sur l'image).
   Les noms de médias ci-dessous sont ceux du projet d'origine : remplace-les par les tiens. */
window.WIZ_FILM = {
  slug: "wizplay", logo: "wizplay", owl: "wizplay",
  color: (((window.WIZ_BRAND || {}).modules || {}).wizplay || {}).main || "#FF5FA2",
  voAt: 0.6, endHold: 3.1, bpm: 116,
  scenes: {
    /* « WizPlay – מתמטיקה שכיף ללמוד! » : le logo se trace au mot, la phrase en géant, le hibou salue */
    s1: { kind: "brand", brandAt: 0, emph: [1], owl: { pose: "wave" } },
    /* « הסביבה שמפגישה בין תוכנית הלימודים לעולם המשחקים » : la vraie bande-annonce du jeu en sticker */
    s2: { emph: [4, 6], media: [{ name: "play-trailer", at: 0, speed: 1.2 }] },
    /* « מסע למידה מרתק על פני 4 איים » : la vraie carte ; chaque île cerclée au feutre sort à son mot (règle d'Eyal) */
    s3: { emph: [5, 6], media: [{ name: "play-map", at: 0, y: 1080,
      marks: [{ r: [1093, 130, 259, 398], at: 2, piece: { x: 900, y: 1440, w: 215, rot: -3 } },
              { r: [806, 130, 259, 398], at: 3, piece: { x: 660, y: 1440, w: 215, rot: 3 } },
              { r: [520, 130, 259, 398], at: 4, piece: { x: 420, y: 1440, w: 215, rot: -2 } },
              { r: [233, 130, 259, 398], at: 5, piece: { x: 180, y: 1440, w: 215, rot: 2 } }] }],
      "16x9": { media: [{ name: "play-map", at: 0, marks: [{ r: [1093, 130, 259, 398], at: 2, piece: true }, { r: [233, 130, 259, 398], at: 5, piece: true }] }] } },
    /* « משחקים דינמיים – מתרגלים שוב ושוב, בלי להשתעמם! » : deux vrais jeux, l'un après l'autre */
    s4: { emph: [1, 6], per: 2, media: [{ name: "play-lock", at: 0, until: 2, speed: 1.5 }, { name: "play-place", at: 2, speed: 1.6 }] },
    /* « משחוק שבונה מוטיבציה » : une vraie image dans une bulle (illustration, pas une capture : ne pas la faire passer pour l'outil) */
    s5: { emph: [2], portal: { name: "play-rewards", at: 0 }, burst: [2] },
    /* « למידה עצמאית – בניהול של המורה » : l'élève seul (bulle), puis l'onglet WizPlay du vrai tableau de l'enseignant */
    s6: { emph: [1, 4], portal: { name: "play-hero", at: 0, until: 2, fy: 600 },
      media: [{ name: "play-dash", at: 2, marks: [{ r: [128, 92, 122, 62], at: 2, piece: true }] }],
      owl: { pose: "point", at: 3, from: "right" } },
    /* « מתמטיקה שתלמידים אוהבים! » : le slogan de l'affiche, logo géant, hibou joyeux, wizdi.school, copyright */
    s7: { kind: "end", emph: [2] },
  },
};
