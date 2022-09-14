all:
	ghdl -a ram.vhd
	ghdl -a ram_tb.vhd
	ghdl -e ram_tb
	ghdl -r ram_tb --wave=ram.ghw --stop-time=35ns
	gtkwave ram.ghw