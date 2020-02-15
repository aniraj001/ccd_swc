       var r = document.getElementById("room-numbers").innerHTML;
       document.getElementById("room-numbers").style.display = "none";
       var lr = r.split(" ");
       var z = document.querySelectorAll(".lol");
       for(var j=0;j<lr.length;j++){
         var p = lr[j];
         for(var i=0;i<z.length;i++){
              if(z[i].innerHTML == p)
                z[i].classList.toggle("occupied");
         }
       }
       var sub = [];
       var mx = 0;
       var ff = document.getElementById("man");
       var a5;
       var div = document.getElementById('div'), x1 = 0, y1 = 0, x2 = 0, y2 = 0;
       function reCalc(){
           var x3 = Math.min(x1,x2);
           var x4 = Math.max(x1,x2);
           var y3 = Math.min(y1,y2);
           var y4 = Math.max(y1,y2);
           div.style.left = x3 + 'px';
           div.style.top = y3 + 'px';
           div.style.width = x4 - x3 + 'px';
           div.style.height = y4 - y3 + 'px';
       }
       var aa = 0;
       ff.onmousedown = function(e){
           a5 = 1;
           div.hidden = 0;
           x1 = e.clientX;
           y1 = e.clientY;
           reCalc();
           aa = 1;
       };
       var a1;
       ff.onmousemove = function(e){
           if(aa != 1) return;
           div.style.borderWidth = "1px";
           x2 = e.clientX;
           y2 = e.clientY;
           reCalc();
           var rect1 = div.getBoundingClientRect();
           for(var i=0;i<x.length;i++)
           {
             if(a5 == 1){
                   var rect2 = x[i].getBoundingClientRect();
                   var overlap = !(rect1.right < rect2.left || rect1.left > rect2.right || rect1.bottom < rect2.top || rect1.top > rect2.bottom)

                   if(overlap == 1){
                       if(!sub.includes(x[i].innerHTML)){
                         x[i].classList.add('active');
                         x[i].classList.remove('lol');
                       }
                       else {
                         x[i].classList.add('lol');
                         x[i].classList.remove('active');
                       }
                   }
                   if(overlap == 0){
                     if(!sub.includes(x[i].innerHTML)){
                       x[i].classList.add('lol');
                       x[i].classList.remove('active');
                     }
                     else {
                       x[i].classList.add('active');
                       x[i].classList.remove('lol');
                     }
                   }
             }
           }
       };
       onmouseup = function(e){
         aa=0;
         div.style.borderWidth = "0px";
         a5 = 0;
       };

         var x = document.querySelectorAll(".lol");
         var rooms = [];
         var y = document.getElementById("hi");
         console.log(y);
         var lop = "";
         y.onclick = function(){
            rooms = [];
            for(var i=0;i<x.length;i++)
            {
               if(x[i].className == 'active'){
                   rooms.push(x[i].innerHTML);
                   sub.push(x[i].innerHTML);
               }
               else{
                 if(sub.includes(x[i].innerHTML))
                 {
                   for(var j = sub.length - 1; j >= 0; j--) {
                     if(sub[j] == x[i].innerHTML) {
                       sub.splice(j, 1);
                     }
                   }
                 }
               }
            }
           console.log(rooms);
           console.log(sub);
         }
