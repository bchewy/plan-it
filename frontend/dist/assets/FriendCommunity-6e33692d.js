import{C as F,F as N}from"./FailBackend-a1db6125.js";import{C as x}from"./CommunitySidebar-40a6d63f.js";import{N as E}from"./Navbar-faf4802b.js";import{P as B}from"./PostComponent-298e32a5.js";import{_ as T,u as D,e as b,j as S,r as _,o as n,c as l,b as f,a,F as y,f as V,d as $,l as A,p as O,h as R}from"./index-0fdca0a9.js";import{a as h}from"./axios-21b846bc.js";import{l as v}from"./index-f203fe86.js";const Y={name:"FriendCommunity",components:{NavBar:E,CreatePostComponent:F,PostComponent:B,CommunitySidebar:x,FailBackend:N},setup(){const{loginWithRedirect:o,user:r,isAuthenticated:c,isLoading:t}=D(),p={"x-api-key":`${{}.VITE_API_KEY}`},m=b([]),d=b([]),i=b(!1),u=async()=>{for(;t.value;)await new Promise(s=>setTimeout(s,100));try{const s=`${{}.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(r.value.email)}`,e=await h.get(s,{headers:p});d.value=e.data.friends;for(let g of d.value){console.log("Fetching posts for friend",g);const k=`${{}.VITE_API_ENDPOINT}/users/${encodeURIComponent(g)}/posts`,C=await h.get(k,{headers:p});m.value=[...m.value,...C.data].sort((P,w)=>new Date(w.timestamp)-new Date(P.timestamp)),i.value=!0}}catch(s){console.error("error",s),i.value=!1}};return S(u),{user:r,posts:m,friends:d,fetchData:u,IsbackendConnected:i}},computed:{async friendslist(){const o=`https://api.bchwy.com/users/${encodeURIComponent(this.user.email)}`,r={"x-api-key":`${{}.VITE_API_KEY}`};try{const c=await h.get(o,{headers:r})}catch(c){console.error("error",c),v.error(`${c.response.data.message}`,{autoClose:5e3,position:v.POSITION.TOP_CENTER})}}}},I=o=>(O("data-v-6abe518d"),o=o(),R(),o),U={class:"container-fluid pb-3 position-relative vh-100",style:{"background-color":"#cbdbb7"}},j={class:"sticky-top border-bottom",style:{"background-color":"#cbdbb7","z-index":"1"}},z=I(()=>a("div",{class:"text-center h2 mb-3 pt-4",style:{"background-color":"#cbdbb7"}},[a("span",{class:"header text-muted",style:{"font-weight":"bold"}},"Your Friends")],-1)),K={class:"row justify-content-center",style:{"background-color":"#cbdbb7"}},L={key:0},M={key:1,style:{"background-color":"#cbdbb7"}},W={key:2,class:"text-center h2 mb-3 pt-4",style:{"background-color":"#cbdbb7"}},q=I(()=>a("span",{class:"header text-muted",style:{"font-weight":"bold"}},"You have no friends yet!",-1)),G=[q];function H(o,r,c,t,p,m){const d=_("NavBar"),i=_("CommunitySidebar"),u=_("PostComponent"),s=_("FailBackend");return n(),l(y,null,[f(d),a("div",U,[a("div",j,[f(i),z]),a("div",K,[t.IsbackendConnected?(n(),l("div",L,[(n(!0),l(y,null,V(t.posts,e=>(n(),A(u,{key:e._id,username:e.username,profileImage:e.userprofile,timePosted:e.timestamp,badge:e.badge,taggedFriends:e.taggedfriends,liked:e.likes,content:e.content,postID:e._id,useremail:t.user.email},null,8,["username","profileImage","timePosted","badge","taggedFriends","liked","content","postID","useremail"]))),128))])):(n(),l("div",M,[f(s)])),t.posts.length==0&&t.IsbackendConnected?(n(),l("div",W,G)):$("",!0)])])],64)}const se=T(Y,[["render",H],["__scopeId","data-v-6abe518d"]]);export{se as default};