function CreateOrthoMatrix (w: number, h: number, n: number, f: number) {
    let t = new Matrix4x4()
    t.SetMatrix([
        [2 / w, 0, 0, 0],
        [0, 2 / h, 0, 0],
        [0, 1, 1 / (f - n), -n / (f - n)],
        [0, 0, 0, 1]
    ])
    return t
}
let background: Image = null
class Vec3 {
    x : number
    y : number
    z : number
    constructor(x : number, y : number, z : number) {
        this.x = x
        this.y = y
        this.z = z
    }
    Add(rhs : Vec3) : Vec3 {
        let x = this.x + rhs.x
        let y = this.y + rhs.y
        let z = this.z + rhs.z
        return new Vec3(x, y, z)
    }
    Sub(rhs : Vec3) : Vec3{
        let x2 = this.x - rhs.x
        let y2 = this.y - rhs.y
        let z2 = this.z - rhs.z
        return new Vec3(x2, y2, z2)
    }
    Length() : number {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2) + Math.pow(this.z, 2))
    }
    Normalize() {
        let s = this.Length()
        if(s != 0) {
            this.x = this.x / s
            this.y = this.y / s
            this.z = this.z / s
        }
    }
    Dot(v : Vec3) : number {
        return this.x * v.x + this.y * v.y + this.z * v.z
    }
    Cross(v : Vec3) : Vec3 {
        let x3 = this.z * v.y - this.y * v.z
        let y3 = this.x * v.z - this.z * v.x
        let z3 = this.y * v.x - this.x * v.y
        return new Vec3(x3, y3, z3)
    }
    ToVec4(w : number) {
        return new Vec4(this.x, this.y, this.z, w)
    }
}
class Vec4 {
    x : number
    y : number
    z : number
    w : number
    constructor(x : number, y : number, z : number, w : number) {
        this.x = x
        this.y = y
        this.z = z
        this.w = w
    }
    ToVec3() : Vec3 {
        return new Vec3(this.x, this.y, this.z)
    }
    Add(rhs : Vec4) : Vec4 {
        let x4 = this.x + rhs.x
        let y4 = this.y + rhs.y
        let z4 = this.z + rhs.z
        let w = this.w + rhs.w
        return new Vec4(x4, y4, z4, w)
    }
    Mul(n : number) : Vec4 {
        let x5 = this.x * n
        let y5 = this.y * n
        let z5 = this.z * n
        let a = this.w * n
        return new Vec4(x5, y5, z5, a)
    }
    Div(n : number) : Vec4 {
        let x6 = this.x / n
        let y6 = this.y / n
        let z6 = this.z / n
        let b = this.w / n
        return new Vec4(x6, y6, z6, b)
    }
}
class Matrix4x4 {
    rows : number
    cols : number
    m    : number[][]
    constructor() {
        this.rows = this.cols = 4
        this.m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    }
    SetMatrix(m : number[][]) {
        this.m = m
    }

    GetCol(index : number) : Vec4 {
        let result : number[] = []
        for(let i = 0; i < this.rows; ++i) {
            result.push(this.m[index][i])
        }
        return new Vec4(result[0], result[1], result[2], result[3])
    }

