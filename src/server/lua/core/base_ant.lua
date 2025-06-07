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


function Base_Ant:update()
    print("Lua received update for ant")
	Base_Ant.emit_pheromone("danger",5)
	Base_Ant.set_velocity(1, .2)
end


return Base_Ant
