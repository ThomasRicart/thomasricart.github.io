---
title: Console
---

# Ma Console


<div style="margin-bottom: 10px;">
  <button onclick="reinitialiserConsole()" 
          style="padding: 6px 12px; cursor: pointer; border-radius: 4px; border: 1px solid #999; background: #eaeaea;">
    🗑️ Effacer le code et réinitialiser
  </button>
</div>

<iframe 
  id="basthon-frame"
  src="https://console.basthon.fr/?kernel=python3" 
  width="100%" 
  height="600px" 
  style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

<script>
function reinitialiserConsole() {
  const frame = document.getElementById('basthon-frame');
  // Forcer le rechargement avec un script vide et un timestamp unique
  frame.src = 'https://console.basthon.fr/?kernel=python3&script=&t=' + Date.now();
}
</script>