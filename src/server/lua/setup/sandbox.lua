-- sandbox.lua
function create_sandbox()
    local sandbox = {}
    -- Allowed globals
    sandbox.math = math
    sandbox.print = print
    sandbox.ant_callbacks = {
        get_position = get_position_from_python,
        set_movement = set_movement_from_python
    }
    
    -- Restrict undefined globals
    local mt = {
        __newindex = function(_, key, value)
            error("Attempt to modify global: " .. key, 2)
        end,
        __index = function(_, key)
            error("Attempt to access undefined global: " .. key, 2)
        end
    }
    setmetatable(sandbox, mt)
    return sandbox
end
