//获取绘制工具
	/*
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");//获取上下文
	ctx.moveTo(0,0);
	ctx.lineTo(450,450);*/
	var c=document.getElementById("canvas");
    var ctx=c.getContext("2d");
    /*ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(450,450);
    ctx.stroke();
    */
 
    var snake =[];//定义一条蛇，画蛇的身体
    var snakeCount = 6;//初始化蛇的长度
	var foodx =0;
	var foody =0;
    var togo =0;
    function drawtable()//画地图的函数
    {
 
 
    	for(var i=0;i<60;i++)//画竖线
    	{
    		ctx.strokeStyle="black";
    		ctx.beginPath();
    		ctx.moveTo(15*i,0);
    		ctx.lineTo(15*i,600);
    		ctx.closePath();
    		ctx.stroke();
    	}
        for(var j=0;j<40;j++)//画横线
    	{
    		ctx.strokeStyle="black";
    		ctx.beginPath();
    		ctx.moveTo(0,15*j);
    		ctx.lineTo(900,15*j);
    		ctx.closePath();
    		ctx.stroke();
    	}
    	
    	