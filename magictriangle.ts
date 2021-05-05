
class Point {
    x:number
    y:number
    constructor(x:number, y:number) {
        this.x = x
        this.y = y
    }
    mul(n:number) {
        return new Point(this.x * n, this.y * n)
    }
    add(p:Point) {
        return new Point(this.x + p.x, this.y + p.y)
    }
    sub(p:Point){
        return new Point(this.x - p.x, this.y - p.y)
    }
    normalize(){
        let s = Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2))
        return new Point(this.x / s, this.y / s)
    }
    dist(p:Point){
        return Math.sqrt(Math.pow(this.x - p.x, 2) + Math.pow(this.y - p.y, 2))
    }
}
let w = scene.screenWidth()
let h = scene.screenHeight()
let ptLst : Point[] = []
ptLst.push(new Point(45, 80))
ptLst.push(new Point(80, 20))
ptLst.push(new Point(115, 80))
let color = 1
game.onUpdate(function () {
    let background = scene.backgroundImage();
    background.fill(0)
    for(let i = 0; i < ptLst.length; ++i){
        if(i == ptLst.length - 1) {
            background.drawLine(ptLst[i].x, ptLst[i].y, ptLst[0].x, ptLst[0].y, color); 
        } else {
            background.drawLine(ptLst[i].x, ptLst[i].y, ptLst[i + 1].x, ptLst[i + 1].y, color); 
        }
    }
});

function delPoints() {
    let iter = 0
    if(ptLst.length == 3) {
        return
    }

    while(iter < ptLst.length) {
        ptLst.removeAt(iter + 1)
        ptLst.removeAt(iter + 1)
        ptLst.removeAt(iter + 1)
        ++iter
    }
}

function addPoints() {
    let iter = 0
    while(iter < ptLst.length) {
        let f:Point
        let t:Point
        if(iter == ptLst.length - 1) {
            f = ptLst[iter]
            t = ptLst[0]
        } else {
            f = ptLst[iter]
            t = ptLst[iter + 1]
        }
        let p1 = f.mul(2 / 3).add(t.mul(1 / 3))
        let p2 = f.mul(1 / 3).add(t.mul(2 / 3))
        let mid = f.mul(1 / 2).add(t.mul(1 / 2))
        ptLst.insertAt(++iter, p1)
        let dir = t.sub(f).normalize()
        let ndir = new Point(dir.y, -dir.x)
        let d = f.dist(t)
        let np = mid.add(ndir.mul(d / 3 / 2 * 1.732))
        ptLst.insertAt(++iter, np)
        ptLst.insertAt(++iter, p2)
        ++iter
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, () => {
    color = randint(0, 14)
    addPoints()
});

controller.B.onEvent(ControllerButtonEvent.Pressed, () => {
    color = randint(0, 14)
    delPoints()
});
