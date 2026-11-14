(() => {
  const key='voxpocket-rich-r3';
  const read=()=>JSON.parse(localStorage.getItem(key)||'{}');
  addEventListener('message',e=>{
    const origin=location.protocol==='file:'?'null':location.origin;
    if(e.source!==parent||e.origin!==origin||!['ratings-read','ratings-write'].includes(e.data?.type))return;
    if(e.data.type==='ratings-write'){
      const entries=e.data.entries;
      if(!entries||typeof entries!=='object')return;
      const data=read();
      for(const [id,value] of Object.entries(entries))if(/^[ABC]-\d\d$/.test(id)&&value&&typeof value==='object')data[id]={star:!!value.star,select:!!value.select,notes:String(value.notes||''),at:value.at};
      localStorage.setItem(key,JSON.stringify(data));
    }
    parent.postMessage({type:'ratings-data',entries:read(),serial:e.data.serial},location.protocol==='file:'?'*':location.origin);
  });
})();
