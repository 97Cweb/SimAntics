map_update = function(in_grid, out_grid, frame)
	for i, row in python.enumerate(in_grid) do
		for j, cell in python.enumerate(row) do
			local cell = in_grid[i][j]
			if type(cell) == "table" then
				-- Example computation: increment resources with a cap
				out_grid[i][j]["resources"] = math.min(cell["resources"] + 1, 10)
			end
			
		end
	end
	return out_grid
end