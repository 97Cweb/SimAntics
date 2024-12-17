gas_update = function(in_grid, out_grid, frame)
    local diffusion_rate = 0.1
    local decay_rate = 0.02

    for pheromone_id, layer in pairs(in_grid) do
        for y, row in ipairs(layer) do
            for x, value in ipairs(row) do
                -- Decay
                local decayed_value = value * (1 - decay_rate)

                -- Diffusion: Spread to neighbors
                local spread_amount = decayed_value * diffusion_rate
                out_grid[pheromone_id][y][x] = out_grid[pheromone_id][y][x] + decayed_value

                for dy = -1, 1 do
                    for dx = -1, 1 do
                        local ny, nx = y + dy, x + dx
                        if ny > 0 and ny <= #layer and nx > 0 and nx <= #row and (dx ~= 0 or dy ~= 0) then
                            out_grid[pheromone_id][ny][nx] = out_grid[pheromone_id][ny][nx] + spread_amount / 8
                        end
                    end
                end
            end
        end
    end
end