    MulVec4(v : Vec4) : Vec4 {
        let vx = this.GetCol(0).Mul(v.x)
        let vy = this.GetCol(1).Mul(v.y)
        let vz = this.GetCol(2).Mul(v.z)
        return vx.Add(vy.Add(vz))
    }
}
class Cube {
    pos : Vec3
    size : number
    vertices : Vec3[]
    edges : number[][]
    faceType : string[]
    faceToEdges : {[key : string] : Vec3[]}
    faceToVertices : {[key : string] : number[]}
    constructor(pos : Vec3, size : number) {
        this.pos = pos
        this.size = size
        let hs = size / 2
        let p = pos
        this.vertices = []
        this.vertices.push(new Vec3(p.x - hs, p.y - hs, p.z - hs))
        this.vertices.push(new Vec3(p.x - hs, p.y - hs, p.z + hs))
        this.vertices.push(new Vec3(p.x + hs, p.y - hs, p.z + hs))
        this.vertices.push(new Vec3(p.x + hs, p.y - hs, p.z - hs))
        this.vertices.push(new Vec3(p.x - hs, p.y + hs, p.z - hs))
        this.vertices.push(new Vec3(p.x - hs, p.y + hs, p.z + hs))
        this.vertices.push(new Vec3(p.x + hs, p.y + hs, p.z + hs))
        this.vertices.push(new Vec3(p.x + hs, p.y + hs, p.z - hs))
        this.edges = []
        this.edges.push([0, 1])
        this.edges.push([1, 2])
        this.edges.push([2, 3])
        this.edges.push([3, 0])
        this.edges.push([4, 5])
        this.edges.push([5, 6])
        this.edges.push([6, 7])
        this.edges.push([7, 4])
        this.edges.push([0, 4])
        this.edges.push([1, 5])
        this.edges.push([2, 6])
        this.edges.push([3, 7])

        this.UpdateLocalAxis()

        this.faceType = ["up", "down", "left", "right", "front", "back"]
        this.faceToEdges = {}
        this.faceToVertices = {}
        this.faceToVertices["up"] = [4, 5, 6, 7]
        this.faceToVertices["down"] = [0, 1, 2, 3]
        this.faceToVertices["left"] = [0, 3, 7, 4]
        this.faceToVertices["right"] = [1, 2, 6, 5]
        this.faceToVertices["front"] = [2, 3, 7, 6]
        this.faceToVertices["back"] = [0, 1, 5, 4]
    }
    GetFaceDir(a_idx : number, o_idx : number, b_idx : number) : Vec3 {
        let c = this.vertices[a_idx].Sub(this.vertices[o_idx])
        let d = this.vertices[b_idx].Sub(this.vertices[o_idx])
        let e = c.Cross(d)
        e.Normalize()
        return e
    }
    local_x_axis : Vec3
    local_y_axis : Vec3
    local_z_axis : Vec3
    UpdateLocalAxis() {
        this.local_x_axis = this.GetFaceDir(5, 1, 2)
        this.local_y_axis = this.GetFaceDir(4, 5, 6)
        this.local_z_axis = this.GetFaceDir(2, 3, 7)
    }
    SetFaceVectors(face : string, a_idx : number, o_idx : number, b_idx : number) {
        let f = this.vertices[a_idx].Sub(this.vertices[o_idx])
        f.Normalize()
        let g = this.vertices[b_idx].Sub(this.vertices[o_idx])
        g.Normalize()
        this.faceToEdges[face] = [f, g]

    }
    UpdateFaceVectors() {
        this.SetFaceVectors("up", 7, 4, 5)
        this.SetFaceVectors("down", 1, 0, 3)
        this.SetFaceVectors("left", 3, 0, 4)
        this.SetFaceVectors("right", 5, 1, 2)
        this.SetFaceVectors("front", 2, 3, 7)
        this.SetFaceVectors("back", 4, 0, 1)
    }
    GetVertices() : Vec3[] {
        return this.vertices
    }
    GetLocalVertices() : Vec3[] {
        let local_vertices : Vec3[] = []
        for(let j = 0; j < this.vertices.length; ++j){
            local_vertices.push(this.vertices[j].Sub(this.pos))
        }
        return local_vertices
    }
    UpdateVertices(new_vertices : Vec3[]) {
        for(let k = 0; k < this.vertices.length; ++k) {
            this.vertices[k] = new_vertices[k]
        }
        this.UpdateFaceVectors()
    }
    WhichFacesBelongTo(v_idx : number) : string[] {
        let faces : string[] = []
        for(let l = 0; l < this.faceType.length; ++l) {
            let key = this.faceType[l]
            if(this.faceToVertices[key].indexOf(v_idx) >= 0) {
                faces.push(key)
            }
        }
        return faces
    }
    GetFaceNormal(face : string) : Vec3{
        let edges = this.faceToEdges[face]
        return edges[0].Cross(edges[1])
    }

