all:
	ghdl -a comparator.vhd
	ghdl -a mac.vhd
	ghdl -a ram.vhd
	ghdl -a rom.vhd
	ghdl -a seven_seg.vhd
	ghdl -a shifter.vhd
	ghdl -a mlp.vhd
	ghdl -a mlp_tb.vhd
	ghdl -e mlp_tb
	ghdl -r mlp_tb --stop-time=1ms --wave=mlp.ghw
	gtkwave mlp.ghw