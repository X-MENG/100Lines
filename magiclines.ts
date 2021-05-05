let background: Image = null
let w = scene.screenWidth()
let h = scene.screenHeight()
class Point {
    x: number;
    y: number;
    dx: number;
    dy: number;
    constructor() {
        this.x = randint(0, w - 1);
        this.y = randint(0, h - 1);
        this.dx = randint(-5, 5);
        this.dy = randint(-5, 5);
    }
    update() {
        let x = this.x + this.dx;
        if(x < 0) {
            this.x = 0;
            this.dx = -this.dx;
        } else if(x > w) {
            this.x = w;
            this.dx = -this.dx;
        } else {
            this.x = x;
        }
        let y = this.y + this.dy;
        if(y < 0) {
            this.y = 0;
            this.dy = -this.dy;
        } else if(y > h) {
            this.y = h;
            this.dy = -this.dy;
        } else {
            this.y = y;
        }
    }
}
let pts1 = [new Point(), new Point(), new Point(), new Point()]
let pts2 = [new Point(), new Point(), new Point(), new Point()]
let pts3 = [new Point(), new Point(), new Point(), new Point()]
let color = 1
game.onUpdateInterval(30, function () {
    color = randint(0, 15)
    for (let j = 0; j <= 3; j++) {
        pts3[j].x = pts2[j].x;
pts3[j].y = pts2[j].y;
pts3[j].dx= pts2[j].dx;
pts3[j].dy = pts2[j].dy;
pts2[j].x = pts1[j].x;
pts2[j].y = pts1[j].y;
pts2[j].dx= pts1[j].dx;
pts2[j].dy = pts1[j].dy;
pts1[j].update();
    }
})
game.onUpdate(function () {
    background = scene.backgroundImage()
    background.fill(0)
    for (let i = 0; i <= 3; i++) {
        if (i == 3) {
            background.drawLine(pts1[i].x, pts1[i].y, pts1[0].x, pts1[0].y, color)
            background.drawLine(pts2[i].x, pts2[i].y, pts2[0].x, pts2[0].y, color)
            background.drawLine(pts3[i].x, pts3[i].y, pts3[0].x, pts3[0].y, color)
        } else {
            background.drawLine(pts1[i].x, pts1[i].y, pts1[i + 1].x, pts1[i + 1].y, color)
            background.drawLine(pts2[i].x, pts2[i].y, pts2[i + 1].x, pts2[i + 1].y, color)
            background.drawLine(pts3[i].x, pts3[i].y, pts3[i + 1].x, pts3[i + 1].y, color)
        }
    }
})
