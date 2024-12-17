Base_Nest = {}

-- Define methods for Base_Nest
function Base_Nest.new()
    local self = setmetatable({}, { __index = Base_Nest })
    return self
end

function Base_Nest.extend()
    local child = {}
    setmetatable(child, { __index = Base_Nest })
    return child
end


function Base_Nest:update()
    print("Lua received update for nest")
	Base_Nest.spawn_ant()
end


return Base_Nest
