# Florida Grand Expedition: Agent Memory & Task Tracker

## 1. Core User Constraints & Preferences
* **Shared Budget Format:** Strictly present all financial figures as a unified shared total for both travelers combined (never divide per person).
* **Accommodation Standard:** Clean, quiet, highly rated 3★ and 4★ hotels, boutique Art Deco inns, Key West historic guesthouses, and Orlando theme park partner hotels with private en-suite baths ($120–$190/night). No $600/night luxury resorts or deceptive resort fee padding.
* **Zero Alcohol:** Authentic Floridian, Cuban, Caribbean, and Southern dining with zero wine, beer, or cocktails. Feature fresh Florida orange and grapefruit juice, Cuban *cafecito* & *colada*, tropical fruit *batidos* (mango, guava, passion fruit), Key Lime sparkling mocktails, and Southern sweet iced tea.
* **Ground Logistics & Route Architecture:** Open-Jaw flight route (Inbound: EWR -> MIA; Outbound: MCO -> EWR). Compact/mid-size rental car with SunPass transponder picked up at MIA and dropped off at MCO. This saves over 7 hours of backtracking, eliminates 390 miles of highway driving, and takes advantage of near-zero intrastate Florida drop fees.
* **Measurement Units:** American units (miles, feet, °F, fluid oz) presented prominently across all metrics, waypoints, cards, and scorecard, with metric equivalents in parentheses where helpful.
* **Visual Excellence:** Every single slide must include high-resolution thematic photography, rich glassmorphism UI cards, sunset gold/ocean teal/emerald accent borders, and clean typography.
* **Mobile First:** Preserve the responsive mobile navigation drawer, native `<select>` slide pickers, and fluid flex/grid layouts.

---

## 2. Slide-by-Slide Buildout Status (30 Slides Total) - ALL COMPLETED [x]

- [x] **Slide 01:** Cover & Expedition Metrics (8-Day Grand Florida Route, Dates, 580 Miles, 4 Biomes)
- [x] **Slide 02:** Strategic Route Architecture: South-to-North Open-Jaw Flight Corridor (EWR->MIA / MCO->EWR)
- [x] **Slide 03:** Interactive Florida Cartography & GPS Command (Interactive SVG: Miami, Keys, Everglades, Orlando)
- [x] **Slide 04:** Florida Meteorology & Microclimate Navigation (Afternoon storms, humidity management, sun protection)
- [x] **Slide 05:** Highway Logistics & SunPass Toll Architecture (Overseas Highway US-1, Florida Turnpike, rental toll transponders)
- [x] **Slide 06:** Subtropical Wildlife & Wetland Safety Protocols (Alligator safety, mosquito management, coral reef protection)
- [x] **Slide 07:** Technical Packing & Theme Park Field Kit (Breathable UV gear, dry bags, park power banks, hydration)
- [x] **Slide 08:** Day 1: Inbound EWR -> MIA Arrival & Miami Cultural Gateway (Wynwood & Calle Ocho)
- [x] **Slide 09:** Night 1 Lodging: Miami Boutique Art Deco / Coral Gables Base
- [x] **Slide 10:** Night 1 Gastronomy: Authentic Cuban Ropa Vieja & Warm Pastelitos (Zero Alcohol)
- [x] **Slide 11:** Day 2: The Overseas Highway (US-1) & Key Largo Coral Reefs (John Pennekamp)
- [x] **Slide 12:** Day 2 Coast: Bahia Honda State Park & Seven Mile Bridge to Key West
- [x] **Slide 13:** Night 2 Lodging: Key West Historic Old Town Guesthouse
- [x] **Slide 14:** Day 3: Key West Historic Peninsula (Mallory Square, Fort Zachary Taylor, Hemingway Estate)
- [x] **Slide 15:** Day 3 Culinary: Authentic Key West Conch & Tart Key Lime Pie
- [x] **Slide 16:** Night 3 Lodging: Upper Keys Ocean Retreat (Marathon / Islamorada)
- [x] **Slide 17:** Day 4: Everglades National Park & Tamiami Trail (Shark Valley Tram & Sawgrass Slough)
- [x] **Slide 18:** Day 4 Transit: Florida Turnpike Northbound Transit to Orlando
- [x] **Slide 19:** Night 4 Lodging: Orlando Theme Park Base (Universal / Disney Area 3★/4★ Hotel)
- [x] **Slide 20:** Day 5: The Universal Day (1 Day at Universal Studios & Islands of Adventure)
- [x] **Slide 21:** Day 5 Tactical Protocol: Express Pass Strategy, Single Rider & Butterbeer
- [x] **Slide 22:** Night 5 Lodging: Orlando Base Continuation & Pool Recovery
- [x] **Slide 23:** Day 6: The Disney Day (1 Day at Walt Disney World Magic Kingdom)
- [x] **Slide 24:** Day 6 Tactical Protocol: Lightning Lane Strategy, Virtual Queue & Fireworks
- [x] **Slide 25:** Night 6 Lodging: Orlando Base Continuation
- [x] **Slide 26:** Day 7: Park-Free Recovery: Winter Park Scenic Canals & Disney Springs Promenade (Zero Park Tickets)
- [x] **Slide 27:** Day 7 Farewell Dinner: Central Florida Southern Smokehouse & Citrus Finale
- [x] **Slide 28:** Day 8: Orlando International (MCO) Departure Protocol & Flight Return to EWR
- [x] **Slide 29:** Master Expedition Scorecard & Shared Financial Ledger (Total Budget Breakdown for 2)
- [x] **Slide 30:** Zero-Fail Field Directory: Park Hotlines, Park-to-Park Transit & Emergency SOS

---

## 3. Implementation Verification & Audits
* **Total Slides in DOM:** 30 sequential sections with `data-slide="1"` through `data-slide="30"`.
* **Theme Palettes:** Porcelain & Slate (`linen`), Atlantic Navy (`coastal`), Obsidian & Gold (`obsidian`).
* **Interactive Cartography (Slide 3):** Full SVG Florida peninsula and Keys landmass map with 8 interactive waypoint nodes and synchronized detail card.
* **Interactive Driving Selector (Slide 5):** 4 vehicle comparison options with interactive toggle.
* **Mobile Responsiveness:** Native `<select>` pickers in header & footer, touch swipe handlers, drag-to-dismiss bottom sheet drawer.
* **Zero Alcohol:** 100% compliant across all gastronomic slides (featuring fresh citrus juices, Cuban cafecitos, mamey batidos, Butterbeer, Dole Whip, and sweet tea).
* **Shared Financials:** 100% compliant (strict shared total of $3,520 for 2 guests; zero per-person columns).
* **American Units:** 100% compliant (miles, feet, °F prominent throughout).
* **Authentic Imagery:** 22 verified high-res local images in `/images/`, zero generic broken placeholders.
