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
    --print("Lua received update for ant")
	
	for i=1, 33 do
      Base_Ant.memory.add(i)
    end
    Base_Ant.set_velocity(1, 0.2)
	Base_Ant.memory.set(0,{1,2})
	print(Base_Ant.memory.get(0))
end


return Base_Ant
