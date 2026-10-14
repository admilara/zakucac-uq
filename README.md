# HE Zakučac – UQ regulacija na sučelju

Rezultati obrade zapisa s pokusa regulacije napona i jalove snage (UQ) na sučelju elektrane
HE Zakučac s prijenosnom mrežom, provedenih u sklopu pilot projekta:

- **21.02.2025.** – agregat A
- **05.03.2025.** – agregat D, uključujući paralelni rad s agregatom A

**Stranica:** <https://admilara.github.io/zakucac-uq/>

Stranica je izrađena u Jekyllu s temom [jekyll-gitbook](https://github.com/sighingnow/jekyll-gitbook)
i objavljuje se putem GitHub Pages.

## Sadržaj stranice

| Pregledna stranica | Izvor | Zapisi | Stranice zapisa | Grafovi |
| --- | --- | --- | --- | --- |
| Agregat A – Watch datoteke | Končar INEM, sustav uzbude | 53 | `watch-md-a/` | `watch-htmls-a/` |
| Agregat D – Watch datoteke | Končar INEM, sustav uzbude | 33 | `watch-md-d/` | `watch-htmls-d/` |
| Agregati A i D – PROCIS | procesne stanice agregata | 2 | `hrvoje-procis-md/` | `hrvoje-procis-htmls/` |

Pregledne stranice su postovi u `_posts/`: svaka ima tablicu zapisa s vremenom početka i kraja
te poveznice na stranice pojedinih zapisa. Stranica zapisa sadrži popis prikazanih veličina i
interaktivni Plotly graf (samostalna HTML datoteka ugrađena preko `<iframe>`).

Watch zapisi bez podataka (prazne log datoteke) nemaju vlastitu stranicu, zbog čega numeracija
u tablicama nije kontinuirana. Zapis A 029 sadrži samo pomoćne signale (Q1IN, Q2IN, ACKQ0OF,
VAUXACTP, INVERTP), njegov graf je prazan, pa nije u tablici; stranica postoji, ali je u zaglavlju
označena s `nav_exclude: true` i strelice ‹ › je preskaču.

## Struktura repozitorija

```
_config.yml              postavke stranice; record_sections povezuje mape zapisa s preglednim stranicama
index.md                 početna stranica
_posts/                  pregledne stranice (Watch A, Watch D, PROCIS)
_pages/                  O stranici, Kontakt
watch-md-a/, watch-md-d/ stranice pojedinih Watch zapisa
hrvoje-procis-md/        stranice PROCIS zapisa
watch-htmls-*/, hrvoje-procis-htmls/   Plotly grafovi
hrvoje-procis-data/      ulazni PROCIS podaci (xlsx)
ListaDogadaja.xlsx, timestamps_agregat_*.xlsx   događaji i vremenske oznake za anotacije grafova
uq_reg_*.py              skripte koje generiraju grafove i stranice zapisa
dajana-pravilnik/        P-Q dijagrami i statičke karakteristike (slike i skripte; nisu dio stranice)
_layouts/, _includes/, assets/gitbook/   lokalna kopija teme
```

Izgled stranice prilagođen je u `assets/gitbook/custom-local.css` (boje, tipografija, tablice,
okviri grafova), a ponašanje okvira grafova u `assets/gitbook/custom-local.js` (širina prema
sadržajnom dijelu, visina prema sadržaju grafa).

## Navigacija između zapisa

Stranice zapisa nisu u bočnom izborniku. U `_config.yml` stavka `record_sections` za svaku mapu
zapisa navodi preglednu stranicu kojoj pripada. Na stranici zapisa se zato:

- iznad naslova prikazuje poveznica natrag na preglednu stranicu,
- u bočnom izborniku označava pripadna pregledna stranica,
- strelicama ‹ › prelazi na prethodni ili sljedeći zapis iz iste mape (stranice s
  `nav_exclude: true` se preskaču).

Nova mapa zapisa dodaje se kao nova stavka u `record_sections`.

## Ponovno generiranje grafova

Skripte čitaju izvorne log datoteke iz mapa `Watch_snimke_A/` i `Watch_snimke_D/`, koje nisu u
ovom repozitoriju, a putanje su zadane kao apsolutne Windows putanje na vrhu svake skripte.

- `uq_reg_agregat_a_watch.py` – Watch zapisi agregata A. **Pažnja:** stranice zapisa sprema u
  `_pages/` (varijabla `output_dir`); stranica ih očekuje u `watch-md-a/`. U `_pages/` bi se
  svih 54 stranice zapisa pojavile u bočnom izborniku.
- `uq_reg_agregat_d_watch_s_anotacijama.py` – Watch zapisi agregata D, s anotacijama iz
  `ListaDogadaja.xlsx`.
- `uq_reg_procis.py` – PROCIS zapisi agregata A i D.

Predlošci u skriptama u `<head>` dodaju `plotly-latest.min.js` (zamrznut na Plotly v1.58.5), a
`pio.to_html(..., include_plotlyjs="cdn")` zatim učitava i Plotly 2.x. U objavljenim grafovima
suvišna je v1 oznaka uklonjena; ponovno generirani grafovi rade, ali učitavaju oko 3,5 MB više.

## Lokalni pregled

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000/zakucac-uq/
```

## Licenca

Tema jekyll-gitbook (`_layouts/`, `_includes/`, `assets/gitbook/`) objavljena je pod licencom
Apache 2.0, © 2019 Tao He – vidi `LICENSE`.
