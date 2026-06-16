# Building the M12864 Transistor Tester — Step-by-Step Guide

A complete, beginner-friendly walkthrough for assembling the **M12864 DIY transistor tester kit**. If
you've never soldered a through-hole kit before, don't worry — this guide explains each step, the order
to install parts, and what a good solder joint looks like.

When it's finished, this little device measures **transistors, MOSFETs, diodes, resistors, capacitors,
and inductors** all on its own, showing the results on an LCD. You just drop a component into the test
socket and press the button.

> **Time:** ~1–2 hours · **Difficulty:** beginner (basic soldering) · **Cost:** low

---

## What you need

**In the kit**

- The red **"Transistor tester"** PCB (ATMEGA328 + 8 MHz crystal)
- Resistors — ten values: 220 Ω, 680 Ω, 1.0 kΩ, 2.2 kΩ, 3.3 kΩ, 10 kΩ, 27 kΩ, 33 kΩ, 100 kΩ, 470 kΩ
- Capacitors — ceramic (marked `104` = 0.1 µF, `1nJ`, `22p`) and electrolytic (`10 µF`)
- Semiconductors — `HT7550` regulator, `TL431` voltage reference, `9012`/`9014` reference transistors
- `ATMEGA328` microcontroller (28-pin DIP) + its socket
- **ZIF test socket** (the lever-locked socket components are inserted into)
- Contrast **trimpot**, LED, pin headers
- **LCD display** module (on a 20-pin header)
- 9 V **battery clip**

**Tools you supply**

