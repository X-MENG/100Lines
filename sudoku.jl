import Random
import Base
# using PyCall

# @pyimport pygame

function fillBoard!(m, x, y, board)
    for r in 1:3
        for c in 1:3
            board[y + r][x + c] = m[r, c]
        end
    end
end

function main()
    board = [[0 for i in 1:9] for i in 1:9]

    mid = Random.shuffle([i for i in 1:9])

    m = [mid[1:3] mid[4:6] mid[7:9]]
    
    fillBoard!(m, 3, 3, board)

    mr1 = m[1, :] 
    mr2 = m[2, :]
    mr3 = m[3, :]

    mc1 = m[:, 1] 
    mc2 = m[:, 2]
    mc3 = m[:, 3]

    ml = [mr2 mr3 mr1]'
    fillBoard!(ml, 0, 3, board)
    mr = [mr3 mr1 mr2]'
    fillBoard!(mr, 6, 3, board)

    mu = [mc2 mc3 mc1]
    fillBoard!(mu, 3, 0, board)
    md = [mc3 mc1 mc2]
    fillBoard!(md, 3, 6, board)

    mlc1 = ml[:, 1]
    mlc2 = ml[:, 2]
    mlc3 = ml[:, 3]

    mlt = [mlc2 mlc3 mlc1]
    fillBoard!(mlt, 0, 0, board)
    mlb = [mlc3 mlc1 mlc2]
    fillBoard!(mlb, 0, 6, board)

    mrc1 = mr[:, 1]
    mrc2 = mr[:, 2]
    mrc3 = mr[:, 3]

    mrt = [mrc2 mrc3 mrc1]
    fillBoard!(mrt, 6, 0, board)
    mrb = [mrc3 mrc1 mrc2]
    fillBoard!(mrb, 6, 6, board)

    for i in 1:9
        println(board[i])
    end
end

@time main()