    Render(g : Image) {
        let vec = this.GetVertices()
        let local_vec = this.GetLocalVertices()
        let vertices : Vec4[] = []
        let new_vertices : Vec3[] = []
        for(let m = 0; m < local_vec.length; ++m) {
            let v = local_vec[m].ToVec4(1)
            v = rot_x.MulVec4(v)
            v = rot_y.MulVec4(v)
            v = rot_z.MulVec4(v)
            let wv = this.pos.Add(v.ToVec3())
            new_vertices.push(wv)
            v = wv.ToVec4(1)
            let h = om.MulVec4(v)
            h = h.Div(h.w)
            vertices.push(h)
        }

        this.UpdateVertices(new_vertices)
        let forward = new Vec3(0, 0, 1)

        for(let n = 0; n < this.edges.length; ++n) {
            let isEdgeVisible = true
            let curEdge = this.edges[n]
            for(let o = 0; o < curEdge.length; ++o) {
                let edgeVertexIndex = curEdge[o]
                let faces2 = this.WhichFacesBelongTo(edgeVertexIndex)
                let isVisible = false
                for(let q = 0; q < faces2.length; ++q) {
                    let r = faces2[q]
                    let fn = this.GetFaceNormal(r)
                    if(fn.Dot(forward) < 0) {
                        isVisible = true
                        break
                    }
                }
                if(isVisible == false) {
                    isEdgeVisible = false
                    break
                }
            }
            if(isEdgeVisible == true) {
                let fx = 80 + this.vertices[curEdge[0]].x * 5
                let fy = 60 + this.vertices[curEdge[0]].y * 5
                let tx = 80 + this.vertices[curEdge[1]].x * 5
                let ty = 60 + this.vertices[curEdge[1]].y * 5
                g.drawLine(fx, fy, tx, ty, randint(1,14))
            }
        }
    }
}
function ToLeft(a : Vec3, b : Vec3, p : Vec3) : boolean {
    return  a.x * b.y + b.x * p.y + p.x * a.y - a.y * b.x - b.y * p.x - p.y * a.x > 0.0;
}
function InSqTest(a : Vec3, b : Vec3, c : Vec3, d : Vec3, p : Vec3) : boolean {
    return ToLeft(a, b, p) && ToLeft(b, c, p) && ToLeft(b, d, p) && ToLeft(d, a, p) 
}
let cube = new Cube(new Vec3(0, 0, 20), 10)
let om = CreateOrthoMatrix(-10, 10, 0.1, 100)
let spd = 1
let D2R = Math.PI / 180
let rot_x = new Matrix4x4()
rot_x.SetMatrix([
    [1, 0, 0, 0],
    [0, Math.cos(spd * D2R), -Math.sin(spd * D2R), 0],
    [0, Math.sin(spd * D2R), Math.cos(spd * D2R), 0],
    [0, 0, 0, 1]
])
let rot_y = new Matrix4x4()
rot_y.SetMatrix([
    [Math.cos(spd * D2R), 0, Math.sin(spd * D2R), 0],
    [0, 1, 0, 0],
    [-Math.sin(spd * D2R), 0, Math.cos(spd * D2R), 0],
    [0, 0, 0, 1]
])
let rot_z = new Matrix4x4()
rot_z.SetMatrix([
    [Math.cos(spd * D2R), -Math.sin(spd * D2R), 0, 0],
    [Math.sin(spd * D2R), Math.cos(spd * D2R), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
game.onUpdateInterval(20, function () {
    background = scene.backgroundImage()
    background.fill(0)
    cube.Render(background)
})
