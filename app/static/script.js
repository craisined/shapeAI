var c = document.getElementById("canvas");
var ctx = c.getContext("2d");

var aiBox = document.getElementById("shapeBox");

var isDragging = false;

function draw(e){
    var canvas_width = 0.4 * document.documentElement.clientWidth;
    if (document.documentElement.clientWidth <= 1000){
        canvas_width = 0.8 * document.documentElement.clientWidth;
    }
    var rect = canvas.getBoundingClientRect();

    if (e.type.includes(`touch`)) {
        const { touches, changedTouches } = e.originalEvent ?? e;
        const touch = touches[0] ?? changedTouches[0];
        var posx = (touch.pageX - rect.left) * 64 / canvas_width;
        var posy = (touch.pageY - rect.top) * 64 / canvas_width;
    } else if (e.type.includes(`mouse`)) {
        var posx = (e.clientX - rect.left) * 64 / canvas_width;
        var posy = (e.clientY - rect.top) * 64 / canvas_width;
    }
    if (isDragging){
        ctx.fillStyle = "#000000";
        ctx.beginPath()
        ctx.arc(posx, posy, 1, 0, 2*Math.PI);
        ctx.fill();
    }
}

function clear_canvas(){
    ctx.fillStyle = "#FFFFFF";
    ctx.beginPath();
    ctx.fillRect(0, 0, 64, 64);
    ctx.fill();
}

function send_image(){
    var img = c.toDataURL();
    const params = new URLSearchParams();
    params.append("img", img);
    fetch(`/shape_model?${params}`).then(
        function (r) {return r.text();}
    ).then(
        function (r) {aiBox.innerHTML = r;}
    );
}

clear_canvas();
setInterval(send_image, 1000);
c.addEventListener("mousemove", draw);
c.addEventListener('touchmove', draw);
c.addEventListener('mousedown', function(e){isDragging = true;});
c.addEventListener('touchstart', function(e){isDragging = true;});
c.addEventListener('mouseup', function(e){isDragging = false;});
c.addEventListener('touchend', function(e){isDragging = false;});