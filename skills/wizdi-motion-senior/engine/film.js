/* LE FILM — une scène par phrase de la narration (clés de words.js). Indices = numéros des mots de la phrase.
   Médias = VRAIS écrans / vraies vidéos du produit (tools/media.py add …) ; coordonnées des repères en px de la SOURCE.
   Tout champ d'une scène peut être surchargé par format : s2: { media: […], "16x9": { media: […] } }. */
window.WIZ_FILM = {
  slug: "wizplay",                 // nom du fichier de sortie + clé du logo dans assets/logos.js
  logo: "wizplay",                 // wizplay | wizplan | wizchat | wizbook | wizbox | wizspace | wizgen | wizmap
  color: (((window.WIZ_BRAND || {}).modules || {}).wizplay || {}).main || "#FF5FA2",   // couleur du module (tokens du kit)
  owl: "wizplay",                  // préfixe des séquences animées du hibou 3D (build/owl/wizplay-wave/…), sinon image fixe
  // Wizi du module, détouré, combinaison + plastron au vrai logo (copié du kit par tools/brand.py) :
  owlImgs: { wave: "assets/owls/wizplay-wave.webp", point: "assets/owls/wizplay-point.webp", joy: "assets/owls/wizplay-joy.webp" },
  // (WizBuddy : assets/owls/wizbuddy-<pose>.webp ; WizPlan n'a pas encore de poses détourées : owlImg: "assets/owl-3d.webp")
  voAt: 0,                         // la voix commence à cet instant du film (s)
  endHold: 1.05,                   // tenue de la carte de fin après le dernier mot (s) — 2,5 à 3,5 s pour un vrai film
  bpm: 116,                        // tempo visé (pop : 112–124) ; la grille réelle est recalculée sur les scènes
  scenes: {
    /* « WizPlay » : le logo officiel se trace au mot (dans un vrai film, le hibou 3D salue : owl: { pose: "wave" }) */
    s1: { kind: "brand", brandAt: 0, owl: false },   // film très court : un seul hibou, celui de la fin (sinon owl: { pose: "wave" })
    /* exemple d'une scène courante avec un VRAI écran (à décommenter quand build/media/<nom> existe) :
    s2: { emph: [2], media: [{ name: "play-map", at: 0,
          marks: [{ r: [1093, 130, 259, 398], at: 2, piece: true }] }],      // écran entier -> feutre -> le morceau sort
          owl: { pose: "point", at: 1 }, "16x9": { wordsX: 1440 } }, */
    /* « מתמטיקה שתלמידים אוהבים! » : slogan de l'affiche, carte de fin (logo, hibou joyeux, wizdi.school, copyright) */
    s2: { kind: "end", emph: [2] },
  },
};
