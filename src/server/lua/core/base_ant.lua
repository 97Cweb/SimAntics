Ant = {}
Ant.__index = Ant

function Ant.new()
    local self = setmetatable({}, Ant)
    return self
end

function Ant:smell()
    print("Ant is smelling.")
end

function Ant:sight()
    print("Ant is seeing.")
end

function Ant:update()
    print("Ant is updating.")
end

return Ant
