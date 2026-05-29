// reading-progress.js - 阅读进度条 + 上次位置持久化 (2026-05-29 v2)
(function(){
  if(typeof window==='undefined')return;
  var KEY='gaoshu_reading_pos';
  function pageId(){
    return location.pathname.split('/').pop().replace('.html','')||'index';
  }
  function loadAll(){try{return JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){return{};}}
  function saveAll(o){try{localStorage.setItem(KEY,JSON.stringify(o));}catch(e){}}

  // 顶部进度条
  function ensureBar(){
    if(document.getElementById('reading-progress-bar'))return;
    var b=document.createElement('div');
    b.id='reading-progress-bar';
    document.body.appendChild(b);
  }
  function updateBar(){
    var bar=document.getElementById('reading-progress-bar');
    if(!bar)return;
    var doc=document.documentElement;
    var h=doc.scrollHeight-doc.clientHeight;
    if(h<=0){bar.style.width='0';return;}
    var pct=Math.min(100, Math.max(0, (window.scrollY/h)*100));
    bar.style.width=pct.toFixed(1)+'%';
  }

  // 滚动位置持久化 (节流 500ms)
  var saveTimer=null;
  function scheduleSave(){
    if(saveTimer)return;
    saveTimer=setTimeout(function(){
      var doc=document.documentElement;
      var h=doc.scrollHeight-doc.clientHeight;
      var pct=h>0?(window.scrollY/h)*100:0;
      var all=loadAll();
      all[pageId()]={pct:pct,scrollY:window.scrollY,ts:Date.now()};
      saveAll(all);
      saveTimer=null;
    }, 500);
  }

  // 恢复 toast
  function showToast(){
    var all=loadAll();
    var rec=all[pageId()];
    if(!rec||rec.pct<3)return; // 进度 <3% 不提示
    var toast=document.createElement('div');
    toast.id='last-pos-toast';
    var d=new Date(rec.ts);
    var ago=Math.round((Date.now()-rec.ts)/60000);
    var agoTxt=ago<1?'刚刚':ago<60?ago+' 分钟前':ago<1440?Math.round(ago/60)+' 小时前':Math.round(ago/1440)+' 天前';
    toast.innerHTML='📖 上次读到 <strong>'+rec.pct.toFixed(0)+'%</strong> ('+agoTxt+') · 点击回到 →';
    toast.style.display='block';
    toast.onclick=function(){
      window.scrollTo({top:rec.scrollY,behavior:'smooth'});
      toast.remove();
    };
    document.body.appendChild(toast);
    setTimeout(function(){if(toast.parentNode)toast.style.opacity='0.6';}, 8000);
    setTimeout(function(){if(toast.parentNode)toast.remove();}, 15000);
  }

  function init(){
    ensureBar();
    updateBar();
    showToast();
    window.addEventListener('scroll', function(){
      updateBar();
      scheduleSave();
    }, {passive:true});
    window.addEventListener('resize', updateBar);
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
