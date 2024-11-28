# Prebiotic Metabolism
Attempting to use molecular dynamics to form oxaloacetate from pyruvate, or the PEP derivate, as an attempt to expand the rTCA cycle.


# To-do
Temperatures to consider:
- Temp of deep sea water (276 K)
- Room temp (293K)
- Around hydrothermal temp (353K)

## xTB
Do all calculations (except Geom opt and MD) in triplicates to add variability measurement.

  - Molecular Dynamics
    - [ ] Pyruvic acid + Base (yet to decide on base)

**Calculations with metal center (as an aqua (H2O) complex) and neutral surface**. For this one, need to do some research into the coordinate numbers of the metal centers, as well as their most stable oxidation states in water?

At 276 K:

| Calculation                              | No complex | Fe(0) complex | Fe (III) complex | Fe fixed surface | Co(0) complex | Co(III) complex | Co fixed surface | Ni(0) complex | Ni(II) complex | Ni fixed surface | Pb(0) complex | Pb(II) complex | Pb fixed surface |
| ---------------------------------------- | ---------- | ------------- | ---------------- | ---------------- | ------------- | --------------- | ---------------- | ------------- | -------------- | ---------------- | ------------- | -------------- | ---------------- |
| Geom opt with Pyruvate + $CO_2$          | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with PEP + $CO_2$               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate + $PO_3^{2-}$ | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Pyruvate + $CO_2$              | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with PEP + $CO_2$                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate + $PO_3^{2-}$     | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Pyruvate + $CO_2$                | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Oxaloacetate + $PO_3^{2-}$       | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |

At 293 K:

| Calculation                              | No complex | Fe(0) complex | Fe (III) complex | Fe fixed surface | Co(0) complex | Co(III) complex | Co fixed surface | Ni(0) complex | Ni(II) complex | Ni fixed surface | Pb(0) complex | Pb(II) complex | Pb fixed surface |
| ---------------------------------------- | ---------- | ------------- | ---------------- | ---------------- | ------------- | --------------- | ---------------- | ------------- | -------------- | ---------------- | ------------- | -------------- | ---------------- |
| Geom opt with Pyruvate + $CO_2$          | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with PEP + $CO_2$               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate + $PO_3^{2-}$ | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Pyruvate + $CO_2$              | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with PEP + $CO_2$                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate + $PO_3^{2-}$     | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Pyruvate + $CO_2$                | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Oxaloacetate + $PO_3^{2-}$       | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |

At 353 K:

| Calculation                              | No complex | Fe(0) complex | Fe (III) complex | Fe fixed surface | Co(0) complex | Co(III) complex | Co fixed surface | Ni(0) complex | Ni(II) complex | Ni fixed surface | Pb(0) complex | Pb(II) complex | Pb fixed surface |
| ---------------------------------------- | ---------- | ------------- | ---------------- | ---------------- | ------------- | --------------- | ---------------- | ------------- | -------------- | ---------------- | ------------- | -------------- | ---------------- |
| Geom opt with Pyruvate + $CO_2$          | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with PEP + $CO_2$               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate               | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| Geom opt with Oxaloacetate + $PO_3^{2-}$ | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Pyruvate + $CO_2$              | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with PEP + $CO_2$                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate                   | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| GFN2 with Oxaloacetate + $PO_3^{2-}$     | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Pyruvate + $CO_2$                | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
| MD with Oxaloacetate + $PO_3^{2-}$       | [ ]        | [ ]           | [ ]              | [ ]              | [ ]           | [ ]             | [ ]              | [ ]           | [ ]            | [ ]              | [ ]           | [ ]            | [ ]              |
