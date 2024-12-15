Base_Nest = {}


function Base_Nest.new()
    local self = setmetatable({}, Base_Nest)
    return self
end

function Base_Nest.extend()
    local child = {}
    setmetatable(child, { __index = Base_Nest })
    return child
end

function Base_Nest:smell()
    print("Base_Nest is smelling.")
end

function Base_Nest:sight()
    print("Base_Nest is seeing.")
end

function Base_Nest:update()
    print("Base_Nest is updating.")
end

return Base_Nest
