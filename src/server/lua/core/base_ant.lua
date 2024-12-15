Base_Ant = {}

-- Define methods for Base_Ant
function Base_Ant.new()
    local self = setmetatable({}, { __index = Base_Ant })
    return self
end

function Base_Ant.extend()
    local child = {}
    setmetatable(child, { __index = Base_Ant })
    return child
end

-- Example method in Base_Ant
function Base_Ant.move()
    print("Base ant move")
end

return Base_Ant
