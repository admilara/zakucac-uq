---
title: GEN D - Watch 006
author: admilara
date: 2025-03-24
category: UQ regulacija
layout: post
---

<span style="font-size: 20px; font-weight: bold; color: red; font-family: Helvetica; text-align: center">
    KONČAR INEM - WATCH LOG - AGREGAT D
</span>

<span style="font-size: 18px; font-weight: bold; color: red; font-family: Helvetica; text-align: center">
    Watch 006
</span>

Na grafovima niže prikazani su zapisi veličina dostavljeni od strane Končar INEM-a. 
Sve veličine su preuzete iz dostavljene log datoteke `watch-zakuca1d-zakuca1d-006.log`.
                               
Prikazane veličine su:
{% raw %}

<style scoped>
table {
  font-size: 13px;
}
</style>
| Signal | Jedinica | Opis |
|--------|----------|------|
| **VHACT** | [kV] | Napon na sučelju |
| **VHREF** | [kV] | Referenca napona na sučelju |
| **QACTH** | [Mvar] | Jalova snaga na sučelju |
| **QHREF** | [Mvar] | Referenca jalove snage na sučelju |
| **PACTH** | [MW] | Radna snaga na sučelju |
| **VGACT** | [kV] | Napon generatora |
| **VGREF** | [pu] | Referenca napona na generatoru |
| **QACT** | [Mvar] | Jalova snaga generatora |
| **IFACT** | [A] | Struja uzbude |
| **UFACT** | [V] | Napon uzbude |
| **QHINC** | [log16] | Nalog za povećanje reference Q na VN (binarni signal) |
| **QHDEC** | [log16] | Nalog za snižavanje reference Q na VN (binarni signal) |
| **VHINC** | [log16] | Nalog za povećanje reference U na VN (binarni signal) |
| **VHDEC** | [log16] | Nalog za smanjenje reference U na VN (binarni signal) |

{% endraw %}

<div class="wide-graph">
    <iframe src="{{ site.baseurl }}/watch-htmls-d/watch-zakuca1d-zakuca1d-006.html" width="100%" height="800px" frameborder="0"></iframe>
</div>