- Soldering iron (a basic one like the **Spurtar #160** shown here is fine) + solder
- Flush cutters (for trimming leads)
- Tip cleaner — brass wool or a damp sponge
- A 9 V battery for testing
- Optional: a multimeter to check your work

**The circuit:** here's the full schematic if you'd like to follow along electrically.

<img src="./assets/schematic.png" width="640" alt="Transistor tester schematic">

> 💡 **Golden rule of through-hole assembly:** install parts from **shortest to tallest**. Resistors
> lie flat, so they go first; the LCD and battery clip go last. That way the board always rests flat
> while you solder.

---

## 1. Inventory & setup

Before melting any solder, lay everything out and confirm you have all the parts. Sorting the resistors
now will save you a lot of squinting later.

<img src="./assets/01_inventory_setup/IMG_004_kit-inventory.webp" width="520" alt="Full kit laid out">

**Sort your resistors.** Resistors are labeled with colored bands, not numbers, so they're easy to mix
up. A simple trick: draw a grid on a sheet of paper, label each cell with a value, and lay each resistor
in its box as you identify it. (Use a multimeter or an online resistor color-code calculator to read
them.)

<img src="./assets/01_inventory_setup/IMG_015_resistor-sheet.webp" width="520" alt="Resistors sorted onto a labeled value chart">

**Inspect the bare board.** The **top (component) side** has white silkscreen showing where every part
goes and its value. The **bottom (solder) side** is where you'll apply the iron.

<img src="./assets/01_inventory_setup/IMG_014_pcb-bare.webp" width="300" alt="Bare PCB, component side">
<img src="./assets/01_inventory_setup/IMG_008_pcb-bottom.webp" width="300" alt="Bare PCB, solder side">

---

## 2. Get your iron ready

Good joints start with a clean, tinned tip. Let the iron come fully up to temperature, wipe the tip on
brass wool (or a damp sponge), then melt a little solder onto it until it's shiny — that's "tinning."

<img src="./assets/02_solder_tip_cleaning/IMG_022_iron-label.webp" width="300" alt="Soldering iron">
<img src="./assets/02_solder_tip_cleaning/IMG_026_iron-stand.webp" width="300" alt="Cleaning the tip in brass wool">

A clean, pointed tip transfers heat well and makes soldering much easier:

<img src="./assets/02_solder_tip_cleaning/IMG_027_iron-tip.webp" width="280" alt="Clean tinned iron tip">

---

## 3. How to solder one joint

Let's do a single joint start to finish, so the rest of the build is just repetition.

> 🆕 **New to soldering?** Read [SOLDERING.md](./SOLDERING.md) first — a short primer on technique, what
> a good joint looks like, safety, and a few free resources.

**1. Prep & insert the part.** Bend the leads to fit the footprint and push it through from the top side
so it sits flat against the board.

<img src="./assets/03_first_component/IMG_017_insert-component.webp" width="360" alt="Inserting a component">

**2. Heat both pad and lead.** Flip the board over. Touch the iron tip to the pad _and_ the lead at the
same time for a second, then feed solder into the joint (not onto the iron). It should flow in and form a
small shiny cone.

<img src="./assets/03_first_component/IMG_036_solder-joint.webp" width="360" alt="Soldering a joint from the back">

**3. Check the joint.** A good joint is smooth and shiny and shaped like a little volcano around the
lead — not a dull ball.

<img src="./assets/03_first_component/IMG_041_solder-fillet.webp" width="360" alt="Close-up of a clean solder fillet">

**4. Trim the lead.** Snip the excess lead flush with the top of the joint.

<img src="./assets/03_first_component/IMG_042_trim-leads.webp" width="360" alt="Trimming the excess lead">

> 🔁 That's the whole technique. Every part from here is: **insert → solder → trim.**

---

## 4. Install the resistors

Resistors are flat and heat-tolerant, so they go first. Work across the board, matching each resistor to
its printed value on the silkscreen. Your sorting sheet from Step 1 is your cheat sheet here.

<img src="./assets/04_populate_resistors/IMG_049_insert-resistors.webp" width="360" alt="Inserting resistors into the board">

A handy method: insert a few resistors, bend their leads slightly outward on the back to hold them, then
flip the board and solder them all at once. Repeat until every resistor position is filled.

<img src="./assets/04_populate_resistors/IMG_059_populate.webp" width="360" alt="Board with all resistors installed">

---

## 5. Install the capacitors & small parts

With the resistors in, set out the remaining parts so you can see what's left.

<img src="./assets/05_install_caps/IMG_060_kit-inventory.webp" width="520" alt="Remaining components laid out">

Now add the **ceramic capacitors** (the small disc/box parts marked `104`, `1nJ`, `22p`). These aren't
polarized, so orientation doesn't matter. The **electrolytic capacitor** (`10 µF`, the small cylinder)
**is** polarized — match its longer leg / unmarked side to the `+` on the silkscreen.

<img src="./assets/05_install_caps/IMG_064_install-caps.webp" width="360" alt="Capacitors installed on the board">

---

## 6. Install the semiconductors

Next come the slightly taller parts: the `HT7550` regulator, the `TL431` reference, the onboard
`9012`/`9014` reference transistors, and the 8 MHz crystal. **Transistors and the regulator are
polarized** — match the flat/curved side of each part to the outline printed on the board.

<img src="./assets/06_mount_transistors/IMG_070_board-back.webp" width="360" alt="Board with semiconductors installed">

Tip: viewed from the side, you can see parts now stand at different heights — that's why we go shortest
first. Push each part flush before soldering.

<img src="./assets/06_mount_transistors/IMG_067_board-side.webp" width="360" alt="Side view showing component heights">

---

## 7. Install the final components

Home stretch — the tall parts and the bits you don't want to overheat.

**IC socket.** Solder the **28-pin DIP socket** for the microcontroller (don't solder the chip directly).
Match the notch on the socket to the notch in the silkscreen outline.

<img src="./assets/07_final_components/IMG_071_ic-socket.webp" width="360" alt="IC socket soldered to the board">

**Microcontroller.** Once the socket is in, press the **ATMEGA328** into it, lining up the notches.

<img src="./assets/07_final_components/IMG_073_install-ic.webp" width="360" alt="ATMEGA328 seated in its socket">

**ZIF test socket.** This is the lever-action socket you'll drop components into for testing. Make sure
it's flat against the board before soldering.

<img src="./assets/07_final_components/IMG_075_install-zif.webp" width="360" alt="ZIF test socket installed">

**LCD module.** The display sits on a pin header. Solder the header to the board, then fit the LCD onto
it (or solder the LCD's pins directly, depending on your kit).

<img src="./assets/07_final_components/IMG_076_install-lcd.webp" width="360" alt="LCD display module and header">

<!-- TODO: add a photo of the LCD fully seated/mounted on the assembled board -->

> 📷 **TODO:** photo of the LCD mounted on the finished board.

**Battery clip.** Solder the 9 V battery clip leads last — red to `+`, black to `–` / `GND` as marked.

<img src="./assets/07_final_components/IMG_080_battery-clip.webp" width="360" alt="9V battery clip attached, board nearly complete">

---

## 8. Test your work

Before powering up, give the board a once-over: look for cold joints (dull/cracked), solder bridges
(blobs connecting two pads that shouldn't touch), and missed joints. A multimeter is handy here — check
that there's no short between the `+9V` and `GND` rails.

<img src="./assets/08_testing/IMG_082_test-meter-none.webp" width="300" alt="Checking the board with a multimeter, no reading">
<img src="./assets/08_testing/IMG_084_test-meter-pushed.webp" width="300" alt="Multimeter showing a reading during test">

---

## 9. Finished tester — see it work

Connect a 9 V battery, drop a component (try a resistor or an LED) into the ZIF socket, and press the
test button. The LCD should light up and display the measured values.

<!-- TODO: 09_final_results is empty — add the payoff shots here:
     - the finished tester powered on with the LCD lit
     - a component (e.g. a transistor) in the ZIF socket being measured
     - the LCD showing a real reading -->

> 📷 **TODO:** add photos of the completed tester powered on and measuring a real component
> (place them in `assets/09_final_results/`).

---

## Optional: a 3D-printed case

A printable enclosure for this board is included in [`../case`](../case) (OpenSCAD source). See its
[README](../case/README.md) for details.

---

## Troubleshooting

| Symptom                          | Likely cause                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------- |
| Nothing on the LCD               | Battery polarity / dead battery; adjust the contrast trimpot; LCD header not fully soldered |
| Display is blank but backlit     | Turn the contrast trimpot                                                                   |
| Garbled or wrong readings        | Cold joint or solder bridge; a resistor in the wrong position                               |
| Gets warm / battery drains fast  | Solder bridge between `+9V` and `GND` — recheck the power rails                             |
| A component reads "none" / fails | Reseat it in the ZIF socket and clamp the lever firmly                                      |

> Most problems on a kit like this come down to a single bad joint. When in doubt, reflow the suspect
> joints and recheck against the [schematic](./assets/schematic.png).
