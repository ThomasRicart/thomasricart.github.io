# 🐍 RD02 : Algèbre de Boole


---

## 📂 Ressources du Chapitre

Accédez ici à l'ensemble des documents de cours et aux outils de révision interactive.

| Support | Description | Corrections |
| :--- | :--- | :--- |
| [📕 **Cours**](./RD02_Algebre_Boole.pdf) | Le support de cours complet en version PDF. | |
| [💡 **Synthèse**](./RD02_Algebre_Boole-synth.pdf) | Fiche récapitulative des concepts clés (HTML). | |
| [✏️ **Exercices 01**](https://raisintine.fr/chocolatine/question.php?idc=29) | Exercices autocorrigés / Généralités| |
| [✏️ **Exercices 02**](https://raisintine.fr/chocolatine/question.php?idc=30) | Exercices autocorrigés / Opérateurs | |
| [✏️ **Exercices 03**](https://raisintine.fr/chocolatine/question.php?idc=31) | Exercices autocorrigés / Avec Python | |
| [📚 **Activité pratique**]() | Activité Capytale | [Correction]()|

---
---

<div style="width: 100%; height: 330px">
  <logic-editor id="nyv9Qa" mode="tryout">
    <script type="application/json5">
      { // JSON5
        v: 8,
        opts: {origin: [0, -43]},
        components: {
          in0: {type: 'in', pos: [100, 245], id: 0},
          and0: {type: 'and', pos: [365, 275], in: [1, 2], out: 3},
          in1: {type: 'in', pos: [105, 300], id: 4},
          in2: {type: 'in', pos: [20, 30], id: 5},
          out0: {type: 'out', pos: [505, 275], id: 6},
        },
        wires: [[0, 1], [4, 2], [3, 6]]
      }
    </script>
  </logic-editor>
</div>

<iframe style="width: 100%; height: 330px; border: 0" src="https://logic.modulo-info.ch/?id=nyv9Qa&mode=tryout&data=N4NwXAHANA9gDgFwM5mDATgSwOaYHZgDaADFALQAsAzALoC+UAxjALZwx4Cmeyq+xqBAE84nMAHJ84qOxSEAjMVIAmCgFYaUTABMwxBgEM82gcGGiJR7dNlEqANjVRlAdg1aCC55pgBXBGBUDPjygiJikng2MHKKTlRKmjpgFMF4ymEWkdFyyqQJSbpqDH4IpuYRpTlEasROru7J9nQMAO6Y6JxyJFDymoQU3lCEVFD2NPRAA"></iframe>

https://logic.modulo-info.ch/?id=nyv9Qa&mode=tryout&data=N4NwXAHANA9gDgFwM5mDATgSwOaYHZgDaADFALQAsAzALoC+UAxjALZwx4Cmeyq+xqBAE84nMAHJ84qOxSEAjMVIAmCgFYaUTABMwxBgEM82gcGGiJR7dNlEqANjVRlAdg1aCC55pgBXBGBUDPjygiJikng2MHKKTlRKmjpgFMF4ymEWkdFyyqQJSbpqDH4IpuYRpTlEasROru7J9nQMAO6Y6JxyJFDymoQU3lCEVFD2NPRAA

```{logic}
:id: nyv9Qa
:height: 330
:mode: tryout

{ // JSON5
  v: 8,
  opts: {origin: [0, -43]},
  components: {
    in0: {type: 'in', pos: [100, 245], id: 0},
    and0: {type: 'and', pos: [365, 275], in: [1, 2], out: 3},
    in1: {type: 'in', pos: [105, 300], id: 4},
    in2: {type: 'in', pos: [20, 30], id: 5},
    out0: {type: 'out', pos: [505, 275], id: 6},
  },
  wires: [[0, 1], [4, 2], [3, 6]]
}
```

### 🧩 Concepts illustrés
```python
```