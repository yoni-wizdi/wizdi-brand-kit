/* MOTS DE L'ÉCRAN — VERBATIM, une clé par phrase de la narration (s1, s2, …), chaque mot avec son instant (s) dans la voix.
   En production ce fichier est GÉNÉRÉ par tools/words.py (texte validé + horodatage de la voix) : ne pas inventer d'instants.
   Champs : w = le mot tel qu'il s'affiche (copie exacte du texte validé, ponctuation comprise) ; t / e = début / fin ;
            br: true = saut de groupe voulu après ce mot ; x: true = mot douteux, INTERDIT à l'écran (il reste pour le calage).
   Exemple : textes VALIDÉS du film WizPlay du 13/10/2026 (nom du module + slogan de l'affiche), instants d'exemple sans voix. */
window.WIZ_WORDS = {
  "s1": [{ "w": "WizPlay", "t": 0.10, "e": 0.70 }],
  "s2": [{ "w": "מתמטיקה", "t": 1.05, "e": 1.45 }, { "w": "שתלמידים", "t": 1.50, "e": 1.85 }, { "w": "אוהבים!", "t": 1.90, "e": 2.20 }],
};
