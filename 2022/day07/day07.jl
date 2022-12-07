mutable struct File
    name::String
    size::Int
end

mutable struct Dir
    name::String
    files::Vector{File}
    dirs::Vector{Dir}
    parent::Union{Nothing, Dir}
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

function parseInput()
    pwd = Dir("/", File[], Dir[], nothing, 0)
    for line in eachline("input.txt")
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


total::Int = 0
function part1(dir::Dir)
    global total
    for d in dir.dirs
        part1(d)
        dir.size += d.size
    end
    for f in dir.files
        dir.size += f.size
    end
    if (dir.size <= 100000)
        total += dir.size
    end
end

min_space::Int = typemax(Int)
const needed_space = 3636666

function part2(dir::Dir)
    global min_space
    for d in dir.dirs
        part2(d)
        dir.size += d.size
    end
    for f in dir.files
        dir.size += f.size
    end
    if (dir.size >= needed_space)
        min_space = min(min_space, dir.size)
    end
end

root = parseInput()
part1(root)
println(total)

root = parseInput()
part2(root)
println(min_space)
