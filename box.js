var x = document.querySelectorAll("div");
console.log(x);
var rooms = [];
for(var i=0;i<x.length;i++)
{
  x[i].onclick = function()
  {
      this.classList.toggle('active');
      this.classList.toggle('lol');
  }
}
var y = document.getElementById("hi");
console.log(y);
y.onclick = function()
{
for(var i=0;i<x.length;i++)
  {
    if(x[i].className == 'active')
    {
      rooms.push(x[i].innerHTML);
      x[i].classList.toggle('active');
      x[i].classList.toggle('lol');
    }
  }
console.log(rooms);
rooms = [];

}
