function draw() {
	var canvas = document.getElementById('canvas');
	var ctx = canvas.getContext('2d');
	ctx.fillRect(0, 0, canvas.width, canvas.height);
}

var sidebarState = 0;

var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
ctx.canvas.width = window.innerWidth - 400;
ctx.canvas.height = window.innerHeight - 300;

draw()

$('#canvas').on('switchSidebar', function () {
	var canvas = document.getElementById('canvas');
	var ctx = canvas.getContext('2d');
	if(sidebarState == 0)
	{
		ctx.canvas.width = window.innerWidth - 200;
		sidebarState = 1;
	}
	else
	{
		ctx.canvas.width = window.innerWidth - 400;
		sidebarState = 0;
	}
	draw();
});
