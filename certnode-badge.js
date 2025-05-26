(function(){
  const badge = document.createElement("div");
  badge.style = "padding:1em;border:1px solid #ccc;display:inline-block;text-align:center;font-family:sans-serif;";
  badge.innerHTML = `<img src='https://www.certnode.io/certnode_seal_v1.1.png' width='100'><p style='margin-top:0.5em;font-size:0.9em;'>Certified by CertNode</p>`;
  document.currentScript.parentNode.insertBefore(badge, document.currentScript);
})();