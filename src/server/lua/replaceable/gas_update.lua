gas_update = function(in_grid, out_grid, frame)
	for i, row in python.enumerate(in_grid) do
		for j, cell in python.enumerate(row) do
			local cell = in_grid[i][j]
			if type(cell) == "table" then
				if cell["volume"]  ~= nil then
					out_grid[i][j]["volume"] = math.max(cell["volume"] -1, 0)
				end
			end
			
		end
	end
	return out_grid
end