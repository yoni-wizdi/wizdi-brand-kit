import { useRef } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
import { WIZ_WORD_PATHS } from "@/assets/logos/wizWordPaths";

gsap.registerPlugin(useGSAP, DrawSVGPlugin);

/**
 * WizWord — nom de marque d'un module (WizPlay, WizBook, …) rendu comme sur les logos :
 *   - vrais tracés Baloo (SVG généré depuis la police, comme le logo Wizdi du header)
 *   - "Wiz" en bleu classique + le suffixe dans la couleur du module (accent)
 *   - apparition = MÊME effet que le logo du header (contour qui se dessine puis
 *     remplissage), mais PLUS LENT et DÉCALÉ pour ne pas jouer en même temps que lui.
 *
 * La taille suit la taille de police du parent (height: 1em) → les classes
 * text-[...] des call-sites continuent de fonctionner.
 */

const WIZ_BLUE = "#23A4D8";

export function WizWord({
  name,
  accent = "#D6336C",
  className = "",
}: {
  name: string;
  accent?: string;
  className?: string;
}) {
  const ref = useRef<SVGSVGElement>(null);
  const data = WIZ_WORD_PATHS[name];

  useGSAP(() => {
    const svg = ref.current;
    if (!svg || !data) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const paths = svg.querySelectorAll("path");

    // Etat de depart : contour seul, invisible en remplissage.
    gsap.set(paths, { fillOpacity: 0, strokeOpacity: 1, strokeWidth: 3, drawSVG: "0%" });

    const io = new IntersectionObserver(
      ([e]) => {
        if (!e.isIntersecting) return;
        io.disconnect();
        // Meme timeline que LogoLockup, ralentie (~2x) + delai pour ne pas
        // demarrer en meme temps que l'animation du logo du header.
        gsap
          .timeline({ delay: 1.1 })
          .to(paths, { drawSVG: "100%", duration: 2.4, ease: "power2.inOut" })
          .to(paths, { fillOpacity: 1, duration: 1, ease: "power2.out" }, "-=0.5")
          .to(paths, { strokeOpacity: 0, duration: 0.7, ease: "power2.out" }, "-=0.6");
      },
      { threshold: 0.35 }
    );
    io.observe(svg);
    return () => io.disconnect();
  }, [name]);

  // Nom inconnu (securite) : fallback texte simple bicolore.
  if (!data) {
    const suffix = name.replace(/^Wiz/i, "");
    return (
      <span dir="ltr" className={"wizword " + className} style={{ fontFamily: '"Baloo Latin", sans-serif', fontWeight: 700 }}>
        <span style={{ color: WIZ_BLUE }}>Wiz</span>
        <span style={{ color: accent }}>{suffix}</span>
      </span>
    );
  }

  return (
    <svg
      ref={ref}
      viewBox={data.vb}
      role="img"
      aria-label={name}
      preserveAspectRatio="xMidYMid meet"
      /* PAS de display force ici : ecraserait le `hidden`/`sm:block` des call-sites
         (bug topbar mobile). Le SVG est inline par defaut, ce qui suffit. */
      className={"wizword " + className}
      style={{ height: "1.05em", width: "auto", verticalAlign: "-0.22em" }}
    >
      {/* SSR / no-JS / reduced-motion : rempli et net par defaut */}
      <path d={data.wiz} fill={WIZ_BLUE} stroke={WIZ_BLUE} strokeOpacity="0" vectorEffect="non-scaling-stroke" />
      <path d={data.suffix} fill={accent} stroke={accent} strokeOpacity="0" vectorEffect="non-scaling-stroke" />
    </svg>
  );
}
