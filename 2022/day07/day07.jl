module Day07

mutable struct File
    name::String
    size::Int
end

mutable struct Dir
    name::String
    files::Vector{File}
    dirs::Vector{Dir}
    parent::Union{Nothing,Dir}
    size::Int
end

function addDir(dir::Dir, name)
    for d in dir.dirs
        if d.name == name
            return d
        end
    end
    newDir = Dir(name, File[], Dir[], dir, 0)
    push!(dir.dirs, newDir)
    return newDir
end

function addFile(dir::Dir, name, size::Int)
    for f in dir.files
        if f.name == name
            return f
        end
    end
    newFile = File(name, size)
    push!(dir.files, newFile)
    return newFile
end

function getRoot(dir::Dir)
    if dir.parent === nothing
        return dir
    end
    return getRoot(dir.parent)
end

function parseInput(input)
    pwd = Dir("/", File[], Dir[], nothing, 0)
    for line in eachline(input)
        if startswith(line, "\$")
            if contains(line, "ls")
                continue
            end
            dir = last(split(line, " "))
            if dir == ".."
                pwd = pwd.parent
            else
                pwd = addDir(pwd, dir)
            end
        else
            info = split(line, " ")
            if (info[1] == "dir")
                addDir(pwd, info[2])
            else
                addFile(pwd, info[2], parse(Int, info[1]))
            end
        end
    end
    return getRoot(pwd)
end

function part1(input="input.txt")
    global total = 0
    function part1Rec(dir::Dir)
        for d in dir.dirs
            part1Rec(d)
            dir.size += d.size
        end
        for f in dir.files
            dir.size += f.size
        end
        if (dir.size <= 100000)
            total += dir.size
        end
    end

    root = parseInput(input)
    part1Rec(root)
    return total
end

const needed_space = 3636666
function part2(input="input.txt")
    global min_space = typemax(Int)

    function part2Rec(dir::Dir)
        for d in dir.dirs
            part2Rec(d)
            dir.size += d.size
        end
        for f in dir.files
            dir.size += f.size
        end
        if (dir.size >= needed_space)
            min_space = min(min_space, dir.size)
        end
    end

    root = parseInput(input)
    part2Rec(root)
    return min_space
end

end
