/* DragonSeek v1.2 additive live-feed experiment; COLLABORATOR_REPORTED DeepSeek concept. */
'use strict';
const USGS_V12_URL='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson';
const USGS_V12={status:'STUB',last_success:null,last_error:null,hash:null,events:[],ttl:300,url:USGS_V12_URL};
const FEED_V12=[
{id:'CMA-PUBLIC-DATA',auth:'REGISTERED_ACCOUNT',state:'NOT_CONNECTED'},
{id:'NSMC-FENGYUN',auth:'REGISTERED_ACCOUNT',state:'NOT_CONNECTED'},
{id:'MNR-OCEAN-CLOUD',auth:'REGISTERED_ACCOUNT',state:'NOT_CONNECTED'},
{id:'NASA-FIRMS',auth:'API_KEY_OR_PERMITTED_DOWNLOAD',state:'NOT_CONNECTED'},
{id:'CELESTRAK-GP',auth:'PUBLIC_CONDITIONAL',state:'NOT_CONNECTED'},
{id:'USGS-EARTHQUAKE-FEED',auth:'NO_ACCOUNT',state:'STUB'},
{id:'OPEN-METEO',auth:'TERMS_DEPENDENT',state:'MODEL_DERIVED_ONLY'}
];
function precisionV12(p){if(!p)return 'UNKNOWN';if(p.relation==='CENSORED_LEFT')return '< '+p.limit+' '+p.unit+' (below detection)';if(p.relation==='CENSORED_RIGHT')return '> '+p.limit+' '+p.unit+' (above range)';return String(p.value??'UNKNOWN')+' '+(p.unit||'')+' ± '+(p.uncertainty??'UNKNOWN')}
function receiptV12(text){return crypto.subtle.digest('SHA-256',new TextEncoder().encode(text)).then(b=>Array.from(new Uint8Array(b),n=>n.toString(16).padStart(2,'0')).join(''))}
function verifiedUSGSV12(f){const p=f&&f.properties,c=f&&f.geometry&&f.geometry.coordinates;return f&&typeof f.id==='string'&&f.geometry.type==='Point'&&p&&Number.isFinite(p.mag)&&Number.isFinite(p.time)&&Number.isFinite(p.updated)&&Array.isArray(c)&&Number.isFinite(c[0])&&Number.isFinite(c[1])&&Math.abs(c[0])<=180&&Math.abs(c[1])<=90}
function displayRealV12(){
 const host=$('usgsEventRowsV12'),layer=$('usgsOverlayV12');if(!host||!layer)return;host.replaceChildren();layer.replaceChildren();
 const inArea=USGS_V12.events.filter(e=>e.lon>=72&&e.lon<=151&&e.lat>=0&&e.lat<=56);
 for(const e of USGS_V12.events.slice(0,30)){const b=document.createElement('button');b.className='event-row';b.textContent=e.label+' · '+new Date(e.time).toISOString()+' · USGS OBSERVED';b.onclick=()=>inspectUSGSV12(e);host.appendChild(b)}
 for(const e of inArea){const b=document.createElement('button');b.className='point event seismic';b.textContent='◈';Object.assign(b.style,coarseXY(e.lon,e.lat));b.title=e.label+' · USGS OBSERVED';b.onclick=()=>inspectUSGSV12(e);layer.appendChild(b)}
 $('usgsCountV12').textContent=USGS_V12.events.length+' globally · '+inArea.length+' within map';layer.hidden=!['all','seismic'].includes(activeLayer);
}
function inspectUSGSV12(e){
 $('selection').textContent=e.label;$('selSub').textContent='USGS OBSERVED · origin '+new Date(e.time).toISOString();
 $('selClass').textContent='GENERAL_PUBLIC';$('selSource').textContent='PUBLIC_SOURCE_VERIFIED · USGS';
 $('selAccuracy').textContent=precisionV12({value:e.mag,unit:'magnitude units',uncertainty:'UNKNOWN'});
 $('selOwner').textContent='United States Geological Survey';$('selAuth').textContent='PUBLIC_OPEN_LICENSE';
 $('selJurisdiction').textContent='INTERNATIONAL · CENC preferred for mainland China';
 $('selCRS').textContent='EPSG:4326 · public natural hazard point';$('selObserved').textContent=new Date(e.time).toISOString();
 $('selProvenance').textContent='OBSERVED_USGS · sha256:'+USGS_V12.hash;
 $('selCII').textContent='NOT APPLICABLE';const a=$('usgsEventLinkV12');a.href=e.url;a.hidden=false;a.textContent='Open original USGS observation';
}
function healthV12(){
 const host=$('feedCatalogV12');if(!host)return;host.replaceChildren();
 const isFresh=USGS_V12.last_success&&Date.now()-Date.parse(USGS_V12.last_success)<USGS_V12.ttl*1000;
 const effective=USGS_V12.status==='CONNECTED_READONLY'&&!isFresh?'STALE':USGS_V12.status;
 for(const item of FEED_V12){const d=document.createElement('div');d.className='measure';const a=document.createElement('span'),b=document.createElement('strong');a.textContent=item.id+' · '+item.auth;b.textContent=item.id==='USGS-EARTHQUAKE-FEED'?effective:item.state;d.append(a,b);host.append(d)}
 $('usgsStatusV12').textContent=effective+(USGS_V12.last_success?' · '+USGS_V12.last_success:' · NOT FETCHED');
 $('usgsReceiptV12').textContent=USGS_V12.hash?'sha256:'+USGS_V12.hash:'NO LIVE RECEIPT';
}
async function fetchUSGSV12(){
 const btn=$('usgsFetchV12');btn.disabled=true;btn.textContent='Fetching...';
 const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),12000);
 try{
 const response=await fetch(USGS_V12_URL,{signal:controller.signal,cache:'no-store'});if(!response.ok)throw Error('HTTP '+response.status);
 const txt=await response.text(),data=JSON.parse(txt);if(data.type!=='FeatureCollection'||!Array.isArray(data.features))throw Error('Malformed USGS payload');
 const hash=await receiptV12(txt);
 const events=data.features.filter(verifiedUSGSV12).map(f=>({id:f.id,lon:f.geometry.coordinates[0],lat:f.geometry.coordinates[1],mag:f.properties.mag,time:f.properties.time,label:'M'+f.properties.mag+' · '+(f.properties.place||'unknown'),url:typeof f.properties.url==='string'&&f.properties.url.startsWith('https://earthquake.usgs.gov/')?f.properties.url:'https://earthquake.usgs.gov/'}));
 USGS_V12.events=events;USGS_V12.hash=hash;USGS_V12.last_success=new Date().toISOString();USGS_V12.status='CONNECTED_READONLY';USGS_V12.last_error=null;displayRealV12();
 btn.textContent='Refresh USGS';$('usgsErrorV12').textContent='Retrieved '+data.features.length+' features, accepted '+events.length+'. Rolling feed changes over time.';
 }catch(error){USGS_V12.last_error=String(error);USGS_V12.status=USGS_V12.last_success?'STALE':'ERROR';$('usgsErrorV12').textContent='Fetch failed: '+USGS_V12.last_error;btn.textContent='Retry USGS';}
 finally{clearTimeout(timer);btn.disabled=false;healthV12()}
}
function simV12(enabled,load,pv,battery,cloud,regime,roundtrip){
 let soc=battery,served=0,unserved=0;const efficiency=Math.sqrt(roundtrip),limit=battery*.25;
 for(let hour=0;hour<168;hour++){const sun=enabled?pv*Math.min(cloud,regime)*Math.max(0,Math.sin(((hour%24)-6)*Math.PI/12))*.85:0;
 const direct=Math.min(load,sun),need=load-direct,excess=Math.max(0,sun-load);
 const charge=Math.min(excess,limit,(battery-soc)/efficiency);soc+=charge*efficiency;
 const discharge=Math.min(need,limit,soc*efficiency);soc-=discharge/efficiency;
 const missing=Math.max(0,need-discharge);unserved+=missing;if(missing<1e-8)served++;
 }return {served,unserved,soc,pass:unserved<1e-7};
}
function compareV12(){
 const vals=['load','pv','battery','cloud','regimeV12','rteV12'].map(id=>Number($(id).value));const [load,pv,bat,cloud,regime,rte]=vals;
 if(!vals.every(Number.isFinite)||load<=0||pv<0||bat<0||cloud<0||cloud>1||regime<0||regime>1||rte<=0||rte>1){$('resultsV12').textContent='Invalid input';return}
 const results=[simV12(false,load,pv,bat,cloud,regime,rte),simV12(true,load,pv,bat,cloud,regime,rte)];
 const host=$('resultsV12');host.replaceChildren();
 for(const [label,key,fmt] of [['Hours fully served','served',x=>x+'/168'],['Unserved energy','unserved',x=>x.toFixed(2)+' kWh'],['End SOC','soc',x=>x.toFixed(2)+' kWh'],['Seven-day result','pass',x=>x?'PASS (synthetic)':'FAIL']]){
 const tr=document.createElement('tr');for(const item of [label,fmt(results[0][key]),fmt(results[1][key])]){const cell=document.createElement('td');cell.textContent=item;tr.append(cell)}host.append(tr)}
}
const oldDrawV12=draw;draw=function(){oldDrawV12();if(USGS_V12.last_success)displayRealV12()};
function initV12(){
 $('usgsFetchV12').addEventListener('click',fetchUSGSV12);$('runSimV12').addEventListener('click',compareV12);$('usgsEventLinkV12').hidden=true;healthV12();compareV12();setInterval(healthV12,60000);
}
initV12();
